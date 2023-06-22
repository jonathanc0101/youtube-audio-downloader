install requeriments using:
    
    python install -r requirements.txt

use with:

    python ./youtube-audio-downloader.py https://www.youtube.com/watch?v=sDYICa6Z6dw

or with:

    python ./download-many.py link1 link2 link3 ...

it downloads audio files to:

    /downloads


to set the album and artist in **ALL** of the files in the ./downloads folder:
    python add-metadata.py "Artist" "Album"