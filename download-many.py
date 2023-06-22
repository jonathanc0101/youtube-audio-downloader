import concurrent.futures
import subprocess
import sys

def download_audio(link):
    subprocess.run(["python", "youtube-audio-downloader.py", link])

if __name__ == "__main__":
    # Obtener los enlaces de YouTube desde la línea de comandos
    links = sys.argv[1:]

    # Crear un grupo de subprocesos para ejecutar las descargas en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Llamar a la función de descarga para cada enlace en el grupo de subprocesos
        results = executor.map(download_audio, links)