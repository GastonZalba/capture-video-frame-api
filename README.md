# Capture Video Frame API

Api pequeña en **FastAPI** que devuelve una captura de video en base a un ID, un servicio (como YouTube), un tiempo de captura en la calidad especificada

## Funcionamiento general
- Youtube: 
    - se utiliza el módulo [yt_dlp](https://pypi.org/project/yt-dlp/) para realizar la descarga en el segundo solicitado (de 0.1 segundo de duración) en la calidad especificada. 
    - Usando [ffmpeg](https://www.ffmpeg.org/) se captura el primer frame de ese fragmento, retornándolo al cliente como imagen jpg.

---

## Requisitos

- Python 3.8+
- pip
- ffmpeg

---

## Instalación

1. Cloná o descargá el proyecto.

2. Creá un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv/Scripts/activate     # Windows
    ```

3. Instalá las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

---

## Cómo iniciar la aplicación

1. Asegurate de estar en el directorio raíz del proyecto.

2. Ejecutá el servidor con **Uvicorn**:

    ```bash
    uvicorn app.main:app --reload
    ```

3. La API estará disponible en:

    ```
    http://localhost:8000
    ```

---

## Cómo usar el endpoint `/capture-frame`

Realizar una petición GET con los siguientes parámetros:

| Parámetro | Tipo  | Descripción                                 |
|-----------|-------|---------------------------------------------|
| vid       | str   | ID del video      |
| source   | str   | Origen del video (ej: youtube)        |
| time   | int   | Tiempo de inicio en segundos (ej: 30)        |
| quality   | str   | Calidad del video (por defecto 134 = 360p)  |

### Calidades
- 134 (360)
- 135 (480)
- 136 (720)
- 137 (1080)
- 138 (2k)
- 139 (4k)

**Ejemplo de URL de petición**:
`http://localhost:8000/capture-frame?vid=XXXXX&source=youtube&time=3&quality=135`


---

## Cómo correr el test

Hay un archivo `test.py` que hace una petición de prueba al servidor y guarda la imagen en el disco.

1. Asegurate de que la API esté corriendo (`uvicorn` abierto).

2. Ejecutá el test:

    ```bash
    python test.py
    ```

3. Si todo sale bien, se generará un archivo `test.jpg` en el mismo directorio.

---

## Notas

- El parámetro `quality` depende de las resoluciones disponibles del video.
- La aplicación está configurada para permitir solicitudes CORS únicamente desde dominios `*.minfra.gba.gob.ar`.

---
