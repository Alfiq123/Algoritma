import tkinter as tk
import ttkbootstrap as ttk

app = ttk.Window(themename = "cyborg")
app.title("Widget Data")
# app.geometry("300x150")
app.resizable(width = False, height = False)





def buttonfunc():
    print(string_var.get())
    
    # Set the Value.
    string_var.set("Button Pressed")

# Tkinter Variables.
string_var = tk.StringVar()

    # bool_var = tk.BooleanVar()
    # double_var = tk.DoubleVar()
    # int_var = tk.IntVar()

label = ttk.Label(master = app, text = "The Title", textvariable = string_var)
label.pack(pady = 10, padx = 10)

entry = ttk.Entry(master = app, textvariable = string_var)
entry.pack(pady = 10, padx = 10)

    # entry2 = ttk.Entry(master = app, textvariable = string_var)
    # entry2.pack(pady = 10)

button = ttk.Button(master = app, text = "Button A", command = buttonfunc)
button.pack(pady = 10, padx = 10)

# Exercise:
exercise_var = tk.StringVar(value = "Test")

exercise_entry1 = ttk.Entry(master = app, textvariable = exercise_var)
exercise_entry1.pack(pady = 10, padx = 10)

exercise_entry2 = ttk.Entry(master = app, textvariable = exercise_var)
exercise_entry2.pack(pady = 10, padx = 10)

exercise_label = ttk.Label(master = app, textvariable = exercise_var)
exercise_label.pack(pady = 10, padx = 10)





app_icon = tk.PhotoImage(file = "Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)
app.mainloop()