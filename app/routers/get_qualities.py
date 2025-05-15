from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse

from ..controllers.youtube import get_youtube_qualities
from ..controllers.cache import get_cache, set_cache
from ..params import CACHE_DAYS_JSON
from ..enums import SourceOption

router = APIRouter()

@router.get("/get-qualities")
def get_qualities(
    vid: str = Query(..., description="Id del video"),
    source: SourceOption = Query(SourceOption.YT, description="Servicio de origen")
):
    try:    
        
        id_cache = f'q_{vid}-{source}'
        cache = get_cache(id_cache)
        
        if (cache):
            qualities = cache
        else:
            if (source == SourceOption.YT):
                qualities = get_youtube_qualities(vid)
            else:
                return
            
            set_cache(id_cache, qualities, CACHE_DAYS_JSON)
            
        return JSONResponse(content=qualities, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener calidades: {str(e)}")

