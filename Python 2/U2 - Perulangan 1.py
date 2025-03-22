import tkinter as tk
import ttkbootstrap as ttk

# Layar.
app = ttk.Window(themename = "darkly")
app.title("Pengubah km ke cm")
app.resizable(width = False, height = False)

# == Proses == #
# Fungsi - Mengonversi ke cm.
def konversi():
    mile_input = entry_int.get()
    km_output = mile_input * 10000
    output_string.set(f"{km_output:,.0f} cm")

# Judul.
title_label = ttk.Label(master = app, text = "Kilometer ke Sentimeter", font = ("Times New Roman", 22, "bold"))
title_label.pack(padx = 10, pady = 10)

# Inputan.
input_frame = ttk.Frame(master = app)
input_frame.pack(pady = 10)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
entry.pack(side = "left", padx = 10)

button = ttk.Button(master = input_frame, text = "Konversi", command = konversi)
button.pack(side = "left", padx = 10)

# Keluaran (Hasil).
output_string = tk.StringVar()
output_label = ttk.Label(master = app, text = "Hasil", font= ("Times New Roman", 24), textvariable = output_string)
output_label.pack(pady = 5)

# Icon.
app_icon = tk.PhotoImage(file="Python Project/Icon_Python.png")
app.iconphoto(True, app_icon)
app.mainloop()