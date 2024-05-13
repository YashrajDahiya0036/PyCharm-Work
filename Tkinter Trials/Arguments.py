import tkinter as tk
import ttkbootstrap as ttk


def button_func(entry_string):
    print("Working")
    print(entry_string.get())


window = tk.Tk()
window.title('Arguments')
window.geometry('400x400')

entry_string = tk.StringVar(value='VAR')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text='button', command=lambda: button_func(entry_string))
button.pack()

window.mainloop()
