import tkinter as tk
from tkinter import ttk, messagebox

class RentalGedungApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Rental Gedung")
        self.root.geometry("500x600")
        
        # Perbaikan 1: Menyimpan display text terpisah
        self.kategori_options = {
            "1": {"display": "Gedung Pertemuan (Rapat)", "harga": 300000, "lebih": 50000},
            "2": {"display": "Gedung Pentas Seni", "harga": 450000, "lebih": 80000},
            "3": {"display": "Gedung Pernikahan", "harga": 600000, "lebih": 100000}
        }
        
        self.setup_ui()

    def setup_ui(self):
        # Frame Input
        input_frame = ttk.LabelFrame(self.root, text="Data Penyewaan")
        input_frame.pack(padx=10, pady=10, fill="x")
        
        # Nama Penyewa
        ttk.Label(input_frame, text="Nama Penyewa:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.nama_entry = ttk.Entry(input_frame)
        self.nama_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
        
        # Kategori Gedung
        ttk.Label(input_frame, text="Kategori Gedung:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.kategori_combo = ttk.Combobox(input_frame, values=list(self.kategori_options.values()))
        self.kategori_combo.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        
        # Lama Sewa
        ttk.Label(input_frame, text="Lama Sewa (hari):").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.lama_sewa_entry = ttk.Entry(input_frame)
        self.lama_sewa_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        
        # Kelebihan Jam
        ttk.Label(input_frame, text="Kelebihan Jam:").grid(row=3, column=0, sticky="w", padx=5, pady=2)
        self.kelebihan_jam_entry = ttk.Entry(input_frame)
        self.kelebihan_jam_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=2)
        
        # Tombol
        button_frame = ttk.Frame(self.root)
        button_frame.pack(padx=10, pady=10, fill="x")
        
        ttk.Button(button_frame, text="Hitung", command=self.hitung_biaya).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_form).pack(side="left", padx=5)
        
        # Hasil
        result_frame = ttk.LabelFrame(self.root, text="Hasil Perhitungan")
        result_frame.pack(padx=10, pady=10, fill="x")
        
        self.result_labels = {}
        labels = [
            ("Harga Sewa", "harga_sewa"),
            ("Biaya Kelebihan Jam", "biaya_jam"),
            ("Potongan", "potongan"),
            ("Total Biaya", "total_biaya")
        ]
        
        for i, (text, key) in enumerate(labels):
            ttk.Label(result_frame, text=text + ":").grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.result_labels[key] = ttk.Label(result_frame, text="Rp.0")
            self.result_labels[key].grid(row=i, column=1, sticky="e", padx=5, pady=2)
    
        # Perbaikan 2: Mengambil display text untuk combobox
        display_values = [v["display"] for v in self.kategori_options.values()]
        self.kategori_combo = ttk.Combobox(input_frame, values=display_values)
        self.kategori_combo.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

    # Perbaikan 3: Fungsi pencarian kategori yang diperbaiki
    def get_kategori_data(self, display_text):
        for key, value in self.kategori_options.items():
            if value["display"] == display_text:
                return value
        return None
    
    def hitung_biaya(self):
        try:
            # Ambil data input
            nama = self.nama_entry.get()
            if not nama:
                raise ValueError("Nama penyewa harus diisi")
            
            kategori = self.kategori_combo.get()
            if not kategori:
                raise ValueError("Kategori gedung harus dipilih")
            
            kategori_data = self.get_kategori_data(kategori)
            if not kategori_data:
                raise ValueError("Kategori tidak valid")
            
            lama_sewa = int(self.lama_sewa_entry.get())
            kelebihan_jam = int(self.kelebihan_jam_entry.get())

            # Perbaikan 4: Mengambil data kategori yang benar
            kategori = self.kategori_combo.get()
            kategori_data = self.get_kategori_data(kategori)
            
            if not kategori_data:
                raise ValueError("Kategori tidak valid")

            # Perbaikan 5: Mengakses data dengan key yang benar
            sewa_per_hari = kategori_data["harga"]
            sewa_lebih_lama = kategori_data["lebih"]
            
            # Perhitungan
            sewa_per_hari = kategori_data[1]
            sewa_lebih_lama = kategori_data[2]
            
            total_sewa = sewa_per_hari * lama_sewa
            biaya_jam = sewa_lebih_lama * kelebihan_jam
            potongan = 0.1 * total_sewa if lama_sewa > 3 else 0
            total_biaya = total_sewa + biaya_jam - potongan
            
            # Update hasil
            self.result_labels['harga_sewa'].config(text=f"Rp.{total_sewa:,.0f}")
            self.result_labels['biaya_jam'].config(text=f"Rp.{biaya_jam:,.0f}")
            self.result_labels['potongan'].config(text=f"Rp.{potongan:,.0f}")
            self.result_labels['total_biaya'].config(text=f"Rp.{total_biaya:,.0f}")
            
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
    
    def reset_form(self):
        self.nama_entry.delete(0, tk.END)
        self.kategori_combo.set('')
        self.lama_sewa_entry.delete(0, tk.END)
        self.kelebihan_jam_entry.delete(0, tk.END)
        for label in self.result_labels.values():
            label.config(text="Rp.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalGedungApp(root)
    root.mainloop()