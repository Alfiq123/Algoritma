class StudiA:
    """Kelas untuk menghitung harga hotspot Modi."""

    @staticmethod
    def megabyte(kode, mb):
        """Menghitung harga berdasarkan rentang MB. 

        Arguments: 
            kode (str): Kode/Ukuran paket ('r', 'c', atau 'v').
            mb (int): Banyaknya jumlah MB.

        Returns:
            float: Biaya pemakaian bandwidth.
        """
        harga_per_mb = {
            "r": [(1, 50, 2000), (51, 80, 4500), (81, float("inf"), 6500)],
            "c": [(1, 50, 5000), (51, 80, 7000), (81, float("inf"), 10000)],
            "v": [(1, 50, 7500), (51, 80, 10000), (81, float("inf"), 15000)]
        }

        if kode in harga_per_mb:
            for (batas_bawah, batas_atas, harga) in (harga_per_mb[kode]):
                if batas_bawah <= mb <= batas_atas:
                    return f"Rp. {harga * mb:,.2f}"

def handle_input():
    """Menangani input dari pengguna."""
    while True:
        print("\n===== Hotspot Modi =====\n")
        pilih = str(input("Masukkan Pilihan (r/c/v): ")).lower()
        if pilih not in ["r", "c", "v"]:
            print("\nError: Input tidak valid, Ulang dari awal!\n")
            continue
        while True:
            try:
                mb = int(input("Masukkan Jumlah MB: "))
                if mb < 0:
                    raise ValueError
            except ValueError:
                print("\nError: Jumlah MB harus berupa angka positif!\n")
                continue
            break
        hasil = StudiA.megabyte(pilih, mb)
        print(hasil)
        break

handle_input()
