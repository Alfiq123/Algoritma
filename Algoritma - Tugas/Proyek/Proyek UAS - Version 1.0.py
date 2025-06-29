import json
from tabulate import tabulate


# General Usage.
# TODO: [x] Buat User Input.
# TODO: [x] Buat Table.

# Main Menu.
# TODO: [x] Buat tampilan menu.
# TODO: [ ] Mengatur data di dalam `.json`.

# User Interaction.
# TODO: [x] User dapat menambahkan barang.
# TODO: [x] User dapat menghapus barang.
# TODO: [x] User dapat mencari barang.
# TODO: [x] User dapat mengurutkan barang.
# TODO: [ ] User dapat mengurangi barnag. - Obsolete.
# TODO: [ ] User dapat peringatan ketika barangnya hampir habis. - Obsolete.

# Algorithm.
# TODO: [x] Buat Algoritma Quick Sort.
# TODO: [x] Buat Algoritma Binary Search

# GUI.
# TODO: FINAL - [ ] Buat PyQt.

class Program:
    def __init__(self) -> None:
        self.filename = "Product_Lists_2.json"
        self.data = self.load_data()

    @staticmethod
    def user_validation(prompt: str) -> int | None:
        while True:
            try:
                valid_value = int(input(prompt))
                if valid_value < 0:
                    print("\nError: Nilai tidak boleh dibawah nol!\n")
                    continue
                return valid_value
            except ValueError:
                print("\nError: Input tidak valid! Masukkan angka bulat.\n")

    def pilihan_menu(self) -> None:
        print(
            "Pilihan Menu:\n"
            "  [1] Tambah Barang\n"
            "  [2] Hapus Barang\n"
            "  [3] Cari Barang\n"
            "  [4] Urutkan Barang\n"
            "  [x] Memasukkan Data (.json) - Deprecated\n"
            "  [6] Tampilkan Data\n"
        )
        while True:
            pilihan = str(input("Masukkan Pilihan Kamu: "))
            if pilihan == "1":
                self.add_item_to_inventory()
                break
            elif pilihan == "2":
                self.delete_items()
                break
            elif pilihan == "3":
                self.find_items()
                break
            elif pilihan == "4":
                self.sort_items()
                break
            elif pilihan == "6":
                self.open_json_file()
                break
            else:
                continue

    # TODO: [1] Tambah Barang.
    # ████████░░
    def add_items(self) -> dict[str, str | int]:
        """
        Fungsi untuk menambahkan barang ke Inventori.
        Return: Dictionary
        """
        print("\n───── Menambah Barang ─────\n")

        barang_nama = str(input("Masukkan Nama Barang: ")).strip()
        barang_kuantitas = self.user_validation("Masukkan Kuantitas Barang: ")
        barang_harga = self.user_validation("Masukkan Harga Barang: ")

        return {
            "nama": barang_nama,
            "kuantitas": barang_kuantitas,
            "harga": barang_harga
        }

    def add_item_to_inventory(self) -> None:
        """
        Menambahkan item baru ke file inventori.
        """
        self.data.append(self.add_items())
        self.save_data(self.data)
        print(
            f"\nBarang '{self.data[-1]['nama']}' "
            f"berhasil ditambahkan ke inventori.\n"
        )

    # TODO: [2] Hapus Barang.
    # █████░░░░░
    def delete_items(self) -> None:
        print("\n───── Menghapus Barang ─────\n")

        self.open_json_file()

        nama_barang = str(
            input("Masukkan nama barang yang ingin dihapus: ")
        ).strip()

        # Jika inventori kosong
        if not self.data:
            print("Inventori kosong.")
            return

        # Menghitung jumlah barang sebelum dihapus
        jumlah_sebelum = len(self.data)

        # Membuat list baru tanpa barang yang namanya sesuai (case-insensitive)
        data_baru = [
            item for item in self.data
            if item['nama'].strip().lower() != nama_barang.lower()
        ]

        # Menghitung jumlah barang yang terhapus
        jumlah_terhapus = jumlah_sebelum - len(data_baru)

        if jumlah_terhapus == 0:
            print(
                f"\nBarang '{nama_barang}' tidak ditemukan dalam inventori!"
            )
        else:
            # Menyimpan data baru ke file
            self.save_data(data_baru)
            print(
                f"\nBerhasil menghapus {jumlah_terhapus} "
                f"barang '{nama_barang}'!"
            )

    # TODO: [3] Cari Barang.
    # ████████░░
    def find_items(self) -> None:
        """
        Dungsi untuk mencari barang di Inventori menggunakan Binary Search
        """
        nama_barang = str(input("Masukkan Nama Barang Yang Ingin Dicari: "))
        # data = self.load_data()
        if not self.data:
            print("Inventori kosong.")
            return

        # Urutkan data berdasarkan nama barang (wajib untuk binary search!)
        self.quicksort(
            array=self.data,
            low=0,
            high=len(self.data) - 1,
            key="nama"
        )

        # Ambil hanya list nama untuk dicari
        nama_list = [item["nama"] for item in self.data]
        index = self.binary_search(nama_list, nama_barang)

        if index != -1:
            item = self.data[index]
            table = [
                [
                    index + 1, item["nama"], item["kuantitas"], item["harga"]
                ]
            ]
            self.show_table(table=table)

        else:
            print(f"Barang dengan nama '{nama_barang}' tidak ditemukan.")

    # TODO: [4] Urutkan Barang.
    # ████████░░
    def sort_items(self) -> None:
        print("\n───── Mengurutkan Barang ─────\n")

        if not self.data:
            print("Inventori kosong.")
            return

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

        self.quicksort(self.data, 0, len(self.data) - 1, pilihan_key)

        print(f"\nInventori setelah diurutkan berdasarkan {pilihan_key}:\n")
        self.show_table(table=self.generate_table(self.data))

    # ═══════════════ JSON FILE HANDLER ═══════════════ #
    #       ─────────────── BEGIN ───────────────       #

    def load_data(self):
        """ Memuat File JSON """
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self, data):
        """ Menyimpan File JSON """
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def open_json_file(self):
        """ Membuka File JSON """
        data = self.load_data()

        if not data:
            print("Inventori kosong.")
            return

        self.show_table(table=self.generate_table(self.data))

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
    def show_table(table):
        print(tabulate(
            table,
            headers=["ID", "Item", "Quantity", "Price"],
            tablefmt="fancy_grid"
        ))

    @staticmethod
    def generate_table(items):
        """Membuat tabel dari data barang (1 atau banyak)."""
        if not isinstance(items, list):
            items = [items]
        return [
            [idx + 1, item['nama'], item['kuantitas'], item['harga']]
            for idx, item in enumerate(items)
        ]

    def running(self):
        self.pilihan_menu()


if __name__ == "__main__":
    Program().running()
