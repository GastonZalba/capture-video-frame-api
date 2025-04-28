import requests

def test_generate_image():
    # Configurá la URL del endpoint y los parámetros
    endpoint = "http://localhost:8000/capture-frame"
    params = {
        "vid": "8plVWI7InnI",  # URL de ejemplo
        "source": "youtube",
        "time": 90,
        "quality": 134
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        file_out = "test.jpg"
        # Guardar la imagen en un archivo
        with open(file_out, "wb") as f:
            f.write(response.content)
        print(f"✅ Imagen guardada como {file_out}")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    test_generate_image()
