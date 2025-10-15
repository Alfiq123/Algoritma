import json
from tabulate import tabulate


# General Usage.
# TODO: [x] Buat User Input.
# TODO: [x] Buat Table.

# Main Menu.
# TODO: [x] Buat tampilan menu.

# User Interaction.
# TODO: [x] User dapat menambahkan barang.
# TODO: [x] User dapat mengurangi barnag.
# TODO: [x] User dapat menghapus barang.
# TODO: [x] User dapat mencari barang.
# TODO: [x] User dapat mengurutkan barang.
# TODO: [x] User dapat mengedit barang.
# TODO: [x] User dapat peringatan ketika barangnya hampir habis.

# Algorithm.
# TODO: [x] Buat Algoritma Quick Sort.
# TODO: [x] Buat Algoritma Binary Search

# Deprecated.
# TODO: Deprecated: [ ] Mengatur data di dalam `.json`.

# GUI.
# TODO: FINAL - [ ] Buat PyQt.

class Program:
    def __init__(self) -> None:
        self.namafile = "Product_Lists.json"
        self.data = self.muat_data()

    @staticmethod
    def validasi_integer(prompt: str) -> int | None:
        while True:
            try:
                angka_valid = int(input(prompt))
                if angka_valid < 0:
                    print("\nError: Nilai tidak boleh dibawah nol!\n")
                    continue
                return angka_valid
            except ValueError:
                print("\nError: Input tidak valid! Masukkan angka bulat.\n")

    def pilihan_menu(self) -> None:
        print(
            "Pilihan Menu:\n"
            "  [1] Tambah Barang\n"
            "  [2] Ambil Barang\n"
            "  [3] Hapus Barang\n"
            "  [4] Cari Barang\n"
            "  [5] Urutkan Barang\n"
            "  [6] Edit Barang\n"
            "  [7] Tampilkan Data\n"
            "\n"
            "  [X] Keluar\n"
        )
        actions = {
            "1": self.tambah_barang,
            "2": self.ambil_barang,
            "3": self.hapus_barang,
            "4": self.cari_barang,
            "5": self.urutkan_barang,
            "6": self.edit_barang,
            "7": self.buka_file_json,
        }

        while True:
            pilihan = input("Masukkan Pilihan Kamu: ").strip()
            action = actions.get(pilihan)
            if action: action(); break
            elif pilihan in ("x", "X"): break
            else: print("\nPilihan tidak valid. Silakan coba lagi.\n")

    # TODO: [1] Tambah Barang.
    def kumpulkan_item(self) -> dict[str, str | int]:
        """
        Mengumpulkan informasi barang baru dari pengguna.

        Melakukan input nama barang, memvalidasi agar tidak duplikat
        atau kosong, serta meminta kuantitas dan harga dengan
        validasi tambahan.

        Returns:
            dict[str, str | int]: Dictionary berisi data barang yang valid,
            atau dictionary kosong jika proses dibatalkan.
        """
        print("\n───── Menambah Barang ─────\n")

        nama_barang = str(input("Masukkan Nama Barang: ")).strip()

        if not nama_barang:
            print("\nNama barang tidak boleh kosong\n")
            return {}

        kuantitas_barang = self.validasi_integer("Masukkan Kuantitas Barang: ")
        harga_barang = self.validasi_integer("Masukkan Harga Barang: ")

        return {
            "nama": nama_barang,
            "kuantitas": kuantitas_barang,
            "harga": harga_barang
        }

    def tambah_barang(self) -> None:
        """
        Menambahkan barang baru ke dalam inventori.

        Memanggil fungsi `kumpulkan_item()` untuk input data.
        Jika data valid dan inventori tidak kosong,
        data disimpan dan file diperbarui.

        Menampilkan pesan konfirmasi setelah penambahan berhasil.
        """
        tambah_item = self.kumpulkan_item()
        if not tambah_item:
            print("\nProses penambahan dibatalkan.\n")
            return

        # Cek duplikasi nama barang (case-insensitive)
        for item in self.data:
            if item["nama"].lower() == tambah_item["nama"].lower():
                print(
                    f"\nBarang < {tambah_item['nama']} > sudah ada di inventori!"
                    f"\n  • Kuantitas saat ini: {item['kuantitas']}"
                    f"\n  • Harga saat ini: Rp {item['harga']:,}\n"
                )

                # Konfirmasi tambah kuantitas
                tambah_stok = input(
                    "Tambah kuantitas ke stok yang ada? (y/n): "
                ).strip().lower()

                if tambah_stok != 'y':
                    print("\nPenambahan dibatalkan.\n")
                    return

                # Tambahkan kuantitas ke stok yang ada
                item["kuantitas"] += tambah_item["kuantitas"]

                # Konfirmasi update harga jika berbeda
                if item["harga"] != tambah_item["harga"]:
                    print(
                        f"\nHarga berbeda!"
                        f"\n  • Harga lama: Rp {item['harga']:,}"
                        f"\n  • Harga baru: Rp {tambah_item['harga']:,}"
                    )

                    update_harga = input(
                        "Update harga barang? (y/n): "
                    ).strip().lower()

                    if update_harga == 'y':
                        item["harga"] = tambah_item["harga"]
                        print(f"Harga diperbarui: Rp {tambah_item['harga']:,}")

                # Simpan perubahan
                self.simpan_data(data=self.data)
                self.buka_file_json()
                print(
                    f"\nStok < {item['nama']} > berhasil ditambahkan!"
                    f"\n  • Kuantitas baru: {item['kuantitas']}"
                    f"\n  • Harga saat ini: Rp {item['harga']:,}\n"
                )

                return

        # Jika tidak ada duplikasi, tambahkan barang baru
        self.data.append(tambah_item)
        self.simpan_data(data=self.data)
        self.buka_file_json()
        print(
            f"\nBarang < {tambah_item['nama']} > "
            f"berhasil ditambahkan ke inventori!"
            f"\n  • Kuantitas: {tambah_item['kuantitas']}"
            f"\n  • Harga: {tambah_item['harga']}\n"
        )

    # TODO: [2] Mengurangi / Mengambil Barang.
    def ambil_barang(self):
        self.buka_file_json()

        if self.is_inventory_kosong(): return

        nama_barang = str(input("\nMasukkan Nama Barang: "))
        jumlah_barang = self.validasi_integer("Masukkan Jumlah Barang: ")

        for item in self.data:
            if item["nama"].lower() != nama_barang.lower(): continue

            if jumlah_barang > item["kuantitas"]:
                print(
                    f'\nGagal mengambil barang: stok < {item["nama"]} > '
                    f'hanya {item["kuantitas"]}, tidak cukup untuk '
                    f'mengambil {jumlah_barang}.\n'
                )
                return

            item["kuantitas"] -= jumlah_barang
            self.simpan_data(data=self.data)
            self.buka_file_json()

            if item["kuantitas"] < 10:
                print(
                    f"Peringatan: Sisa stok < {item['nama']} > "
                    f"tinggal {item['kuantitas']}!"
                )

            return

        print(f"Barang < {nama_barang} > tidak ditemukan di inventaris.")

    # TODO: [3] Hapus Barang.
    def hapus_barang(self) -> None:
        print("\n───── Menghapus Barang ─────\n")

        self.buka_file_json()

        if self.is_inventory_kosong(): return

        while True:
            nama_barang = str(
                input("\nMasukkan nama barang yang ingin dihapus: ")
            ).strip()

            if nama_barang == "":
                print("\nNama barang tidak boleh kosong!\n")
                continue
            break

        data_baru = []  # List kosong untuk menampung item yang tidak dihapus

        for item in self.data:
            # Normalisasi nama item
            nama_item = item["nama"].strip().lower()

            # Normalisasi nama yang ingin dihapus
            nama_target = nama_barang.lower()

            if nama_item != nama_target:
                # Tambahkan item ke data_baru kalau tidak sama
                data_baru.append(item)

        # Menghitung jumlah barang yang terhapus
        jumlah_terhapus = len(self.data) - len(data_baru)

        if jumlah_terhapus == 0:
            print(
                f"\nBarang < {nama_barang} > tidak ditemukan dalam inventori!"
            )

        else:
            # Menyimpan data baru ke file
            self.simpan_data(data_baru)
            self.buka_file_json()
            print(
                f"\nBerhasil menghapus {jumlah_terhapus} "
                f"barang < {nama_barang} >!"
            )

    # TODO: [4] Cari Barang.
    def cari_barang(self) -> None:
        """
        Dungsi untuk mencari barang di Inventori menggunakan Binary Search
        """
        print("\n───── Mencari Barang ─────\n")

        if self.is_inventory_kosong(): return

        nama_barang = str(input(
            "Masukkan Nama Barang Yang Ingin Dicari: "
        )).title()

        # Urutkan data berdasarkan nama barang (wajib untuk binary search!)
        self.quicksort(
            array=self.data,
            low=0,
            high=len(self.data) - 1,
            key="nama"
        )

        # Ambil hanya list nama untuk dicari
        nama_list = [item["nama"] for item in self.data]
        index = self.binary_search(arr=nama_list, target=nama_barang)

        if index != -1:
            item = self.data[index]
            table = [[
                item["nama"],
                item["kuantitas"],
                item["harga"]
            ]]
            self.lihat_tabel(table=table)

        else: print(f"Barang dengan nama < {nama_barang} > tidak ditemukan.")

    # TODO: [5] Urutkan Barang.
    def urutkan_barang(self) -> None:
        print("\n───── Mengurutkan Barang ─────\n")

        if self.is_inventory_kosong(): return

        print(
            "Urutkan Berdasarkan:\n"
            "  1. Nama\n"
            "  2. Kuantitas\n"
            "  3. Harga\n"
        )

        key_map = {
            "1": "nama",
            "2": "kuantitas",
            "3": "harga"
        }
        pilihan = input("Masukkan pilihan (1-3): ")
        pilihan_key = key_map.get(pilihan)

        if pilihan not in key_map:
            print("Pilihan tidak valid!")
            return

        self.quicksort(
            array=self.data,
            low=0,
            high=len(self.data) - 1,
            key=pilihan_key
        )

        print(f"\nInventori setelah diurutkan berdasarkan {pilihan_key}:\n")
        self.lihat_tabel(table=self.generate_tabel(self.data))

    # TODO: [6] Edit Barang.
    def edit_barang(self) -> None:
        print("\n───── Mengedit Barang ─────\n")

        self.buka_file_json()

        nama_barang = input("\nMasukkan nama barang yang ingin diedit: ").strip()

        for item in self.data:
            if item["nama"].lower() == nama_barang.lower():
                print(
                    f"\nData saat ini:\n"
                    f"  Nama     : {item['nama']}\n"
                    f"  Kuantitas: {item['kuantitas']}\n"
                    f"  Harga    : Rp {item['harga']:,}\n"
                    f"\nPilih data yang ingin diubah:\n"
                    f"  1. Nama\n"
                    f"  2. Kuantitas\n"
                    f"  3. Harga\n"
                )
                keymap = {
                    "1": "nama",
                    "2": "kuantitas",
                    "3": "harga"
                }
                pilihan = input("Masukkan pilihan (1/2/3): ").strip()

                if pilihan not in keymap:
                    print("\nPilihan tidak valid!\n")
                    return

                key = keymap[pilihan]

                if key == "nama":
                    nama_baru = input("Masukkan nama baru: ").strip()
                    if not nama_baru:
                        print("\nNama tidak boleh kosong!\n"); return
                    item["nama"] = nama_baru

                elif key == "kuantitas":
                    kuantitas_baru = self.validasi_integer(
                        "Masukkan kuantitas baru: "
                    )
                    if kuantitas_baru is None:
                        print("Input dibatalkan atau tidak valid."); return
                    item["kuantitas"] = kuantitas_baru

                elif key == "harga":
                    harga_baru = self.validasi_integer("Masukkan harga baru: ")
                    if harga_baru is None:
                        print("Input dibatalkan atau tidak valid."); return
                    item["harga"] = harga_baru

        self.simpan_data(data=self.data)
        self.buka_file_json()

    # ═══════════════ JSON FILE HANDLER ═══════════════ #
    #       ─────────────── BEGIN ───────────────       #

    def muat_data(self):
        """ Memuat File JSON """
        try:
            with open(self.namafile, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def simpan_data(self, data):
        """ Menyimpan File JSON """
        with open(self.namafile, "w") as file:
            json.dump(data, file, indent=4)

    def buka_file_json(self) -> None:
        """ Membuka File JSON """
        self.data = self.muat_data()  # Ini penting!

        self.lihat_tabel(table=self.generate_tabel(self.data))

        for item in self.data:
            if item["kuantitas"] == 0:
                print(
                    f"Peringatan: Stok '{item['nama']} "
                    f"telah habis' ({item['kuantitas']} unit)"
                )
            elif item["kuantitas"] <= 10:
                print(
                    f"Peringatan: Stok '{item['nama']}' "
                    f"hampir habis ({item['kuantitas']} unit)"
                )

    #        ─────────────── END ───────────────        #
    # ═════════════════════════════════════════════════ #

    # ═══════════════ BINARY SEARCH ALGORITHM ═══════════════ #
    #          ─────────────── BEGIN ───────────────          #

    # TODO: [x] Buat Algoritma Binary Search
    @staticmethod
    def binary_search(arr: list[int | str], target: int | str) -> int:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    #           ─────────────── END ───────────────           #
    # ═══════════════════════════════════════════════════════ #

    # ═══════════════ QUICKSORT ALGORITHM ═══════════════ #
    #        ─────────────── BEGIN ───────────────        #

    # TODO: [x] Buat Algoritma Quick Sort.
    @staticmethod
    def partition(array, low, high, key):
        pivot = array[high][key]
        i = low - 1

        for j in range(low, high):
            if array[j][key] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quicksort(self, array, low, high, key):
        if low < high:
            pi = self.partition(array, low, high, key)
            self.quicksort(array, low, pi - 1, key)
            self.quicksort(array, pi + 1, high, key)

    #         ─────────────── END ───────────────         #
    # ═══════════════════════════════════════════════════ #

    @staticmethod
    def generate_tabel(items) -> list[list[int | str]]:
        """Membuat tabel dari data barang (1 atau banyak)."""
        if not isinstance(items, list): items = [items]

        # Membuat list kosong untuk menyimpan hasil
        result = []

        # Loop melalui setiap item dengan index-nya
        for item_data in items:
            # Membuat entry baru untuk setiap item:
            #   - Nama item
            #   - Kuantitas item
            #   - Harga item
            new_entry = [
                item_data["nama"],  # Nama item
                item_data["kuantitas"],  # Jumlah item
                f'Rp {item_data["harga"]:,}'  # Harga per item
            ]

            # Tambahkan entry baru ke dalam hasil
            result.append(new_entry)

        # Kembalikan list hasil yang sudah dibuat
        return result

    @staticmethod
    def lihat_tabel(table) -> None:
        print(tabulate(
            tabular_data=table,
            headers=["Nama", "Kuantitas", "Harga"],
            tablefmt="fancy_grid"
        ))

    def is_inventory_kosong(self) -> bool:
        if not self.data:
            print("Inventori kosong.")
            return True
        return False

    def jalankan(self):
        self.pilihan_menu()


if __name__ == "__main__":
    Program().jalankan()
