import argparse
import yt_dlp as youtube_dl
import os

# Crear la carpeta "downloads" si no existe
if not os.path.exists("downloads"):
    os.makedirs("downloads")

def download_audio(url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'audio')

        ydl.download([url])

# Ejemplo de uso
# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Reemplaza con tu URL de video
# download_audio(video_url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="YouTube Video to MP3 Downloader")
    parser.add_argument("url", help="URL of the YouTube video")

    args = parser.parse_args()
    video_url = args.url

    download_audio(video_url)
