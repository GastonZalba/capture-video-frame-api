import io, os

from fastapi import APIRouter, Query, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse

from ..controllers.capture import download_and_capture
from ..controllers.cache import get_cache, set_cache
from ..params import CACHE_DAYS_IMG
from ..enums import SourceOption, VideoCodecOption

router = APIRouter()

def delete_file(path: str):
    try:
        os.remove(path)
    except Exception as e:
        print(f"No se pudo eliminar {path}: {e}")


@router.get("/capture-frame")
def get_image(
    vid: str = Query(..., description="Id del video"),
    source: SourceOption = Query(SourceOption.YT, description="Servicio de origen"),
    time: float = Query(..., ge=0, description="Tiempo (en segundos)"),
    resolution: int = Query(360, description="Resolución"),
    vcodec: str = Query(VideoCodecOption.AVC1, description="Codec de video prioritario"),
    background_tasks: BackgroundTasks = None,
    disable_cache: bool = Query(False, description="Deshabilitar caché")
):
    try:
        img_io = None
        
        if not disable_cache:       
            id_cache = f'img_{vid}-{source}-{time}-{resolution}'
            cache = get_cache(id_cache)
            
            if (cache):
                img_io = cache
                
        if not img_io:                     
            img_path = download_and_capture(vid, source, time, resolution, vcodec)
            
            with open(img_path, 'rb') as f:
                img_bytes = f.read()
            img_io = io.BytesIO(img_bytes)
            
            if not disable_cache: 
                set_cache(id_cache, img_io, CACHE_DAYS_IMG)    
                        
            background_tasks.add_task(delete_file, img_path)
            
        return StreamingResponse(img_io, media_type="image/jpeg")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar el video: {str(e)}")

