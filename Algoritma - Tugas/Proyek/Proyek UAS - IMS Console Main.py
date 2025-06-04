class Aplikasi:
    def __init__(self):
        self.gudang = Gudang()  # Initialize warehouse with inventory

    def tampilkan_menu(self):
        """Display menu and handle user interaction"""
        while True:
            print(
                f"{'=' * 50}\n"
                "Pilihan Opsi:\n"
                "  1. Tambah Barang\n"
                "  2. Hapus Barang\n"
                "  3. Cari Barang\n"
                "  4. Urutkan Barang\n"
                "  5. Tampilkan Semua Barang\n"
                "  0. Keluar\n"
                f"{'=' * 50}\n"
            )
            self.handling_input()

    def handling_input(self):
        """Handle user menu selection"""
        user_input = input("Masukkan Pilihan Kamu: ").strip()

        if user_input == "0":
            print("\nKeluar dari aplikasi. Sampai jumpa!\n")
            exit()

        options = {
            "1": self.gudang.tambah_barang,
            "2": self.gudang.hapus_barang,
            "3": self.gudang.cari_barang,
            "4": self.gudang.urutkan_barang,
            "5": self.gudang.tampilkan_semua
        }

        if user_input in options:
            options[user_input]()
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.\n")


class Gudang:
    def __init__(self):
        self.inventory = {}  # More descriptive name than 'kosongan'

    # noinspection PyMethodMayBeStatic
    def _validasi_nama(self, nama):
        """Validate item name input"""
        if not nama:
            print("\nError: Nama barang tidak boleh kosong!\n")
            return False
        return True

    # noinspection PyMethodMayBeStatic
    def _validasi_jumlah(self, jumlah):
        """Validate quantity input"""
        try:
            jumlah = int(jumlah)
            if jumlah <= 0:
                print("\nError: Jumlah harus lebih besar dari nol!\n")
                return False
            return jumlah
        except ValueError:
            print("\nError: Jumlah harus berupa angka!\n")
            return False

    def tambah_barang(self):
        """Menambahkan barang ke inventori"""
        nama = input("Masukkan nama barang: ").strip()
        if not self._validasi_nama(nama):
            return

        jumlah = input("Masukkan jumlah barang: ").strip()
        jumlah = self._validasi_jumlah(jumlah)
        if not jumlah:
            return

        if nama in self.inventory:
            self.inventory[nama] += jumlah
            print(
                f"\n{jumlah} {nama} ditambahkan. "
                f"Total sekarang: {self.inventory[nama]}\n"
            )
        else:
            self.inventory[nama] = jumlah
            print(
                f"\n{nama} dengan jumlah {jumlah} berhasil ditambahkan!\n"
            )

    def hapus_barang(self):
        """Remove item from inventory"""
        nama = input("Masukkan nama barang yang ingin dihapus: ").strip()

        if not self._validasi_nama(nama):
            return

        if nama in self.inventory:
            del self.inventory[nama]
            print(f"\n{nama} berhasil dihapus dari inventori.\n")
        else:
            print(f"\n{nama} tidak ditemukan dalam inventori.\n")

    def cari_barang(self):
        """Search for item in inventory"""
        nama = input("Masukkan nama barang yang dicari: ").strip()

        if not self._validasi_nama(nama):
            return

        if nama in self.inventory:
            print(
                f"\n{nama} ditemukan dengan jumlah: {self.inventory[nama]}\n"
            )
        else:
            print(
                f"\n{nama} tidak ditemukan dalam inventori.\n"
            )

    def urutkan_barang(self):
        """Mengurutkan barang berdasarkan nama menggunakan Bubble Sort"""
        items = list(self.inventory.items())
        BubbleSorting.bubble_sort(items)
        print("\nBarang telah diurutkan:")
        for nama, jumlah in items:
            print(f"{nama}: {jumlah}")

    def tampilkan_semua(self):
        """Menampilkan semua barang di inventori"""
        if not self.inventory:
            print("Inventori kosong.")
            return

        print("\nDaftar barang dalam inventori:")
        for nama, jumlah in self.inventory.items():
            print(f"  • {nama}: {jumlah}")


class BubbleSorting:
    """
    A class to encapsulate the bubble sort algorithm.
    Sorts a list in-place.
    """

    @staticmethod
    def bubble_sort(values: list) -> None:
        """
        Sorts a list using the bubble sort algorithm in ascending order.
        Modifies the list in-place.

        Args:
            values (list): The list of comparable elements to be sorted.
        """
        total_elements = len(values)
        for current_pass in range(total_elements - 1):
            is_swapped = False

            for current_index in range(total_elements - 1 - current_pass):
                next_index = current_index + 1

                if values[current_index][0] > values[next_index][0]:
                    values[current_index], values[next_index] = values[next_index], values[current_index]

                    is_swapped = True

            if not is_swapped:
                break


if __name__ == "__main__":
    aplikasi = Aplikasi()
    aplikasi.tampilkan_menu()
