
import os
from pytube import YouTube

try:
    newpath = r'Youtube Downloaded videos'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    print("coded by Dev7knight")
    print("don't forget to visit : https://freemovies-ops.github.io/ for free movies")
    print("found a bug or want to add something new report it from this link : https://dev7knight.github.io/Report.html")


    link = input("youtube link: ")
    video = YouTube(link).streams.filter(res="720p").first()
    print("downloading")
    video.download(r'Youtube Downloaded videos')
    print("Downloaded!")

except SyntaxError:
    print("error happened please reset program")
