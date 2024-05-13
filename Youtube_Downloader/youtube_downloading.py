from pytube import YouTube
from pytube import Playlist
from tkinter import filedialog
import os
import ffmpeg


def open_file_dia():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder is: {folder}")
    return folder


def get_res(vid_url):
    yt = YouTube(vid_url)
    stream = yt.streams.filter(file_extension="mp4", adaptive=True, type="video")
    for st in stream:
        print(f"this is {st.resolution}")


def get_audio(vid_url):
    yt = YouTube(vid_url)
    stream = yt.streams.filter(type="audio", abr="128kbps")
    print(stream)


def video_download(video_url, save_path, resolution="1080p"):
    print(video_url)
    print(save_path)
    print(resolution)
    # try:
    #     yt = YouTube(video_url)
    #     video_stream = yt.streams.filter(res=resolution, file_extension="mp4", adaptive=True, type="video")
    #     audio_stream = yt.streams.filter(type="audio", abr="128kbps")
    #     vid_i_tag = None
    #     aud_i_tag = 140
    #     for st in video_stream:
    #         vid_i_tag = st.itag
    #     for st in audio_stream:
    #         aud_i_tag = st.itag
    #     vid_i_tag = int(vid_i_tag)
    #     print(video_stream)
    #
    #     # For video
    #     video = video_stream.get_by_itag(vid_i_tag)
    #     video_title = video.title
    #     old_video_path = video.download(output_path=save_path)
    #     new_video_title = "v.mp4"
    #     new_video_path = os.path.join(save_path, new_video_title)
    #     os.rename(old_video_path, new_video_path)
    #     print("Video downloaded successfully.")
    #
    #     # For audio
    #     audio = audio_stream.get_by_itag(aud_i_tag)
    #     audio_title = audio.title
    #     old_audio_path = audio.download(output_path=save_path)
    #     new_audio_title = "a.mp3"
    #     new_audio_path = os.path.join(save_path, new_audio_title)
    #     os.rename(old_audio_path, new_audio_path)
    #     print("Audio downloaded successfully.")
    #     print("playing audio:")
    #     # os.system(new_audio_path)
    #
    #     # ffmpeg
    #     output_file = os.path.join(save_path, video_title+".mp4")
    #     input_video = ffmpeg.input(new_video_path)
    #     input_audio = ffmpeg.input(new_audio_path)
    #     ffmpeg.concat(input_video, input_audio, v=1, a=1).output(output_file).run()
    #
    #     # removing old files
    #     os.remove(new_video_path)
    #     os.remove(new_audio_path)
    #
    # except Exception as e:
    #     print(e)


def playlist_download(playlist_url, save_path, resolution="1080p"):
    p = Playlist(playlist_url)
    for video_url in p:
        video_download(video_url, save_path, resolution)


url = "https://youtu.be/__bNjF-xR1U?si=WrEsMAqotYXhaavt"
save = "C:/Users/yashr/Downloads"
# video_download(url, save, "360p")
# get_res(url)
# get_audio(url)

if __name__ == "__main__":
    first_input = int(input("Enter 1 for downloading video\nEnter 2 for downloading playlist\n"))
    if first_input == 1:
        save_path = open_file_dia()
        vid_url = input("Enter the Url of the video: ")
        get_res(vid_url)
        res = input("Enter a resolution from above.")
        video_download(vid_url, save_path, res)

    if first_input == 2:
        save_path = open_file_dia()
        playlist_u = input("Enter the playlist url")

        playlist_download(playlist_u, save_path)
