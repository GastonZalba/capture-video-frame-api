import requests
import time

params = {
    "vid": "aB7dgH_ekl4",  # URL de ejemplo
    "source": "youtube",
    "time": 6.6,
    "vcodec": "vp9", 
    "resolution": 2160,
    #"disable_cache": True
}

def test_get_qualities():
    endpoint = "http://localhost:8000/get-qualities"

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        print(f"✅ Calidades obtenidas: {response.content}")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")


def test_generate_image():
    inicio = time.time()

    endpoint = "http://localhost:8000/capture-frame"

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        file_out = "test.jpg"
        # Guardar la imagen en un archivo
        with open(file_out, "wb") as f:
            f.write(response.content)
        print(f"✅ Imagen guardada como {file_out}")
        fin = time.time()    
        print(f"La captura tardó {fin - inicio:.4f} segundos.")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
    



if __name__ == "__main__":
    test_get_qualities()
    test_generate_image()
