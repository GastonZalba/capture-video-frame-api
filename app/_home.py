
import markdown


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

def get_home():
    return f"{dark_mode_css}{readme_html}"