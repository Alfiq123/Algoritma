import tkinter as tk

# Initialize main application window
root = tk.Tk()
root.title("Calculator")

# Global expression variable
expression = ""

# StringVar to update the display Entry widget
equation = tk.StringVar()

# Function to update the expression in the Entry widget when a button is clicked
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to clear the current expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to evaluate the expression and update the display with the result
def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result  # Allow further calculations
    except Exception:
        equation.set("Error")
        expression = ""

# Create the display entry widget
entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=4,
                 width=14, justify='right')
entry.grid(columnspan=4)

# Define calculator buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons in a grid layout
row = 1
col = 0
for btn in buttons:
    if btn == "C":
        action = clear
    elif btn == "=":
        action = equal
    else:
        # Use a lambda to capture the current button text
        action = lambda x=btn: press(x)
    tk.Button(root, text=btn, padx=20, pady=20, font=("Arial", 20), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the Tkinter event loop
root.mainloop()
