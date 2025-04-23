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

class Graphics(tk.Tk):
    def __init__(self):
        super().__init__()

        # Judul.
        self.title("Hotspot Modi App")
        self.resizable(width = False, height = False)
        self.configure(background = "#18230F")

        # ! Window Icon
        # self_icon = tk.PhotoImage(file="Python_Intermediate/Python Project/Icon_Python.png")
        # self.iconphoto(True, self_icon)

        # Tombol Hitung Command.
        def button_command():
            try:
                if len(str(entry_int.get())) > 13:
                    hasil_label_var.set("Tidak boleh lebih dari 13 digit!")
                    return None

                harga_sewa = StudiA.megabyte(kode = kode_str.get(), mb = entry_int.get())

                if harga_sewa == None:
                    raise ValueError
                
                hasil_label_var.set(harga_sewa)
                
            except:
                hasil_label_var.set("Inputan harus angka positif!")

        # Frame (Garis).
        frame = tk.LabelFrame(
            master = self, 
            text = "Pilihan Paket", 
            labelanchor="n", 
            font = ("Comic Sans MS", 12), 
            background = "#18230F",
            foreground = "#1F7D53",
            padx = 10, 
            pady = 10
        )
        frame.configure(background = "#18230F")
        frame.pack(pady=10, fill="x", padx=10)

        # Tombol Radio.
        radio_list = [("Paket Regular (r)", "r"), ("Paket Spesial (c)", "c"), ("Paket VIP (v)", "v")]
        
        kode_str = tk.StringVar(value="r")

        for nama, kode in radio_list:
            tk.Radiobutton(
                master = frame, 
                text = nama, 
                font = ("Comic Sans MS", 12), 
                variable = kode_str, 
                value = kode, 
                background = "#18230F", 
                foreground = "#1F7D53", 
                activeforeground = "#1F7D53", 
                activebackground = "#27391C", 
                width = 15, 
                anchor = "w"
            ).pack()
            
        # Frame (Garis).
        frame2 = tk.LabelFrame(
            master = self, 
            text = "Masukkan Jumlah MB", 
            labelanchor="n", 
            font = ("Comic Sans MS", 12), 
            background = "#18230F",
            foreground = "#1F7D53", 
            padx = 10, 
            pady = 10
        )
        frame2.configure(background = "#18230F")
        frame2.pack(padx=10, fill="x", pady=10)
    
        # Entry (Input).
        entry_int = tk.IntVar()
        entry = tk.Entry(
            master = frame2, 
            font = ("Comic Sans MS", 12), 
            textvariable = entry_int, 
            background = "#27391C", 
            foreground = "#1F7D53"
        )
        entry.pack()

        # Tombol Hitung.
        button = tk.Button(
            master = frame2, 
            text = "Hitung Sewa", 
            font = ("Comic Sans MS", 12), 
            background = "#27391C", 
            foreground = "#1F7D53", 
            activeforeground = "#1F7D53", 
            activebackground = "#27391C", 
            command = button_command
        )
        button.pack(padx = 10, pady = 10)

        # Text Hasil.
        hasil_label_var = tk.StringVar()
        hasil_label = tk.Label(
            master = self, 
            text = "Output", 
            textvariable = hasil_label_var, 
            font = ("Comic Sans MS", 12), 
            background = "#18230F", 
            foreground = "#1F7D53",
        )
        hasil_label.pack()

if __name__ == "__main__":
    app = Graphics()
    app.mainloop()
