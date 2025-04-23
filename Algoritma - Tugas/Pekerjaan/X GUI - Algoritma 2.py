import tkinter as tk
import ttkbootstrap as ttk

class BangunRuang:
    @staticmethod
    def kubus(s):
        luas = 6 * s ** 2
        volume = s ** 3
        return f"Luas Permukaan: {luas:,.2f} cm³, \nVolume: {volume:,.2f} cm³"

    @staticmethod
    def balok(p, l, t):
        luas = 2 * ((p * l) + (p * t) + (l * t))
        volume = p * l * t
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"
    
    @staticmethod
    def prisma(l_alas, k_alas, t_prisma):
        luas = 2 * l_alas + (k_alas * t_prisma)
        volume = l_alas * t_prisma
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"
    
    @staticmethod
    def limas(l_alas, l_selimut, t_limas):
        luas = l_alas + l_selimut
        volume = (1/3) * l_alas * t_limas
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"
    
    @staticmethod
    def tabung(jari, tinggi):
        PI = 3.141592653589793
        luas = 2 * PI * jari * (jari + tinggi)
        volume = PI * (jari ** 2) * tinggi
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"


class Graphical(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Bangun Ruang")
        self.resizable(width = False, height = False)
        self.style = ttk.Style(theme = "darkly")

        # Window Icon
        self_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Icon_Python.png")
        self.iconphoto(True, self_icon)


        # Notebook
        self.notebook = ttk.Notebook(master = self)


        # Kubus
        def kubus_func():
            try:
                result = BangunRuang.kubus(s = self.entry_kubus_int.get())
                self.result_kubus_str.set(result)
            except tk.TclError:
                self.result_kubus_str.set("Input Tidak Valid")
            pass
        self.tab_kubus = ttk.Frame(master = self.notebook)
        self.label_kubus = ttk.Label(master = self.tab_kubus, text = "Kubus")
        self.label_kubus.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        # Kubus Label Sisi
        self.kubus_sisi = ttk.Label(master = self.tab_kubus, text = "Sisi:")
        self.kubus_sisi.grid(row = 1, column = 0, padx = 5, pady = 10)
        # Kubus Entry
        self.entry_kubus_int = tk.IntVar(value = 0)
        self.entry_kubus = ttk.Entry(master = self.tab_kubus, textvariable = self.entry_kubus_int)
        self.entry_kubus.grid(row = 1, column = 1, padx = 10, pady = 10)
        # Kubus Button
        self.button_kubus = ttk.Button(master = self.tab_kubus, text = "Convert", command = kubus_func)
        self.button_kubus.grid(row = 1, column = 2, padx = 10, pady = 10)
        # Kubus Result
        self.result_kubus_str = tk.StringVar()
        self.result_kubus = ttk.Label(master = self.tab_kubus, text = "Result", textvariable = self.result_kubus_str)
        self.result_kubus.grid(row = 2, columnspan = 3, padx = 10, pady = 10)


        # Balok
        self.tab_balok = ttk.Frame(master = self.notebook)
        self.label_balok = ttk.Label(master = self.tab_balok, text = "Balok")
        self.label_balok.pack(padx = 10, pady = 10)

        # Prisma
        self.tab_prisma = ttk.Frame(master = self.notebook)
        self.label_prisma = ttk.Label(master = self.tab_prisma, text = "Prisma")
        self.label_prisma.pack(padx = 10, pady = 10)

        # Limas
        self.tab_limas = ttk.Frame(master = self.notebook)
        self.label_limas = ttk.Label(master = self.tab_limas, text = "Limas")
        self.label_limas.pack(padx = 10, pady = 10)

        # Tabung
        self.tab_tabung = ttk.Frame(master = self.notebook)
        self.label_tabung = ttk.Label(master = self.tab_tabung, text = "Tabung")
        self.label_tabung.pack(padx = 10, pady = 10)

        self.notebook.add(child = self.tab_kubus, text = "Kubus")
        self.notebook.add(child = self.tab_balok, text = "Balok")
        self.notebook.add(child = self.tab_prisma, text = "Prisma")
        self.notebook.add(child = self.tab_limas, text = "Limas")
        self.notebook.add(child = self.tab_tabung, text = "Tabung")
        self.notebook.pack(padx = 10, pady = 10)


if __name__ == "__main__":
    app = Graphical()
    app.mainloop()
