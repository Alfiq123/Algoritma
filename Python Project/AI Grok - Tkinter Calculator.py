import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")

        # Initialize variables
        self.first_operand = None
        self.pending_operation = None
        self.start_new_number = True

        # Create display
        self.display_var = tk.StringVar()
        self.display_var.set('0')
        self.display = tk.Label(
            self,
            textvariable=self.display_var,
            anchor='e',
            font=('Arial', 18),
            bg='white',
            relief='sunken',
            padx=10,
            pady=10
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Define button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('=', 4, 3),
            ('+', 5, 0)
        ]

        # Create and place buttons
        for (text, row, col) in buttons:
            if text.isdigit():
                cmd = lambda t=text: self.press_digit(t)
            elif text == '.':
                cmd = self.press_decimal
            elif text in ['+', '-', '*', '/']:
                cmd = lambda t=text: self.press_operation(t)
            elif text == '=':
                cmd = self.press_equals
            elif text == 'C':
                cmd = self.press_clear
            button = tk.Button(
                self,
                text=text,
                command=cmd,
                font=('Arial', 18),
                width=5,
                height=2
            )
            if text == '+' or text == '=' or text == 'C':
                button.grid(row=row, column=col, columnspan=1, sticky='nsew')
            else:
                button.grid(row=row, column=col, sticky='nsew')

        # Configure grid weights for resizing
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def press_digit(self, digit):
        """Handle digit button presses."""
        current = self.display_var.get()
        if self.start_new_number:
            self.display_var.set(digit)
            self.start_new_number = False
        else:
            self.display_var.set(current + digit)

    def press_decimal(self):
        """Handle decimal point button press."""
        current = self.display_var.get()
        if self.start_new_number:
            self.display_var.set('0.')
            self.start_new_number = False
        elif '.' not in current:
            self.display_var.set(current + '.')

    def press_operation(self, op):
        """Handle operation button presses (+, -, *, /)."""
        if self.start_new_number and self.first_operand is not None:
            self.pending_operation = op
        else:
            current = float(self.display_var.get())
            if self.pending_operation is not None:
                if self.pending_operation == '+':
                    self.first_operand += current
                elif self.pending_operation == '-':
                    self.first_operand -= current
                elif self.pending_operation == '*':
                    self.first_operand *= current
                elif self.pending_operation == '/':
                    if current == 0:
                        self.display_var.set('Error')
                        self.start_new_number = True
                        return
                    else:
                        self.first_operand /= current
                self.display_var.set(str(self.first_operand))
            else:
                self.first_operand = current
            self.pending_operation = op
            self.start_new_number = True

    def press_equals(self):
        """Handle equals button press."""
        if self.pending_operation is not None:
            current = float(self.display_var.get())
            if self.pending_operation == '+':
                self.first_operand += current
            elif self.pending_operation == '-':
                self.first_operand -= current
            elif self.pending_operation == '*':
                self.first_operand *= current
            elif self.pending_operation == '/':
                if current == 0:
                    self.display_var.set('Error')
                    self.start_new_number = True
                    return
                else:
                    self.first_operand /= current
            self.display_var.set(str(self.first_operand))
            self.pending_operation = None
            self.start_new_number = True

    def press_clear(self):
        """Handle clear button press."""
        self.display_var.set('0')
        self.first_operand = None
        self.pending_operation = None
        self.start_new_number = True

if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()