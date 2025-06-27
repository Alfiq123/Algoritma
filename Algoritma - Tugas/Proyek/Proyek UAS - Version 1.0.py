import json
from tabulate import tabulate

# TODO: [x] Buat User Input.
# TODO: [x] Buat Table.

# TODO: [ ] Buat tampilan menu.
# TODO: [ ] Mengatur data di dalam `.json`.

# TODO: [ ] User dapat menambahkan barang.
# TODO: [ ] User dapat menghapus barang.
# TODO: [ ] User dapat mencari barang.
# TODO: [ ] User dapat mengurutkan barang.
# TODO: [ ] User dapat peringatan ketika barangnya hampir habis.

# TODO: [ ] Buat Algoritma Quick Sort.
# TODO: [ ] Buat Algoritma Search Sort (Linear atau Binary).

class Program:
    def __init__(self):
        self.filename = "Product_Lists_2.json"

    # noinspection PyMethodMayBeStatic
    def user_validation(self, prompt):
        while True:
            try:
                valid_value = int(input(prompt))
                if valid_value < 0:
                    print("\nError: Nilai tidak boleh dibawah nol!\n")
                    continue
                return valid_value
            except ValueError:
                print("\nError: Input tidak valid! Masukkan angka bulat.\n")

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def user_input(self):

        print(
            "Masukkan Pilihan\n"
            "  1. Menambah Barang\n"
            "  2. Menghapus Barang\n"
            "  3. Mencari Barang\n"
            "  4. Mengurutkan Barang\n"
            "  5. Memasukkan Data (.json)\n"
        )

        barang_nama = str(input("Masukkan Nama Barang: ")).strip()
        barang_kuantitas = self.user_validation("Masukkan Kuantitas Barang: ")
        barang_harga = self.user_validation("Masukkan Harga Barang: ")

        return {
            "nama": barang_nama,
            "kuantitas": barang_kuantitas,
            "harga": barang_harga
        }

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def open_json_file(self):
        data = self.load_data()

        if not data:
            print("Inventori kosong.")
            return

        table = []
        for idx, item in enumerate(data, start=1):
            table.append([idx, item['nama'], item['kuantitas'], item['harga']])

        print(
            tabulate(
                table,
                headers=["ID", "Item", "Quantity", "Price"],
                tablefmt="fancy_grid"
            )
        )

    def add_item(self, new_item):
        data = self.load_data()
        data.append(new_item)
        self.save_data(data)

    def running(self):
        self.open_json_file()
        self.add_item(self.user_input())
        print("\nItem berhasil ditambahkan!\n")
        self.open_json_file()  # Tampilkan inventori terbaru

class QuickSorter:
    def __init__(self, arr):
        """
        Inisialisasi objek QuickSorter dengan array yang akan diurutkan.
        Kita membuat salinan array untuk menghindari modifikasi array asli
        jika diinginkan, atau langsung bekerja pada referensi jika tidak.
        Untuk contoh ini, kita akan memodifikasi array in-place.
        """
        self.arr = arr

    def partition(self, low, high):
        """
        Metode helper untuk partisi array.
        Ini adalah metode internal (diawali dengan underscore) karena
        biasanya tidak dipanggil langsung dari luar kelas.
        """
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def sort(self):
        """
        Metode publik untuk memulai proses pengurutan QuickSort secara iteratif.
        """
        if not self.arr:
            return []

        stack = [(0, len(self.arr) - 1)]

        while stack:
            low, high = stack.pop()

            if low < high:
                pi = self.partition(low, high)

                # Dorong subarray kanan ke stack terlebih dahulu untuk optimasi
                # (memastikan subarray yang lebih kecil diproses lebih dulu,
                # tapi ini bukan keharusan mutlak untuk kebenaran algoritma)
                stack.append((pi + 1, high))
                stack.append((low, pi - 1))
        return self.arr

if __name__ == "__main__":
    Program().running()
