import markdown
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

from .routers.capture_frame import router
from .middlewares.cors import add_cors_middleware
from ._home import get_home

app = FastAPI(
    title="Capture Video Frame API",
    description="Captura un frame de video en el tiempo solicitado a partir de un id de YouTube",
    version="1.0.0"
)

add_cors_middleware(app)

app.include_router(router)

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')

@app.get("/", response_class=HTMLResponse)
def read_root():
    return get_home()