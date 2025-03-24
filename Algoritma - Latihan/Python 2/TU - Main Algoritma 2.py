from math import pi
class BangunRuang:
    def __init__(self):
        pass

    def kubus(s):
        luas = 6 * s ** 2
        volume = s ** 3
        return f"Luas Permukaan: {luas} cm", f"Volume: {volume} cm"

    def balok(p, l, t):
        luas = 2 * ((p * l) + (p * t) + (l * t))
        volume = p * l * t
        return f"Luas Permukaan: {luas} cm", f"Volume: {volume} cm"
    
    def prisma(l_alas, k_alas, t_prisma):
        luas = 2 * l_alas + (k_alas * t_prisma)
        volume = l_alas * t_prisma
        return f"Luas Permukaan: {luas} cm", f"Volume: {volume} cm"
    
    def limas(l_alas, l_selimut, t_limas):
        luas = l_alas + l_selimut
        volume = (1/3) * l_alas * t_limas
        return f"Luas Permukaan: {luas} cm", f"Volume: {volume} cm"
    
    def tabung(jari, tinggi):
        luas = 2 * pi * jari * (jari + tinggi)
        volume = pi * (jari ** 2) * tinggi
        return f"Luas Permukaan: {luas:,.2f} cm", f"Volume: {volume:,.2f} cm"
    
def input_tracker():
    pilihan = str(input("Masukkan Pilihan: "))
    if pilihan == "1":
        i_sisi = int(input("Masukkan Sisi Kubus: "))
        bangun = BangunRuang.kubus(s = i_sisi)
        print(bangun)

    elif pilihan == "2":
        i_panjang = int(input("Masukkan Panjang Balok: "))
        i_lebar = int(input("Masukkan Lebar Balok: "))
        i_tinggi = int(input("Masukkan Tinggi Balok: "))
        bangun = BangunRuang.balok(p = i_panjang, l = i_lebar, t = i_tinggi)
        print(bangun)

    elif pilihan == "3":
        i_lalas = int(input("Masukkan Luas Alas Prisma: "))
        i_kalas = int(input("Masukkan Keliling Alas Prisma: "))
        i_tprisma = int(input("Masukkan Tinggi Prisma: "))
        bangun = BangunRuang.prisma(l_alas = i_lalas, k_alas = i_kalas, t_prisma = i_tprisma)
        print(bangun)

    elif pilihan == "4":
        i_l_alas = int(input("Masukkan Luas Alas Limas: "))
        i_l_selimut = int(input("Masukkan Luas Selimut Limas: "))
        i_t_limas = int(input("Masukkan TInggi Limas: "))
        bangun = BangunRuang.limas(l_alas = i_l_alas, l_selimut = i_l_selimut, t_limas = i_t_limas)
        print(bangun)

    elif pilihan == "5":
        i_jari = int(input("Masukkan Jari Tabung: "))
        i_tinggi = int(input("Masukkan Tinggi Tabung: "))
        bangun = BangunRuang.tabung(jari = i_jari, tinggi = i_tinggi)
        print(bangun)
    
    else:
        input_tracker()

input_tracker()