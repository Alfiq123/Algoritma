# import tkinter as tk
import customtkinter as ctk

app = ctk.CTk()

label = ctk.CTkLabel(master=app, text="Hello, My Self"); label.pack(padx=10, pady=10)

entry = ctk.CTkEntry(master=app); entry.pack(padx=10, pady=10)

button = ctk.CTkButton(master=app, text="Confirm"); button.pack(padx=10, pady=10)

app.mainloop()
