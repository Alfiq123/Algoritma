import tkinter as tk

class StudiA:
    @staticmethod
    def megabyte(kode, mb):
        if kode == "r":
            if 1 <= mb <= 50:
                return f"Rp. {2000 * mb:,.0f}"
            elif 51 <= mb <= 80:
                return f"Rp. {4500 * mb:,.0f}"
            elif mb > 80:
                return f"Rp. {6500 * mb:,.0f}"
            else:
                return "Error: Input tidak valid"
            
        elif kode == "c":
            if 1 <= mb <= 50:
                return f"Rp. {5000 * mb:,.0f}"
            elif 51 <= mb <= 80:
                return f"Rp. {7000 * mb:,.0f}"
            elif mb > 80:
                return f"Rp. {10000 * mb:,.0f}"
            else:
                return "Error: Input tidak valid"

        elif kode == "v":
            if 1 <= mb <= 50:
                return f"Rp. {7500 * mb:,.0f}"
            elif 51 <= mb <= 80:
                return f"Rp. {10000 * mb:,.0f}"
            elif mb > 80:
                return f"Rp. {15000 * mb:,.0f}"
            else:
                return "Error: Input tidak valid"

class StudioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Studio A Calculator")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame untuk pilihan kode
        code_frame = tk.LabelFrame(self, text="Pilihan Kode", padx=10, pady=10)
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
        mb_frame = tk.LabelFrame(self, text="Jumlah MB", padx=10, pady=10)
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
            self.result_label.config(text="Error: Input MB tidak valid", fg="red")
            return
        
        result = StudiA.megabyte(kode, mb)
        self.result_label.config(text=result, fg="blue")

if __name__ == "__main__":
    app = StudioApp()
    app.mainloop()
