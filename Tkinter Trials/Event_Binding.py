import tkinter as tk
import ttkbootstrap as ttk


def get_pos(event):
    print(f'x:{event.x} y:{event.y}')


window = tk.Tk()
window.title("Event Binding")

text = ttk.Text(window, height='10', width=50)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='Button')
button.pack()

entry.bind('<Alt-KeyPress-a>', lambda event: print('it is done'))
window.bind('<Motion>', get_pos)
entry.bind('<FocusIn>', lambda event: print('The entry field is selected.'))
entry.bind('<FocusOut>', lambda event: print('The entry field is unselected.'))

window.mainloop()
