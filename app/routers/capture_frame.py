import io

from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import StreamingResponse

from ..controllers.capture import download_and_capture
from ..enums import SourceOption

router = APIRouter()

@router.get("/capture-frame")
def get_image(
    vid: str = Query(..., description="Id del video"),
    source: SourceOption = Query(SourceOption.YT, description="Servicio de origen"),
    time: float = Query(..., ge=0, description="Tiempo (en segundos)"),
    resolution: int = Query(360, description="Resolución")
):
    try:
        img = download_and_capture(vid, source, time, resolution)
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        return StreamingResponse(img_io, media_type="image/jpeg")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar el video: {str(e)}")

