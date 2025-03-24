from math import pi
class BangunRuang:
    @staticmethod
    def kubus(s):
        luas = 6 * s ** 2
        volume = s ** 3
        return f"Luas Permukaan: {luas} cm³", f"Volume: {volume} cm³"

    @staticmethod
    def balok(p, l, t):
        luas = 2 * ((p * l) + (p * t) + (l * t))
        volume = p * l * t
        return f"Luas Permukaan: {luas} cm³", f"Volume: {volume} cm³"
    
    @staticmethod
    def prisma(l_alas, k_alas, t_prisma):
        luas = 2 * l_alas + (k_alas * t_prisma)
        volume = l_alas * t_prisma
        return f"Luas Permukaan: {luas} cm³", f"Volume: {volume} cm³"
    
    @staticmethod
    def limas(l_alas, l_selimut, t_limas):
        luas = l_alas + l_selimut
        volume = (1/3) * l_alas * t_limas
        return f"Luas Permukaan: {luas} cm³", f"Volume: {volume} cm³"
    
    @staticmethod
    def tabung(jari, tinggi):
        luas = 2 * pi * jari * (jari + tinggi)
        volume = pi * (jari ** 2) * tinggi
        return f"Luas Permukaan: {luas:,.2f} cm³", f"Volume: {volume:,.2f} cm³"
    
def input_tracker():
    print("""
Bangun Ruang (Lagi).

    1. Kubus        
    2. Balok
    3. Prisma
    4. Limas
    5. Tabung
    """)
    pilihan = str(input("Masukkan Pilihan: "))
    if pilihan == "1":
        try:
            i_sisi = int(input("Masukkan Sisi Kubus: "))

        except ValueError:
            print("\nInput tidak valid!\n")
            input_tracker()

        bangun = BangunRuang.kubus(s = i_sisi)
        print(bangun)

    elif pilihan == "2":
        try:
            panjang = int(input("Masukkan Panjang Balok: "))
            lebar = int(input("Masukkan Lebar Balok: "))
            tinggi = int(input("Masukkan Tinggi Balok: "))

        except ValueError:
            print("\nInput tidak valid!\n")
            input_tracker()

        bangun = BangunRuang.balok(p = panjang, l = lebar, t = tinggi)
        print(bangun)

    elif pilihan == "3":
        try:
            lalas = int(input("Masukkan Luas Alas Prisma: "))
            kalas = int(input("Masukkan Keliling Alas Prisma: "))
            tprisma = int(input("Masukkan Tinggi Prisma: "))

        except ValueError:
            print("\nInput tidak valid!\n")
            input_tracker()

        bangun = BangunRuang.prisma(l_alas = lalas, k_alas = kalas, t_prisma = tprisma)
        print(bangun)

    elif pilihan == "4":
        try:
            lalas = int(input("Masukkan Luas Alas Limas: "))
            lselimut = int(input("Masukkan Luas Selimut Limas: "))
            tlimas = int(input("Masukkan TInggi Limas: "))

        except ValueError:
            print("\nInput tidak valid!\n")
            input_tracker()
    
        bangun = BangunRuang.limas(l_alas = lalas, l_selimut = lselimut, t_limas = tlimas)
        print(bangun)

    elif pilihan == "5":
        try:
            jari = int(input("Masukkan Jari Tabung: "))
            tinggi = int(input("Masukkan Tinggi Tabung: "))

        except ValueError:
            print("\nInput tidak valid!\n")
            input_tracker()

        bangun = BangunRuang.tabung(jari = jari, tinggi = tinggi)
        print(bangun)
    
    else:
        input_tracker()

input_tracker()