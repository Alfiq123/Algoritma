import tkinter as tk
from tkinter import ttk

class StudiD:

    @staticmethod
    def lahan(kategori, sewa):
        if (kategori == "a"):
            return f"Rp. {5000 + (3000 * (sewa - 1)):,.2f}"
        elif (kategori == "b"):
            return f"Rp. {7000 + (3500 * (sewa - 1)):,.2f}"
        else:
            return f"Rp. {6000 + (2500 * (sewa - 1)):,.2f}"
        
class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        # Judul.
        self.title("Persewaan Lahan Parkir")
        self.resizable(width = False, height = False)
        self.configure(background = "#201E43")

        # Icon window.
        self_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Icon_Python.png")
        self.iconphoto(True, self_icon)

        # Fungsi untuk menampilkan hasil.
        def show_result():
            try:
                harga_sewa = StudiD.lahan(kategori = self.kategori_var.get(), sewa = self.entry_var.get())

                if self.entry_var.get() < 0:
                    raise ValueError
                
                self.hasil_label_var.set(harga_sewa)

            except (ValueError, tk.TclError):
                self.hasil_label_var.set("Inputan harus angka positif!")

        # Garis pembatas.
        frame = tk.LabelFrame(
            master = self, 
            text = "Persewaan Lahan Parkir", 
            labelanchor="n", 
            font = ("Arial", 15, "bold"), 
            background = "#201E43",
            foreground = "#508C9B",
            padx = 10, 
            pady = 10
            )
        frame.configure(background = "#201E43")
        frame.pack(pady=10, fill="x", padx=10)

        # Pilihan gudang dalam bentuk radio.
        gudang_list = [("(A) Kategori Sedan", "a"), ("(B) Kategori Minibus", "b"), ("(C) Kategori Truk", "c")]
        
        self.kategori_var = tk.StringVar(value = "a")

        for nama, kategori in gudang_list:
            tk.Radiobutton(
                master = frame, 
                text = nama, 
                font = ("Arial", 12),
                value = kategori, 
                variable = self.kategori_var, 
                background = "#201E43",
                foreground = "#508C9B", 
                activebackground = "#508C9B", 
                activeforeground = "#201E43", 
                width = 18, 
                anchor = "w"
                ).pack(padx=10, pady=1, anchor = "w")
            
        # Input.
        self.entry_var = tk.IntVar(value = 10)
        entry = tk.Entry(
            master = frame, 
            font = ("Arial", 12), 
            textvariable = self.entry_var, 
            background = "#201E43", 
            foreground = "#508C9B", 
            width = 25
            )
        entry.pack(padx=10, pady=10, side = "left")

        # Tombol Hitung.
        button = tk.Button(
            master = frame, 
            text = "Hitung Sewa", 
            font = ("Arial", 12), 
            background = "#201E43", 
            foreground = "#508C9B", 
            activeforeground = "#508C9B", 
            activebackground = "#201E43", 
            command = show_result
            )
        button.pack(padx = 10, pady = 10, side = "left")

        # Menampilkan Hasil.
        self.hasil_label_var = tk.StringVar()
        hasil_label = tk.Label(
            master = self, 
            text = "Output", 
            textvariable = self.hasil_label_var , 
            font = ("Arial", 12), 
            background = "#201E43", 
            foreground = "#508C9B",
            )
        hasil_label.pack(pady = 10)

if __name__ == "__main__":
    app = Gui()
    app.mainloop()
