from mutagen.easyid3 import EasyID3
import argparse
import os

def add_metadata(artist, album, filepath):
    audio = EasyID3(filepath)
    audio['artist'] = artist
    audio['album'] = album
    audio.save()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("artist", help="Nombre del artista")
    parser.add_argument("album", help="Nombre del álbum")
    args = parser.parse_args()

    artist = args.artist
    album = args.album

    # Directorio donde se encuentran los archivos descargados
    directory = 'downloads'

    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            add_metadata(artist, album, filepath)