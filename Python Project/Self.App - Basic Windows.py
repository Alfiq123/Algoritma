import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb

# Create a Window
app = ttkb.Window(themename = "darkly")
app.title("Something")
# app.geometry("750x550")
app.resizable(width = False, height = False)

# Widget Command
def button_1():
    print("Clicked...")

def button_2():
    print("Clicked Again...")

# Ttk Label
label = ttkb.Label(master = app, text = "Welcome", font = ("Times New Roman", 24, "bold"))
label.pack(pady = 10)

# Ttk Text
text = ttkb.Text(master = app)
text.pack(fill = "both", pady= 10)

# Frame to hold Entry and Button
button_frame = ttkb.Frame(master = app)
button_frame.pack(side = "top", pady = 10)

# Center the button_frame horizontally
button_frame.pack_configure(anchor = "center")

# Ttk Entry
entry = ttkb.Entry(master = button_frame)
entry.pack(side = "left", padx = 5)

# Ttk Button
button = ttk.Button(master = button_frame, text = "Accept", command = lambda: print("Clicked..."))
button.pack(side = "left", padx = 5)

# Exercise Label
exercise_label = ttk.Label(master = app, text = "My Label")
exercise_label.pack(pady = 10)

# Exercise Button
# exercise_button = ttk.Button(master = app, text = "Button 2", command = button_2)
exercise_button = ttk.Button(master = app, text = "Button 2", command = lambda: print("Hello World!"))
exercise_button.pack(pady = 10)

# Window Icon
app_icon = tk.PhotoImage(file = "Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)

# Loop the Program
app.mainloop()