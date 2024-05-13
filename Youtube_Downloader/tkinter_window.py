import tkinter as tk
import ttkbootstrap as ttk


def value_print():
    var = playlist_entry_string.get()
    print(var)


window = ttk.Window(themename="darkly")

window.geometry("500x500")
window.title("YouTube Downloader")

title_label = ttk.Label(master=window, text="YouTube Downloader", font="Calibri 20 bold")
title_label.pack()

# For video
video_input_frame = ttk.Frame(master=window)
video_entry_string = ttk.StringVar()
video_entry = ttk.Entry(master=video_input_frame, textvariable=video_entry_string)
video_button = ttk.Button(master=video_input_frame, text="video")
print(video_entry_string)
video_entry.pack(side="left")
video_button.pack(side="left")
video_input_frame.pack(pady=20)

# For playlist
playlist_input_frame = ttk.Frame(master=window)
playlist_entry_string = ttk.StringVar()
playlist_entry = ttk.Entry(master=playlist_input_frame, textvariable=playlist_entry_string)
playlist_button = ttk.Button(master=playlist_input_frame, text="playlist", command=value_print)
print(playlist_entry_string)
playlist_entry.pack(side="left")
playlist_button.pack(side="left")
playlist_input_frame.pack(pady=20)

window.mainloop()
