import tkinter as tk
import ttkbootstrap as ttk

class Prisma:
    def __init__(self, luas_alas, tinggi_prisma):
        self.luas_alas = luas_alas
        self.tinggi_prisma = tinggi_prisma

    def volume(self):
        return self.luas_alas * self.tinggi_prisma

class Tabung:
    def __init__(self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi

    def volume(self):
        PI = 3.141592653589793
        return PI * self.jari ** 2 * self.tinggi

class Gui:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")
        self.root.title("Bangun Ruang")
        self.root.resizable(False, False)

        # Label Judul
        ttk.Label(self.root, text="Bangun Ruang", font=("Times New Roman", 24, "bold")).pack(pady=10)

        # Dropdown Menu
        self.selected_shape = tk.StringVar(value="Prisma")
        self.shape_menu = ttk.Combobox(self.root, textvariable=self.selected_shape, values=["Prisma", "Tabung"])
        self.shape_menu.pack(pady=5)
        self.shape_menu.bind("<<ComboboxSelected>>", self.update_form)

        # Frame untuk input
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(pady=10)
        self.create_prisma_inputs()

        # Tombol Hitung
        self.calculate_button = ttk.Button(self.root, text="Hitung", command=self.calculate_volume)
        self.calculate_button.pack(pady=10)

        # Label Hasil
        self.result_label = ttk.Label(self.root, text="Volume: - cm³", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

        self.root.mainloop()

    def create_prisma_inputs(self):
        """Buat input untuk Prisma"""
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.input_frame, text="Luas Alas (cm²):").grid(row=0, column=0, padx=5, pady=5)
        self.luas_alas_entry = ttk.Entry(self.input_frame)
        self.luas_alas_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Tinggi Prisma (cm):").grid(row=1, column=0, padx=5, pady=5)
        self.tinggi_prisma_entry = ttk.Entry(self.input_frame)
        self.tinggi_prisma_entry.grid(row=1, column=1, padx=5, pady=5)

    def create_tabung_inputs(self):
        """Buat input untuk Tabung"""
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.input_frame, text="Jari-jari (cm):").grid(row=0, column=0, padx=5, pady=5)
        self.jari_entry = ttk.Entry(self.input_frame)
        self.jari_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Tinggi (cm):").grid(row=1, column=0, padx=5, pady=5)
        self.tinggi_entry = ttk.Entry(self.input_frame)
        self.tinggi_entry.grid(row=1, column=1, padx=5, pady=5)

    def update_form(self, event=None):
        """Update tampilan input sesuai dengan pilihan dropdown"""
        shape = self.selected_shape.get()
        if shape == "Prisma":
            self.create_prisma_inputs()
        else:
            self.create_tabung_inputs()

    def calculate_volume(self):
        """Menghitung volume berdasarkan input pengguna"""
        shape = self.selected_shape.get()
        try:
            if shape == "Prisma":
                luas_alas = float(self.luas_alas_entry.get())
                tinggi_prisma = float(self.tinggi_prisma_entry.get())
                prisma = Prisma(luas_alas, tinggi_prisma)
                volume = prisma.volume()
            else:
                jari = float(self.jari_entry.get())
                tinggi = float(self.tinggi_entry.get())
                tabung = Tabung(jari, tinggi)
                volume = tabung.volume()

            self.result_label.config(text=f"Volume: {volume:,.2f} cm³")
        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid!")

Gui()
