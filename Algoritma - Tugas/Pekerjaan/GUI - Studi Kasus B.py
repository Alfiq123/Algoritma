import tkinter as tk

class StudiB:

    @staticmethod
    def gedung(kategori, sewa):
        if kategori == "a":
            return f"Rp. {7000000 + (6500000 * (sewa - 1)):,.2f}"
        elif kategori == "b":
            return f"Rp. {8000000 + (7000000 * (sewa - 1)):,.2f}"
        elif kategori == "c":
            return f"Rp. {7500000 + (6000000 * (sewa - 1)):,.2f}"
        else:
            return None

class Graphic(tk.Tk):
    def __init__(self):
        super().__init__()

        # Judul.
        self.title("Persewaan Gudang")
        self.resizable(width = False, height = False)
        self.configure(background = "#F8F4E1")

        # ! Icon window.
        # self_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Icon_Python.png")
        # self.iconphoto(True, self_icon)

        # Fungsi untuk menampilkan hasil.
        def show_result():
            try:
                harga_sewa = StudiB.gedung(kategori = self.kategori_var.get(), sewa = self.entry_var.get())
                
                if len(str(self.entry_var.get())) > 13:
                    self.hasil_label_var.set("Tidak boleh lebih dari 13 digit!")
                    return None

                elif self.entry_var.get() <= 0:
                    raise ValueError
                
                self.hasil_label_var.set(harga_sewa)

            except (ValueError, tk.TclError):
                self.hasil_label_var.set("Inputan harus angka positif!")

        # Garis pembatas.
        frame = tk.LabelFrame(
            master = self, 
            text = " Pilihan Gedung ", 
            labelanchor="n", 
            font = ("Arial", 15, "bold"), 
            background = "#F8F4E1",
            foreground = "#74512D",
            padx = 10, 
            pady = 10
        )
        frame.configure(background = "#F8F4E1")
        frame.pack(pady=10, fill="x", padx=10)

        # Pilihan gudang dalam bentuk radio.
        gudang_list = [("(A) Barang Elektronik", "a"), ("(B) Bahan Bangunan", "b"), ("(C) Barang Mebeler", "c")]
        
        self.kategori_var = tk.StringVar(value = "a")

        for nama, kategori in gudang_list:
            tk.Radiobutton(
                master = frame, 
                text = nama, 
                font = ("Arial", 12),
                value = kategori, 
                variable = self.kategori_var, 
                background = "#F8F4E1",
                foreground = "#74512D", 
                activebackground = "#74512D", 
                activeforeground = "#F8F4E1", 
                width = 18, 
                anchor = "w"
            ).pack(padx=10, pady=1, anchor = "w")
            
        # Input.
        self.entry_var = tk.IntVar(value = 10)
        entry = tk.Entry(
            master = frame, 
            font = ("Arial", 12), 
            textvariable = self.entry_var, 
            background = "#F8F4E1", 
            foreground = "#74512D", 
            width = 25
        )
        entry.pack(padx=10, pady=10, side = "left")

        # Tombol Hitung.
        button = tk.Button(
            master = frame, 
            text = "Hitung Sewa", 
            font = ("Arial", 12), 
            background = "#F8F4E1", 
            foreground = "#74512D", 
            activeforeground = "#74512D", 
            activebackground = "#F8F4E1", 
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
            background = "#F8F4E1", 
            foreground = "#74512D",
        )
        hasil_label.pack(pady = 10)

if __name__ == "__main__":
    app = Graphic()
    app.mainloop()
