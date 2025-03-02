import tkinter as tk

def add_to_display(value):
    global calculation_done
    current = display_var.get()
    if current == "Error":
        current = ''
        calculation_done = False
    if calculation_done:
        if value in '0123456789.(':
            current = value
            calculation_done = False
        else:
            current += value
            calculation_done = False
    else:
        current += value
    display_var.set(current)

def clear_display():
    display_var.set('')
    calculation_done = False

def backspace():
    current = display_var.get()
    display_var.set(current[:-1])
    calculation_done = False

def calculate():
    global calculation_done
    try:
        current = display_var.get()
        result = eval(current)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        display_var.set(result)
        calculation_done = True
    except:
        display_var.set("Error")
        calculation_done = False

root = tk.Tk()
root.title("Calculator")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, state='readonly', font=('Arial', 14))
display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

button_grid = [
    ['(', ')', 'C', '←'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

calculation_done = False

for row_idx, row in enumerate(button_grid, start=1):
    for col_idx, text in enumerate(row):
        if text == '=':
            cmd = calculate
        elif text == 'C':
            cmd = clear_display
        elif text == '←':
            cmd = backspace
        else:
            cmd = lambda t=text: add_to_display(t)
        btn = tk.Button(root, text=text, width=5, height=2, command=cmd)
        if row_idx == 5 and col_idx == 0:
            btn.grid(row=row_idx, column=col_idx, columnspan=2, sticky='nsew')
        else:
            btn.grid(row=row_idx, column=col_idx, sticky='nsew')

# Configure grid weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()