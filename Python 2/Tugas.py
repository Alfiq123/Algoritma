class LimasSegiEnam:
    def __init__(self, la, ta):
        self.la = la
        self.ta = ta

    def limas_segienam(self):
        """Volume = (1/3) Luas Alas * Tinggi Limas"""
        volume = (1/3) * self.la * self.ta
        return volume
    
    def limas_segienam_2(self):
        """Volume = (1/3) Luas Alas * Tinggi Limas"""
        volume = (1/3) * self.la * self.ta
        print(f"{volume} cm³")

class Balok:
    def __init__(self, p, l, t):
        self.p = p
        self.l = l
        self.t = t

    def balok(self):
        """Volume = Panjang * Lebar * Tinggi"""
        volume = self.p * self.l * self.t
        return volume
    
    def balok_2(self):
        """Volume = Panjang * Lebar * Tinggi"""
        volume = self.p * self.l * self.t
        print(f"{volume} cm³")

limassegienam = LimasSegiEnam(la = 24, ta = 12)
balok = Balok(p = 12, l = 24, t = 36)

pilihan = str(input("Masukkan Pilihan: "))
if pilihan == "1":
    limassegienam.limas_segienam_2()

elif pilihan == "2":
    balok.balok_2()

else:
    print("System Aborted!")

# print(f"{limas_segienam(la = 12, ta = 24)} cm³")
# print(f"{balok(p = 6, l = 7, t = 8)} cm³")

# print(f"{limassegienam.limas_segienam()} cm³")
# limassegienam.limas_segienam_2()

# print()

# print(f"{balok.balok()} cm³")
