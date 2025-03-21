import tkinter as tk
import ttkbootstrap as ttk

class Prisma:
    def __init__(self, luas_alas, tinggi_prisma):
        self.luas_alas = luas_alas
        self.tinggi_prisma = tinggi_prisma

    def volume_prisma(self):
        volume = self.luas_alas * self.tinggi_prisma
        print(f"{volume:,.2f} cm³")
        return volume

class Tabung:
    def __init__(self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi

    def volume_tabung(self):
        PI = 3.141592653589793
        volume = PI * self.jari ** 2 * self.tinggi
        print(f"{volume:,.2f} cm³")
        return(volume)

# def catcher():
    # pilih = str(input("Masukkan Pilihan (1/2): "))
    # if pilih == "1":
        # la = int(input("Masukkan Luas Alas: "))
        # ta = int(input("Masukkan Tinggi Prisma: "))
        # prisma = Prisma(luas_alas = la, tinggi_prisma = ta)
        # prisma.volume_prisma()

    # elif pilih == "2":
        # r = int(input("Masukkan Jari-Jari: "))
        # t = int(input("Masukkan TInggi: "))
        # tabung = Tabung(jari = r, tinggi = t)
        # tabung.volume_tabung()

    # else:
        # catcher()

# catcher()

class Gui:
    def __init__(self):
        pass

    def main_menu():
        root = ttk.Window(themename = "darkly", title = "Regen", resizable = (False, False))

        label = ttk.Label(master = root, text = "Bangun Ruang", font = ("Times New Roman", 24, "bold"))
        label.pack(padx = 10, pady = 10)

        entry = ttk.Entry(master = root)
        entry.pack(padx = 10, pady = 10)

        button = ttk.Button(master = root, text = "Hitung")
        button.pack(padx = 10, pady = 10)

        root.mainloop()

Gui.main_menu()