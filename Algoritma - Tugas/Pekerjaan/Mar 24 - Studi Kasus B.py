class StudiB:
    """Kelas untuk menghitung biaya sewa gedung."""
    @staticmethod
    def gedung(kategori, sewa):
        """Menghitung biaya sewa berdasarkan kategori dan lama sewa (tahun).

        Arguments:
            kategori (str): Kategori gedung ('a', 'b', atau 'c').
            sewa (int): Lama sewa dalam tahun.

        Returns:
            float: Biaya sewa.
        """
        if kategori == "a":
            return 7000000 + (6500000 * (sewa - 1))
        elif kategori == "b":
            return 8000000 + (7000000 * (sewa - 1))
        else:
            return 7500000 + (6000000 * (sewa - 1))

def handler():
    """Menangani input pengguna dan menampilkan biaya sewa."""
    while True:
        print("\n===== Komplek Pergudangan =====\n")
        kategori = str(input("Masukkan Kategori Gedung (a/b/c): ")).lower()
        if kategori not in ("a", "b", "c"):
            print("\nError: Kategori tidak valid. Silakan masukkan 'a', 'b', atau 'c'.\n")
            continue
        while True:
            try:
                sewa = int(input("Masukkan Lama Sewa: "))
                if sewa <= 0:
                    raise ValueError
            except ValueError:
                print("\nError: Lama sewa harus berupa angka positif.\n")
                continue
            break
        biaya_sewa = StudiB.gedung(kategori, sewa)
        print(f"\n「 Gedung {kategori.upper()} 」\n")
        print(f"Biaya Sewa: Rp. {biaya_sewa:,.2f}")
        break

handler()
