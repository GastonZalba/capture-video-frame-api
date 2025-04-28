import markdown
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .capture_frame import router
from .cors import add_cors_middleware

app = FastAPI(
    title="Capture Video Frame API",
    description="Captura un frame de video en el tiempo solicitado a partir de un id de YouTube",
    version="1.0.0"
)

add_cors_middleware(app)

app.include_router(router)

with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

readme_html = markdown.markdown(readme_content, extensions=['tables'])

dark_mode_css = """
<style>
body {
    max-width: 800px; /* limita el ancho máximo */
    margin: 0 auto; /* centra el contenido */
    background-color: #121212;
    color: #e0e0e0;
    font-family: Arial, sans-serif;
    padding: 20px;
}
a { color: #bb86fc; }
h1, h2, h3 { color: #ffffff; }
code { background-color: #333333; color: #ffffff; padding: 2px 4px; border-radius: 4px; }
pre { background-color: #333333; padding: 10px; border-radius: 6px; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #444; padding: 8px; }
th { background-color: #222; }
</style>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    return f"{dark_mode_css}{readme_html}"