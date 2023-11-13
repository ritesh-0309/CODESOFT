import tkinter as tk

def click(button_text):
    current_entry_text = entry.get()

    if button_text == "=":
        try:
            result = eval(current_entry_text)
            entry_clr()
            display_result(result)
        except Exception as e:
            entry_clr()
            display_error()

    elif button_text == "C":
        entry_clr()

    else:
        entry_append(button_text)

def entry_clr():
    entry.delete(0, tk.END)

def display_result(result):
    entry_clr()
    entry.insert(tk.END, str(result))

def display_error():
    entry_clr()
    entry.insert(tk.END, "Error")

def entry_append(text):
    entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=24, font=("Helvetica", 48), justify="right", bd=20, bg="blue")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, width=16, height=4, command=lambda b=button_text: click(b), bg="yellow", font=("Helvetica", 16))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
