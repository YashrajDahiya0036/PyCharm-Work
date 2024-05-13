# import tkinter as tk
import ttkbootstrap as ttk


def button_func():
    print(entry.get())
    label.config(text="Hell NO")
    entry['state'] = 'disabled'


def button_reset_func():
    label['text'] = 'some other text'
    entry['state'] = 'enabled'


window = ttk.Window()
window.title("Getting And Setting Widgets")
window.geometry('500x500')

entry_string = ttk.StringVar(value='starting')
label = ttk.Label(master=window, text='hehe;(', textvariable=entry_string)
label.pack()
entry = ttk.Entry(master=window, textvariable=entry_string)
entry.pack()
button = ttk.Button(master=window, text='Fuck You', command=button_func)
button.pack()
button2 = ttk.Button(master=window, text='Fuck You2', command=button_reset_func)
button2.pack()
multi_string = ttk.StringVar(value='test')
label2 = ttk.Label(master=window, text='HEHE', textvariable=multi_string)
label2.pack()
entry2 = ttk.Entry(master=window, textvariable=multi_string)
entry2.pack()
entry3 = ttk.Entry(master=window, textvariable=multi_string)
entry3.pack()
window.mainloop()
