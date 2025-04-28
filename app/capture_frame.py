import io

from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import StreamingResponse

from .ytdl import download_and_capture
from .enums import QualityOption, SourceOption

router = APIRouter()

@router.get("/capture-frame")
def get_image(
    vid: str = Query(..., description="Id del video"),
    source: str = Query(SourceOption.YT, description="Servicio de origen"),
    time: int = Query(..., ge=0, description="Tiempo (en segundos)"),
    quality: QualityOption = Query(QualityOption.Q137, description="Calidad")
):
    try:
        img = download_and_capture(vid, source, time, quality)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar el video: {str(e)}")

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/jpeg")