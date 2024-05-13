from pytube import YouTube

url = "https://youtu.be/Oxtp2ygyQog?si=Er1Lw_6x1FFeFzWl"
yt = YouTube(url)
for st in yt.streams:
    print(st)
