import customtkinter as ctk

from tables import TabelKolom


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
