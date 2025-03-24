import tkinter as tk
from tkinter import messagebox

class AirBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PT Air Minum")
        self.root.geometry("256x256")
        self.root.resizable(width=False, height=False)

        # Label Judul
        tk.Label(root, text="Hitung Biaya Air", font=("Arial", 14, "bold")).pack(pady=10)

        # Dropdown Ukuran
        tk.Label(root, text="Pilih Ukuran (F/R/N):").pack()
        self.ukuran_var = tk.StringVar()
        self.ukuran_var.set("f")  # Default value
        self.ukuran_menu = tk.OptionMenu(root, self.ukuran_var, "f", "r", "n")
        self.ukuran_menu.pack()

        # Input Jumlah Air
        tk.Label(root, text="Masukkan Jumlah Air:").pack()
        self.air_entry = tk.Entry(root)
        self.air_entry.pack()

        # Tombol Hitung
        self.calculate_button = tk.Button(root, text="Hitung", command=self.calculate)
        self.calculate_button.pack(pady=10)

        # Label Hasil
        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack()

    def calculate(self):
        ukuran = self.ukuran_var.get()
        try:
            air = int(self.air_entry.get())
            if air < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid, masukkan angka positif.")
            return

        biaya = self.hitung_biaya(ukuran, air)
        self.result_label.config(text=f"Total Biaya: {biaya}")

    def hitung_biaya(self, ukuran, air):
        if ukuran == "f":
            if air <= 50:
                return f"Rp. {1000 * air:,.0f}"
            elif air <= 100:
                return f"Rp. {1500 * air:,.0f}"
            else:
                return f"Rp. {2500 * air:,.0f}"
        elif ukuran == "r":
            if air <= 50:
                return f"Rp. {4000 * air:,.0f}"
            elif air <= 100:
                return f"Rp. {7000 * air:,.0f}"
            else:
                return f"Rp. {10000 * air:,.0f}"
        elif ukuran == "n":
            if air <= 50:
                return f"Rp. {7500 * air:,.0f}"
            elif air <= 100:
                return f"Rp. {10000 * air:,.0f}"
            else:
                return f"Rp. {13500 * air:,.0f}"

if __name__ == "__main__":
    root = tk.Tk()
    app = AirBillingApp(root)
    root.mainloop()
