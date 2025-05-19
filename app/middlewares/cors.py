from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://*.minfra.gba.gob.ar"],
        allow_origin_regex=r"https:\/\/.*\.minfra\.gba\.gob\.ar$",
        allow_credentials=True,
        allow_methods=["GET"]
    )