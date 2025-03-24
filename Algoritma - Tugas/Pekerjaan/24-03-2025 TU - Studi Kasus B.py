class StudiB:

    @staticmethod
    def gedung(kategori, sewa):
        if kategori == "a":
            print("\n「 Gedung A 」\n")
            return f"Biaya Sewa: Rp. {7000000 + (6500000 * (sewa - 1)):,.2f}"
        elif kategori == "b":
            print("\n「 Gedung B 」\n")
            return f"Biaya Sewa: Rp. {8000000 + (7000000 * (sewa - 1)):,.2f}"
        else:
            print("\n「 Gedung C 」\n")
            return f"Biaya Sewa: Rp. {7500000 + (6000000 * (sewa - 1)):,.2f}"

def handler():
        
    while True:
        print("\n===== Komplek Pergudangan =====\n")
        kategori = str(input("Masukkan Kategori Gedung (a/b/c): ")).lower()

        if kategori not in ("a", "b", "c"):
            print("\nError: Kategori tidak valid, Program diulang!\n")
            continue

        try:
            sewa = int(input("Masukkan Lama Sewa: "))

        except ValueError:
            print("\nError: Lama sewa bukan angka, Program diulang!\n")
            continue
            
        hasil = StudiB.gedung(kategori, sewa)
        print(hasil)
        break

handler()
