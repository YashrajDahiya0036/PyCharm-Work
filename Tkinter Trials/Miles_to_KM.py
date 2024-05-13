import tkinter as tk
# widgets
import ttkbootstrap as ttk


def convert():
    miles = entry_int.get()
    km = str(miles * 1.61)
    output_string.set(km)


# window
# window = tk.Tk()
window = ttk.Window(themename="darkly")
window.title("Miles to km")
window.geometry("500x250")

# Title
title_label = ttk.Label(master=window, text="MILES TO KM CONVERTOR", font="Calibri 24 bold")
title_label.pack(pady=20)

# input frame
input_frame = ttk.Frame(master=window)
entry_int = ttk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
convert = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left")
convert.pack(side="left")
input_frame.pack()

# output frame
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="output", font="Calibre 24", textvariable=output_string)
output_label.pack(pady=25)

# run
window.mainloop()
