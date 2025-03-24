import tkinter as tk
from tkinter import ttk, messagebox


class StudiD:
    @staticmethod
    def lahan(kategori, sewa):
        if kategori == "a" and sewa > 0:
            return f"Biaya Sewa: Rp. {5000 + (3000 * (sewa - 1)):,.2f}"
        elif kategori == "b" and sewa > 0:
            return f"Biaya Sewa: Rp. {7000 + (3500 * (sewa - 1)):,.2f}"
        elif kategori == "c" and sewa > 0:
            return f"Biaya Sewa: Rp. {6000 + (2500 * (sewa - 1)):,.2f}"
        else:
            return "Error: Bilangan tidak boleh negatif!"


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Persewaan Lahan Parkir")
        self.root.geometry("400x350")
        self.root.configure(bg="#f4f4f4")
        self.root.resizable(False, False)

        # Frame utama dengan border
        self.frame = tk.Frame(root, bd=3, relief="ridge", bg="white", padx=20, pady=20)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Judul
        self.label_title = tk.Label(
            self.frame, text="Persewaan Lahan Parkir", font=("Arial", 14, "bold"), bg="white"
        )
        self.label_title.pack(pady=5)

        # Dropdown kategori lahan
        self.label_kategori = tk.Label(self.frame, text="Kategori Lahan:", font=("Arial", 11), bg="white")
        self.label_kategori.pack(anchor="w")

        self.kategori_var = tk.StringVar()
        self.combobox_kategori = ttk.Combobox(
            self.frame, textvariable=self.kategori_var, state="readonly", font=("Arial", 11)
        )
        self.combobox_kategori["values"] = ("a", "b", "c")
        self.combobox_kategori.pack(fill="x", padx=5, pady=2)

        # Input lama sewa
        self.label_sewa = tk.Label(self.frame, text="Lama Sewa (Hari):", font=("Arial", 11), bg="white")
        self.label_sewa.pack(anchor="w")

        self.entry_sewa = tk.Entry(self.frame, font=("Arial", 11))
        self.entry_sewa.pack(fill="x", padx=5, pady=2)

        # Label untuk pesan error
        self.error_label = tk.Label(self.frame, text="", font=("Arial", 10), fg="red", bg="white")
        self.error_label.pack()

        # Tombol Hitung Biaya
        self.button_hitung = tk.Button(
            self.frame, text="Hitung Biaya", command=self.hitung_biaya, font=("Arial", 11, "bold"),
            bg="#007BFF", fg="white", padx=10, pady=5
        )
        self.button_hitung.pack(pady=10)

        # Label hasil
        self.result_label = tk.Label(self.frame, text="", font=("Arial", 12, "bold"), fg="green", bg="white")
        self.result_label.pack()

    def hitung_biaya(self):
        kategori = self.kategori_var.get()
        sewa_text = self.entry_sewa.get()

        # Validasi input kategori
        if kategori not in ("a", "b", "c"):
            self.error_label.config(text="Kategori tidak valid!")
            self.result_label.config(text="")
            return

        # Validasi input lama sewa
        try:
            sewa = int(sewa_text)
            if sewa <= 0:
                raise ValueError
        except ValueError:
            self.error_label.config(text="Lama sewa harus angka positif!")
            self.result_label.config(text="")
            return

        # Hapus pesan error jika valid
        self.error_label.config(text="")

        # Hitung biaya dan tampilkan
        hasil = StudiD.lahan(kategori, sewa)
        self.result_label.config(text=hasil)


# Menjalankan GUI
root = tk.Tk()
app = GUI(root)
root.mainloop()
