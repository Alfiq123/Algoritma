import tkinter as tk
from tkinter import ttk

class StudiC:

    def kubik(ukuran, air):
        harga_per_kubik = {
            "f": [(1, 50, 1000), (51, 100, 1500), (101, float("inf"), 2500)],
            "r": [(1, 50, 4000), (51, 100, 7000), (101, float("inf"), 10000)],
            "n": [(1, 50, 7500), (51, 100, 10000), (101, float("inf"), 13500)]
        }

        if ukuran in harga_per_kubik:
            for (batas_bawah, batas_atas, harga) in (harga_per_kubik[ukuran]):
                if batas_bawah <= air <= batas_atas:
                    return f"Rp. {harga * air:,.2f}"
                
class Graphical(tk.Tk):
    def __init__(self):
        super().__init__()


        # Instalasi Program.
        self.title("Perusahaan Air Minum")
        self.resizable(width = False, height = False)
        self.configure(background = "#003C43")


        # ! Icon window.
        # self_icon = tk.PhotoImage(file = "Python_Intermediate/Python Project/Icon_Python.png")
        # self.iconphoto(True, self_icon)


        # Fungsi perhitungan.
        def hitung():
            try:
                biaya_retribusi = StudiC.kubik(ukuran = self.combo_selected.get()[0].lower(), air = int(self.entry.get()))
                self.hasil_str.set(biaya_retribusi)

                if biaya_retribusi == None:
                    raise ValueError

            except ValueError:
                self.hasil_str.set("Input tidak valid")
            
        # Pembatas.
        self.frame = tk.LabelFrame(
            master = self, 
            text = "Pilih kode dan jumlah air yang digunakan", 
            background = "#003C43", 
            foreground = "#E3FEF7", 
            labelanchor = "n"
            )
        self.frame.grid(row = 0, column = 0, padx = 10, pady = 10)


        # Dropdown.
        self.style = ttk.Style(master = self)
        self.style.configure(
            "TCombobox", 
            foreground = "#E3FEF7", 
            background = "#003C43", 
            fieldbackground = "#003C43"
            )
        self.style.map(
            "TCombobox", 
            fieldbackground = [("readonly", "#003C43")], 
            selectbackground = [("readonly", "#E3FEF7")], 
            selectforeground = [("readonly", "#003C43")]
            )

        self.combo_selected = tk.StringVar(master = self, value = "Fasilitas Umum")
        self.combo = ttk.Combobox(
            master = self.frame, 
            values = ["Fasilitas Umum", "Rumah Biasa", "Niaga"], 
            textvariable = self.combo_selected, 
            state = "readonly", 
            style = "TCombobox", 
            )
        self.combo.grid(row = 0, column = 0, padx = 10, pady = 10)


        # Input.
        self.entry_int = tk.IntVar()
        self.entry = tk.Entry(
            master = self.frame, 
            background = "#003C43", 
            foreground = "#E3FEF7", 
            textvariable = self.entry_int, 
            )
        self.entry.grid(row = 0, column = 1, padx = 10, pady = 10)
            

        # Tombol.
        self.button = tk.Button(
            master = self.frame, 
            text = "Tampilkan Biaya", 
            background = "#003C43", 
            foreground = "#E3FEF7", 
            activebackground = "#77B0AA", 
            command = hitung
            )
        self.button.grid(row = 1, column = 0, padx = 10, pady = 10, columnspan = 2)


        # Hasil.
        self.hasil_str = tk.StringVar(master = self, value = "Rp. 0,00")
        self.hasil = tk.Label(
            master = self.frame, 
            text = "", 
            background = "#003C43", 
            foreground = "#E3FEF7", 
            textvariable = self.hasil_str, 
            anchor = "w"
            )
        self.hasil.grid(row = 2, column = 0, padx = 10, pady = 10, columnspan = 2)


if __name__ == "__main__":
    app = Graphical()
    app.mainloop()
