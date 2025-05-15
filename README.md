# Capture Video Frame API

**FastAPI** que devuelve una captura de video en base a un ID, un servicio (como YouTube) y un tiempo de video en una calidad especificada. También permite averiguar qué calidades de video existen antes de realizar la descarga.

## Funcionamiento general
- Captura de imagen de YouTube: se utiliza el módulo [yt_dlp](https://pypi.org/project/yt-dlp/) para realizar la descarga en el segundo solicitado, en formato video webm (de 0.1 segundo de duración) y en la calidad requerida. 
- Usando [ffmpeg](https://www.ffmpeg.org/) se captura el primer frame de ese fragmento, retornándolo al cliente como imagen jpg.
- Cacheado de recursos: como los tiempos de las peticiones usando yt_dlp son muy largos, se utiliza el módulo [diskcache](https://pypi.org/project/diskcache/) para almacenar temporalmente cada respuesta (30 días para imágenes, 360 para los `.json` de calidades existentes), posibilitando responder instantáneamente futuras peticiones. Los elementos cacheados se almacenan en la carpeta temporal del sistema (retornada por `tempfile.gettempdir()`)

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
## Uso
### Endpoint `/capture-frame`

Realizar una petición GET para obtener una imagen con los siguientes parámetros:

| Parámetro | Tipo  | Descripción                                 |
|-----------|-------|---------------------------------------------|
| vid       | str   | ID del video      |
| source   | SourceOption   | Origen del video (ej: youtube)        |
| time   | float   | Tiempo de inicio en segundos (ej: 30)        |
| resolution   | int   | Resolución vertical del video (por defecto 360)  |

#### Resoluciones habituales
* 144
* 240
* 360
* 480
* 720
* 1080    
* 1440
* 2160

**Ejemplo de URL de petición**:
[http://localhost:8000/capture-frame?vid=dQw4w9WgXcQ&source=youtube&time=6.6&resolution=360](http://localhost:8000/capture-frame?vid=dQw4w9WgXcQ&source=youtube&time=6.6&resolution=360)


### Endpoint `/get-qualities`

Realizar una petición GET para obtener todas las calidades exitentes del video, con los siguientes parámetros:

| Parámetro | Tipo  | Descripción                                 |
|-----------|-------|---------------------------------------------|
| vid       | str   | ID del video      |
| source   | SourceOption   | Origen del video (ej: youtube)        |

**Ejemplo de URL de petición**:
[http://localhost:8000/get-qualities?vid=dQw4w9WgXcQ&source=youtube](http://localhost:8000/get-qualities?vid=dQw4w9WgXcQ&source=youtube)

---

## Tests

Hay un archivo `test.py` que hace una petición de prueba al servidor, obtiene las calidades disponibles del video y una imagen en el disco.

1. Asegurate de que la API esté corriendo (`uvicorn` abierto).

2. Ejecutá el test:

    ```bash
    python test.py
    ```

3. Si todo sale bien, se generará un archivo `test.jpg` en el mismo directorio.

---

## Notas

- La aplicación está configurada para permitir solicitudes CORS únicamente desde dominios `*.minfra.gba.gob.ar`.

---

# #TODO
- Usar env para manejo de variables por entorno