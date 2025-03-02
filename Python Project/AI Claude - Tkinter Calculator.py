import tkinter as tk
from tkinter import ttk
import re

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("300x400")
        self.master.resizable(False, False)
        self.master.configure(bg="#f0f0f0")
        
        # Set style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12))
        
        # Expression variable
        self.expression = ""
        
        # Create display frame
        self.display_frame = tk.Frame(self.master, width=300, height=80, bg="#f0f0f0")
        self.display_frame.pack(pady=10)
        
        # Create input field
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(
            self.display_frame,
            font=('Arial', 20),
            textvariable=self.input_text,
            width=18,
            bd=5,
            relief=tk.RIDGE,
            justify=tk.RIGHT
        )
        self.input_field.grid(row=0, column=0, ipady=10)
        self.input_field.pack(fill=tk.BOTH, expand=True)
        
        # Create button frame
        self.buttons_frame = tk.Frame(self.master, width=300, height=300, bg="#f0f0f0")
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create buttons
        self.create_buttons()
        
    def create_buttons(self):
        # Define button layout
        button_layout = [
            ('C', 'CE', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '±', '=')
        ]
        
        # Define button colors
        operator_bg = "#f5923e"
        number_bg = "#ffffff"
        special_bg = "#e0e0e0"
        equals_bg = "#4CAF50"
        
        # Create buttons
        for i, row in enumerate(button_layout):
            for j, text in enumerate(row):
                # Determine button color
                if text in ('/', '*', '-', '+'):
                    bg_color = operator_bg
                elif text in ('C', 'CE', '%', '±'):
                    bg_color = special_bg
                elif text == '=':
                    bg_color = equals_bg
                else:
                    bg_color = number_bg
                
                button = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=('Arial', 16),
                    fg="black",
                    bg=bg_color,
                    bd=1,
                    relief=tk.RAISED,
                    width=5,
                    height=2,
                    command=lambda t=text: self.button_click(t)
                )
                button.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
        
        # Configure row and column weights for resizing
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.buttons_frame.columnconfigure(j, weight=1)
    
    def button_click(self, button_text):
        if button_text == 'C':
            self.clear_all()
        elif button_text == 'CE':
            self.clear_entry()
        elif button_text == '=':
            self.calculate()
        elif button_text == '±':
            self.negate()
        elif button_text == '%':
            self.percentage()
        else:
            self.update_expression(button_text)
    
    def clear_all(self):
        self.expression = ""
        self.input_text.set("")
    
    def clear_entry(self):
        # Clear the last entry
        current_text = self.input_text.get()
        if current_text:
            # Find the last number or operator
            match = re.search(r'[\+\-\*\/]?\d*\.?\d*$', current_text)
            if match:
                self.expression = current_text[:match.start()]
                self.input_text.set(self.expression)
    
    def update_expression(self, value):
        self.expression += value
        self.input_text.set(self.expression)
    
    def calculate(self):
        try:
            # Replace % with /100 for calculation
            expr = self.expression.replace('%', '/100')
            
            # Evaluate the expression and round to avoid floating point errors
            result = round(eval(expr), 10)
            
            # Handle trailing zeros for better display
            if result == int(result):
                result = int(result)
                
            self.input_text.set(result)
            self.expression = str(result)
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""
    
    def negate(self):
        try:
            # If expression is empty, do nothing
            if not self.expression:
                return
                
            # If current value is just a number, negate it
            if self.expression.replace('.', '').replace('-', '').isdigit():
                if self.expression.startswith('-'):
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
                self.input_text.set(self.expression)
            else:
                # Find the last number in the expression
                match = re.search(r'([\+\-\*\/])?([\d\.]+)$', self.expression)
                if match:
                    operator, number = match.groups()
                    if operator == '-':
                        # If preceded by a minus, replace with plus
                        self.expression = self.expression[:match.start()] + '+' + number
                    elif operator == '+':
                        # If preceded by a plus, replace with minus
                        self.expression = self.expression[:match.start()] + '-' + number
                    elif operator in ('*', '/') or operator is None:
                        # If preceded by * or / or at the start, insert a negative
                        prefix = self.expression[:match.start() + len(operator or '')]
                        self.expression = prefix + '-' + number
                    self.input_text.set(self.expression)
        except Exception:
            pass
    
    def percentage(self):
        self.update_expression('%')

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()