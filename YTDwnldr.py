from pytube import YouTube
from sys import argv

if len(argv) != 2:
    print("Usage: python script.py <YouTube URL>")
    exit()

link = argv[1]

try:
    yt = YouTube(link)
except Exception as e:
    print(f"Error: {e}")
    exit()

pathout = './ytvideos'

print("Title: ", yt.title)
print("Description: ", yt.description)
print("Duration: ", yt.length)
print("Views: ", yt.views)

try:
    stream = yt.streams.get_highest_resolution()
    stream.download(pathout)
    print("Download completed successfully.")
except Exception as e:
    print(f"Error during download: {e}")
