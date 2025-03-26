import tkinter as tk

class StudiA:

    @staticmethod
    def megabyte(kode, mb):
        harga_per_mb = {
            "r": [(1, 50, 2000), (51, 80, 4500), (81, float("inf"), 6500)],
            "c": [(1, 50, 5000), (51, 80, 7000), (81, float("inf"), 10000)],
            "v": [(1, 50, 7500), (51, 80, 10000), (81, float("inf"), 15000)]
        }

        if kode in harga_per_mb:
            for (batas_bawah, batas_atas, harga) in (harga_per_mb[kode]):
                if batas_bawah <= mb <= batas_atas:
                    return f"Rp. {harga * mb:,.2f}"

class StudioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Studio A Calculator")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame untuk pilihan kode
        code_frame = tk.LabelFrame(self, text="Pilihan Kode", padx=10, pady=10, labelanchor="n")
        code_frame.pack(pady=10, fill="x", padx=10)
        
        self.code_var = tk.StringVar(value="r")
        
        codes = [
            ("Paket Regular (r)", "r"),
            ("Paket Spesial (c)", "c"),
            ("Paket VIP (v)", "v")
        ]
        
        for text, value in codes:
            tk.Radiobutton(
                code_frame,
                text=text,
                variable=self.code_var,
                value=value
            ).pack(anchor="w")
        
        # Frame untuk input MB
        mb_frame = tk.LabelFrame(self, text="Jumlah MB", padx=10, pady=10, labelanchor="n")
        mb_frame.pack(pady=10, fill="x", padx=10)
        
        self.mb_entry = tk.Entry(mb_frame)
        self.mb_entry.pack()
        
        # Tombol hitung
        tk.Button(self, text="Hitung", command=self.calculate).pack(pady=5)
        
        # Label hasil
        self.result_label = tk.Label(self, text="", fg="blue")
        self.result_label.pack(pady=10)
        
    def calculate(self):
        kode = self.code_var.get()
        mb = self.mb_entry.get()
        
        try:
            mb = int(mb)
            if mb <= 0:
                raise ValueError

        except ValueError:
            self.result_label.config(text="Error: Jumlah MB harus angka positif!", fg="red")
            return
        
        result = StudiA.megabyte(kode, mb)
        self.result_label.config(text=result, fg="blue")

if __name__ == "__main__":
    app = StudioApp()
    app.mainloop()
