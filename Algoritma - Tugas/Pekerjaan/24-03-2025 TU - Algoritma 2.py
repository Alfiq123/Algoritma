class BangunRuang:
    @staticmethod
    def kubus(s):
        luas = 6 * s ** 2
        volume = s ** 3
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"

    @staticmethod
    def balok(p, l, t):
        luas = 2 * ((p * l) + (p * t) + (l * t))
        volume = p * l * t
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"
    
    @staticmethod
    def prisma(l_alas, k_alas, t_prisma):
        luas = 2 * l_alas + (k_alas * t_prisma)
        volume = l_alas * t_prisma
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"
    
    @staticmethod
    def limas(l_alas, l_selimut, t_limas):
        luas = l_alas + l_selimut
        volume = (1/3) * l_alas * t_limas
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"
    
    @staticmethod
    def tabung(jari, tinggi):
        PI = 3.141592653589793
        luas = 2 * PI * jari * (jari + tinggi)
        volume = PI * (jari ** 2) * tinggi
        return f"\nLuas Permukaan: {luas:,.2f} cm³, Volume: {volume:,.2f} cm³"
    
def input_tracker():
    while True:

        print("\nPilih Bangun Ruang (Lagi)\n  1. Kubus\n  2. Balok\n  3. Prisma\n  4. Limas\n  5. Tabung\n")

        pilihan = str(input("Masukkan Pilihan: "))
        if pilihan == "1":
            while True:
                try:
                    i_sisi = int(input("Masukkan Sisi Kubus: "))

                except ValueError:
                    print("\nError: Input tidak valid!\n")
                    continue

                bangun = BangunRuang.kubus(s = i_sisi)
                print(bangun)
                break
            break

        elif pilihan == "2":
            while True:
                try:
                    panjang = int(input("Masukkan Panjang Balok: "))
                    lebar = int(input("Masukkan Lebar Balok: "))
                    tinggi = int(input("Masukkan Tinggi Balok: "))

                except ValueError:
                    print("\nError: Input tidak valid!\n")
                    continue

                bangun = BangunRuang.balok(p = panjang, l = lebar, t = tinggi)
                print(bangun)
                break
            break

        elif pilihan == "3":
            while True:
                try:
                    lalas = int(input("Masukkan Luas Alas Prisma: "))
                    kalas = int(input("Masukkan Keliling Alas Prisma: "))
                    tprisma = int(input("Masukkan Tinggi Prisma: "))

                except ValueError:
                    print("\nnError: Input tidak valid!\n")
                    continue

                bangun = BangunRuang.prisma(l_alas = lalas, k_alas = kalas, t_prisma = tprisma)
                print(bangun)
                break
            break

        elif pilihan == "4":
            while True:
                try:
                    lalas = int(input("Masukkan Luas Alas Limas: "))
                    lselimut = int(input("Masukkan Luas Selimut Limas: "))
                    tlimas = int(input("Masukkan TInggi Limas: "))

                except ValueError:
                    print("\nnError: Input tidak valid!\n")
                    continue
            
                bangun = BangunRuang.limas(l_alas = lalas, l_selimut = lselimut, t_limas = tlimas)
                print(bangun)
                break
            break

        elif pilihan == "5":
            while True:
                try:
                    jari = int(input("Masukkan Jari Tabung: "))
                    tinggi = int(input("Masukkan Tinggi Tabung: "))

                except ValueError:
                    print("\nnError: Input tidak valid!\n")
                    continue

                bangun = BangunRuang.tabung(jari = jari, tinggi = tinggi)
                print(bangun)
                break
            break

        else:
            print("\nError: Masukkan Pilihan yang Benar!\n")
            continue

input_tracker()
