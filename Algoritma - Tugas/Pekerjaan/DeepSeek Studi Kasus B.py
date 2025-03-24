import tkinter as tk
from tkinter import ttk, messagebox

class StudiB:
    @staticmethod
    def gedung(kategori, sewa):
        if kategori == "a":
            building = "Gedung A"
            cost = 7000000 + (6500000 * (sewa - 1))
        elif kategori == "b":
            building = "Gedung B"
            cost = 8000000 + (7000000 * (sewa - 1))
        else:
            building = "Gedung C"
            cost = 7500000 + (6000000 * (sewa - 1))
        return building, f"Biaya Sewa: Rp. {cost:,.2f}"

class WarehouseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Komplek Pergudangan StudiB")
        self.root.geometry("400x400")
        self.root.resizable(width=False, height=False)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill='both', expand=True)
        
        # Header
        header = ttk.Label(
            main_frame, 
            text="Komplek Pergudangan",
            font=('Helvetica', 14, 'bold')
        )
        header.pack(pady=10)
        
        # Category Selection
        category_frame = ttk.LabelFrame(main_frame, text="Pilih Kategori Gedung")
        category_frame.pack(fill='x', pady=10)
        
        self.kategori_var = tk.StringVar(value='a')
        
        ttk.Radiobutton(
            category_frame,
            text="Gedung A - Rp.6.5jt/bulan setelah bulan pertama",
            variable=self.kategori_var,
            value='a'
        ).pack(anchor='w', padx=5, pady=2)
        
        ttk.Radiobutton(
            category_frame,
            text="Gedung B - Rp.7jt/bulan setelah bulan pertama",
            variable=self.kategori_var,
            value='b'
        ).pack(anchor='w', padx=5, pady=2)
        
        ttk.Radiobutton(
            category_frame,
            text="Gedung C - Rp.6jt/bulan setelah bulan pertama",
            variable=self.kategori_var,
            value='c'
        ).pack(anchor='w', padx=5, pady=2)
        
        # Sewa Input
        sewa_frame = ttk.Frame(main_frame)
        sewa_frame.pack(fill='x', pady=10)
        
        ttk.Label(sewa_frame, text="Lama Sewa (bulan):").pack(side='left', padx=5)
        self.sewa_entry = ttk.Entry(sewa_frame)
        self.sewa_entry.pack(side='right', expand=True, fill='x')
        
        # Button
        ttk.Button(
            main_frame,
            text="Hitung Biaya Sewa",
            command=self.calculate
        ).pack(pady=10)
        
        # Result Display
        self.result_frame = ttk.LabelFrame(main_frame, text="Detail Biaya")
        self.result_frame.pack(fill='both', expand=True)
        
        self.building_label = ttk.Label(self.result_frame, font=('Helvetica', 10))
        self.building_label.pack(pady=5)
        
        self.cost_label = ttk.Label(
            self.result_frame, 
            font=('Helvetica', 12, 'bold'),
            foreground='green'
        )
        self.cost_label.pack(pady=5)
        
    def calculate(self):
        try:
            sewa = int(self.sewa_entry.get())
            if sewa < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Input lama sewa harus bilangan bulat positif!")
            return
            
        kategori = self.kategori_var.get()
        building, biaya = StudiB.gedung(kategori, sewa)
        
        self.building_label.config(text=f"「 {building} 」")
        self.cost_label.config(text=biaya)

if __name__ == "__main__":
    root = tk.Tk()
    app = WarehouseApp(root)
    root.mainloop()