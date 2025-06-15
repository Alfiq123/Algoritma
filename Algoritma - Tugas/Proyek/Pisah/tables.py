import customtkinter as ctk


class TabelJudul:
    def __init__(self, parent):
        self.parent = parent

        self.frame = ctk.CTkFrame(master=parent)
        self.frame.grid(row=3, column=0, padx=10, pady=10)

        self.label_nama = ctk.CTkLabel(
            master=self.frame,
            text="Nama",
            font=("Helvetica", 14, "bold"),
            width=100
        )
        self.label_nama.grid(row=0, column=0, padx=10, pady=10)

        self.label_jumlah = ctk.CTkLabel(
            master=self.frame,
            text="Kuantitas",
            font=("Helvetica", 14, "bold"),
            width=100
        )
        self.label_jumlah.grid(row=0, column=1, padx=10, pady=10)

        self.label_status = ctk.CTkLabel(
            master=self.frame,
            text="Status",
            font=("Helvetica", 14, "bold"),
            width=100
        )
        self.label_status.grid(row=0, column=2, padx=10, pady=10)

        self.label_aksi = ctk.CTkLabel(
            master=self.frame,
            text="Aksi",
            font=("Helvetica", 14, "bold"),
            width=100
        )
        self.label_aksi.grid(row=0, column=3, padx=10, pady=10)


class TabelKolom:
    def __init__(self, parent):
        self.parent = parent

        self.inventori = [
            {"Nama": "Linggis", "Kuantitas": 100, "Status": "Tersedia"},
            {"Nama": "Obeng", "Kuantitas": 50, "Status": "Sedikit"},
            {"Nama": "Sekop", "Kuantitas": 14, "Status": "Beberapa"}
        ]

        self.frame = ctk.CTkScrollableFrame(
            master=parent,
            width=480,
            height=200,
            fg_color="transparent"
        )
        self.frame.grid(row=4, column=0, padx=10, pady=10)

        self.tampilkan_data()

    def tampilkan_data(self):
        # Bersihkan frame dulu
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Tampilkan ulang semua item
        for index_baris, item in enumerate(self.inventori, start=1):
            ctk.CTkLabel(
                master=self.frame,
                text=item["Nama"],
                font=("Helvetica", 14),
                width=100
            ).grid(row=index_baris, column=0, padx=10, pady=10)

            ctk.CTkLabel(
                master=self.frame,
                text=item["Kuantitas"],
                font=("Helvetica", 14),
                width=100
            ).grid(row=index_baris, column=1, padx=10, pady=10)

            ctk.CTkLabel(
                master=self.frame,
                text=item["Status"],
                font=("Helvetica", 14),
                width=100
            ).grid(row=index_baris, column=2, padx=10, pady=10)

            ctk.CTkButton(
                master=self.frame,
                text="Hapus",
                font=("Helvetica", 14),
                width=100,
                command=lambda idx=index_baris - 1: self.hapus_item(idx)
            ).grid(row=index_baris, column=3, padx=10, pady=10)

    def hapus_item(self, index):
        if 0 <= index < len(self.inventori):
            del self.inventori[index]
            self.tampilkan_data()
