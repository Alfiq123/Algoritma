import tkinter as tk
import ttkbootstrap as ttk
# from tkinter import ttk

# Window
app = ttk.Window(themename = "journal")
app.title("Program 1")
app.geometry("300x150")
app.resizable(width = False, height = False)

# Main Program

# Function - Calculation
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(str(km_output) + " km")

# Title Label
title_label = ttk.Label(master = app, text = "Miles to Kilometers", font = ("Times New Roman", 24, "bold"))
title_label.pack()

# Input
input_frame = ttk.Frame(master = app)
input_frame.pack(pady = 10)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
entry.pack(side = "left", padx = 10)

button = ttk.Button(master = input_frame, text = "Convert", command = convert)
button.pack(side = "left", padx = 10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master = app, text = "Output", font= ("Times New Roman", 24), textvariable = output_string)
output_label.pack(pady = 5)

# Window Icon
app_icon = tk.PhotoImage(file="Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)

# Run
app.mainloop()