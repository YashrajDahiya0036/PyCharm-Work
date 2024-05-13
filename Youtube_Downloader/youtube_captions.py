from pytube import YouTube
from tkinter import filedialog


def get_captions(video_url, save_path=None):
    yt = YouTube(video_url)
    yt.bypass_age_gate()
    # yt.streams
    caption = yt.captions.get_by_language_code('a.en')
    print(caption)
    # caption.xml_captions
    caption.download("cap.srt", srt=True, output_path=save_path)
    # print(caption.geneate_srt_captions())
    # print(srt_cap)


url = "https://youtu.be/7mSH86O2qzA?si=PBmYnyvLBV-vjBrJ"
# path = "C:/Work/Python"
folder = filedialog.askdirectory()
get_captions(url, folder)
