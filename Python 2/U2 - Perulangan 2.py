import tkinter as tk
import ttkbootstrap as ttk

def deposit():
    d = tk.Toplevel()
    d.title("Deposit")
    d.resizable(width = False, height = False)

    d_judul = ttk.Label(master = d, text = "Deposit", font = ("DejaVu Math TeX Gyre", 24, "bold"))
    d_judul.pack(padx = 10, pady = 10)

    d_judul2 = ttk.Label(master = d, text = "Masukkan Dana", font = ("Times New Roman", 12))
    d_judul2.pack(padx = 10, pady = 10, side = "left")

    d_entry = ttk.Entry(master = d)
    d_entry.pack(padx = 10, pady = 10, side = "left")

    print("Deposit")

def Withdraw():
    print("Withdraw")

def Transfer():
    print("Transfer")

akar = ttk.Window(themename = "journal")
akar.title("Simulasi ATM Sederhana")
akar.resizable(width = False, height = False)

judul = ttk.Label(master = akar, text = "Simulasi ATM", font = ("DejaVu Math TeX Gyre", 24, "bold"))
judul.pack(padx = 10, pady = 10)

entry = ttk.Entry(master = akar)
entry.pack(padx = 10, pady = 10)

tombol_deposit = ttk.Button(master = akar, text = "Deposit", command = deposit)
tombol_deposit.pack(padx = 10, pady = 10)

tombol_withdraw = ttk.Button(master = akar, text = "Withdraw", command = Withdraw)
tombol_withdraw.pack(padx = 10, pady = 10)

tombol_transfer = ttk.Button(master = akar, text = "Transfer", command = Transfer)
tombol_transfer.pack(padx = 10, pady = 10)

akar.mainloop()
