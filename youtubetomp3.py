#!/bin/env python
# Requires: youtube_dl module
# Requires: ffmpeg
# Usage:
#
# python youtube2mp3.py <URL>, ...
# 
# Example:
# 
# python youtube2mp3.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

import youtube_dl, sys, os, re, shutil

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if __name__ == "__main__":
    filenames = []
    
    with open("links.txt") as file:
        filenames = file.read().split('\n')
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(filenames)
        
    open("links.txt", "w").close()
    
    files = []
    for filename in sorted(os.listdir(os.curdir)):
        if filename[-4:] == ".mp3" and filename[-16:-15] == "-":
            new_filename = filename[:-16]+filename[-4:]
            os.rename(filename, new_filename)
            shutil.move(new_filename, "../" + new_filename)
            files.append(filename)

    ## print(files)
    print(len(files))
