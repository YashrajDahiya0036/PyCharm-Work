import tkinter as tk
import ttkbootstrap as ttk

# window = tk.Tk()
window = ttk.Window()
window.title('Combo and Spin')
window.geometry('500x300')

items = ('Coke', 'Pepsi', 'Dew')
food_string = tk.StringVar()
combo = ttk.Combobox(window, textvariable=food_string)
combo.config(values=items)
combo.pack()

combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f'The selected value is: {food_string.get()}'))

combo_label = ttk.Label(window, text='A Label')
combo_label.pack()

spin = ttk.Spinbox(window, from_=3, to=20, increment=3, command=lambda: print('A arrow was pressed.'))
spin.bind('<<Increment>>', lambda: print('Up'))
# spin['values'] = (1, 2, 3, 4, 5)
spin.pack()

window.mainloop()
