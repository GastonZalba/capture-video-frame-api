from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse

from ..controllers.youtube import get_youtube_qualities
from ..enums import SourceOption

router = APIRouter()

@router.get("/get-qualities")
def get_qualities(
    vid: str = Query(..., description="Id del video"),
    source: SourceOption = Query(SourceOption.YT, description="Servicio de origen")
):
    try:        
        if (source == SourceOption.YT):
            qualities = get_youtube_qualities(vid)
        return JSONResponse(content=qualities, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener calidades: {str(e)}")

