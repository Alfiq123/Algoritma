class StudiD:

    @staticmethod
    def lahan(kategori, sewa):
        if (kategori == "a") and (sewa > 0):
            print("\n「 Lahan A 」\n")
            return f"Biaya Sewa: Rp. {5000 + (3000 * (sewa - 1)):,.2f}"
        elif (kategori == "b") and (sewa > 0):
            print("\n「 Lahan B 」\n")
            return f"Biaya Sewa: Rp. {7000 + (3500 * (sewa - 1)):,.2f}"
        elif (kategori == "c") and (sewa > 0):
            print("\n「 Lahan C 」\n")
            return f"Biaya Sewa: Rp. {6000 + (2500 * (sewa - 1)):,.2f}"
        else:
            print("\nError: Bilangan tidak boleh negatif!\n")
            return handler()

def handler():

    while True:
        print("\n===== Persewaan Lahan Parkir =====\n")
        kategori = str(input("Masukkan Kategori Lahan (a/b/c): ")).lower()

        if kategori not in ("a", "b", "c"):
            print("\nError: Kategori tidak valid, Program diulang!\n")
            continue

        try:
            sewa = int(input("Masukkan Lama Sewa: "))

        except ValueError:
            print("\nError: Lama sewa bukan angka, Program diulang!\n")
            continue

        hasil = StudiD.lahan(kategori, sewa)
        print(hasil)
        break

handler()
