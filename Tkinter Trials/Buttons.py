import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.title('Buttons')
window.geometry('500x400')


def button_func():
    print("This is a basic button.")


button_var = tk.StringVar(value='A button with string var')
button = ttk.Button(window, text='basic button', command=button_func, textvariable=button_var)
button.pack()

check_var = tk.IntVar()
check = ttk.Checkbutton(window,
                        text='Checkbox',
                        command=lambda: print(check_var.get()),
                        variable=check_var,
                        onvalue=100,
                        offvalue=00)
check.pack()

radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text='Radio1', value='radio1', variable=radio_var, command=lambda: print("hello"))
radio1.pack()
radio2 = ttk.Radiobutton(window, text='Radio2', value=1, variable=radio_var)
radio2.pack()
window.mainloop()
