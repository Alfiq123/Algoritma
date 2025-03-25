class StudiD:
    """Kelas untuk menghitung biaya sewa lahan parkir."""
    @staticmethod
    def lahan(kategori, sewa):
        """Menghitung biaya sewa berdasarkan kategori dan lama sewa (jam).

        Arguments:
            kategori (str): Kategori lahan ('a', 'b', atau 'c').
            sewa (int): Lama sewa dalam jam.

        Returns:
            float: Biaya sewa.
        """
        if (kategori == "a"):
            return 5000 + (3000 * (sewa - 1))
        elif (kategori == "b"):
            return 7000 + (3500 * (sewa - 1))
        else:
            return 6000 + (2500 * (sewa - 1))

def handler():
    while True:
        print("\n===== Persewaan Lahan Parkir =====\n")
        kategori = str(input("Masukkan Kategori Lahan (a/b/c): ")).lower()
        if kategori not in ("a", "b", "c"):
            print("\nError: Kategori tidak valid, Program diulang!\n")
            continue
        while True:
            try:
                sewa = int(input("Masukkan Lama Sewa: "))
                if sewa < 0:
                    raise ValueError
            except ValueError:
                print("\nError: Lama sewa harus berupa angka positif!\n")
                continue
            break
        biaya_sewa = StudiD.lahan(kategori, sewa)
        print(f"\n「 Kategori {kategori.upper()} 」\n")
        print(f"Biaya Sewa: Rp. {biaya_sewa:,.2f}")
        break

handler()
