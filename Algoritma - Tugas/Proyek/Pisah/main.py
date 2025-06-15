import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Makalah")
        self.geometry("1000x600")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=2)

        self.title = ctk.CTkLabel(
            master=self,
            text="Manajemen Inventaris",
            font=("Helvetica", 24, "bold")
        )
        self.title.grid(row=0, column=0, padx=10, pady=10)

        self.init_button = Widgets(self)
        self.init_tabel_judul = TabelJudul(self)
        self.init_tabel_kolom = TabelKolom(self)


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


class Widgets:
    def __init__(self, parent):
        self.parent = parent
        self.tabel = TabelKolom(parent)

        self.frame = ctk.CTkFrame(master=parent)
        self.frame.grid(row=1, column=0, padx=10, pady=(10, 0))

        self.tambah = ctk.CTkButton(
            master=self.frame,
            text="Tambah Barang",
            font=("Helvetica", 14),
            command=self.tambah_show
        )
        self.tambah.grid(row=0, column=0, padx=10, pady=10)

        # ════════════════════════════════════════════════════════════ #
        # ════════════════════ Tombol Tersembunyi ════════════════════ #

        self.frame_2 = ctk.CTkFrame(master=parent)
        # self.frame_2.grid(row=2, column=0, padx=10, pady=10)

        self.entry_item_name = ctk.CTkEntry(
            master=self.frame_2,
            placeholder_text="Nama Barang",
            font=("Helvetica", 14)
        )
        # self.entry_item_name.grid(row=0, column=1, padx=10, pady=10)
        # self.entry_item_name.grid_forget()

        self.entry_quantity = ctk.CTkEntry(
            master=self.frame_2,
            placeholder_text="Jumlah Barang",
            font=("Helvetica", 14)
        )
        # self.entry_quantity.grid(row=0, column=2, padx=10, pady=10)
        # self.entry_quantity.grid_forget()

        self.tambah_barang = ctk.CTkButton(
            master=self.frame_2,
            text="Tambah",
            font=("Helvetica", 14),
            command=self.tambah_item
        )
        # self.tambah_barang.grid(row=1, column=0, padx=10, pady=10)
        # self.tambah_barang.grid_forget()

        # ════════════════════ Tombol Tersembunyi ════════════════════ #
        # ════════════════════════════════════════════════════════════ #

        self.entry_search_item = ctk.CTkEntry(
            master=self.frame,
            placeholder_text="🔍 Cari Barang",
            font=("Helvetica", 14)
        )
        self.entry_search_item.grid(row=0, column=3, padx=10, pady=10)

        self.button_sort = ctk.CTkOptionMenu(
            master=self.frame,
            font=("Helvetica", 14),
            values=[
                "Default",
                "Nama (Asc)",
                "Nama (Desc)",
                "Kuantitas (Asc)",
                "Kuantitas (Desc)"
            ]
        )
        self.button_sort.grid(row=0, column=4, padx=10, pady=10)

    # ════════════════════ --- ════════════════════ #

    def tambah_show(self):
        """ Menampilkan widget untuk menambah barang """
        self.frame_2.grid(row=2, column=0, padx=10, pady=(0, 10))
        self.entry_item_name.grid(
            row=1, column=0,
            padx=10, pady=10,
        )
        self.entry_quantity.grid(
            row=1, column=1,
            padx=10, pady=10,
        )
        self.tambah_barang.grid(
            row=1, column=2,
            padx=10, pady=10,
        )
        self.tambah.configure(text="Kembali", command=self.tambah_hide)

    def tambah_hide(self):
        """ Menyembunyikan widget 'Tambah Barang' """
        self.frame_2.grid_forget()
        self.entry_item_name.grid_forget()
        self.entry_quantity.grid_forget()
        self.tambah_barang.grid_forget()
        self.tambah.configure(text="Tambah Barang", command=self.tambah_show)

    def tambah_item(self):
        self.tabel.inventori[0]["Nama"] = self.entry_item_name.get()
        self.parent.update_idletasks()


if __name__ == "__main__":
    app = App()
    app.mainloop()
