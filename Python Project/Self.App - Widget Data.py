import tkinter as tk
import ttkbootstrap as ttk

app = tk.Tk()
app.title("Widget Data")
app.geometry("300x200")
app.resizable(width = False, height = False)

# Function - Button.
def buttonfunc():
    entry_change = entry.get()

    # Update the Label.

    # label.config(text = change)    # | Normal
    # label.configure(text = change) # | Normal 2

    label["text"] = entry_change     # | Shorthand
    
    # entry.configure(state = "disabled")
    entry["state"] = "disabled"

# Label.
label = ttk.Label(master = app, text = "The Text")
label.pack()

# Entry.
entry = ttk.Entry(master = app)
entry.pack()

# Button.
button = ttk.Button(master = app, text = "Disabled", command = buttonfunc)
button.pack(pady = 10)

def buttonfunc2():
    entry_change = entry.get()
    label["text"] = entry_change 
    entry["state"] = "enabled"

# Button Enabled.
button_2 = ttk.Button(master = app, text = "Enabled", command = buttonfunc2)
button_2.pack(pady = 10)

# Window Icon.
app_icon = tk.PhotoImage(file = "Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)

# Run
app.mainloop()