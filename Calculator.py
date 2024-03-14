import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=50, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4,padx=50, pady=50)
number_button_bg = "lightgrey"
operator_button_bg = "yellow"
clear_button_bg = "orange"
equal_button_bg = "green"

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('.', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    if text.isdigit():
        button_bg = number_button_bg
    else:
        button_bg = operator_button_bg
    button = tk.Button(root, text=text, padx=20, pady=10, bg=button_bg, command=lambda text=text: button_click(text))
    button.grid(row=row, column=column)

zerobutton = tk.Button(root, text="0", padx=74, pady=20, bg=number_button_bg, command=lambda text="0": button_click(text))
zerobutton.grid(row=4, column=0, columnspan=2)

clear_button = tk.Button(root, text="Clear", padx=60, pady=20, bg=clear_button_bg, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2)

equal_button = tk.Button(root, text="=", padx=60, pady=20, bg=equal_button_bg, command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2)

root.mainloop()
