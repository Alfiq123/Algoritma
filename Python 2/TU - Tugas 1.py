class LimasSegiEnam:
    def __init__(self, luas_alas, tinggi_limas):
        self.luas_alas = luas_alas
        self.tinggi_limas = tinggi_limas

    def limas_segienam(self):
        """Volume = (1/3) Luas Alas * Tinggi Limas"""
        volume = (1/3) * self.luas_alas * self.tinggi_limas
        return volume
    
    def limas_segienam_2(self):
        """Volume = (1/3) Luas Alas * Tinggi Limas"""
        volume = (1/3) * self.luas_alas * self.tinggi_limas
        print(f"Volume dari limas tersebut adalah: {volume:,.0f} cm³")

class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def balok(self):
        """Volume = Panjang * Lebar * Tinggi"""
        volume = self.panjang * self.lebar * self.tinggi
        return volume
    
    def balok_2(self):
        """Volume = Panjang * Lebar * Tinggi"""
        volume = self.panjang * self.lebar * self.tinggi
        print(f"Volume dari balok tersebut adalah: {volume:,.0f} cm³")

def input_handler():
    while True:
        pilihan = str(input("Masukkan Pilihan: "))
        if pilihan == "1":

            while True:
                try:
                    input_alas = int(input("Masukkan Luas Alas: "))
                    input_tinggi = int(input("Masukkan Tinggi Limas: "))
                    break

                except ValueError:
                    print("\nInput tidak valid!\n")
                    continue

            limas = LimasSegiEnam(luas_alas = input_alas, tinggi_limas = input_tinggi)
            limas.limas_segienam_2()

            break

        elif pilihan == "2":
            while True:
                try:
                    input_panjang = int(input("Masukkan Panjang Balok: "))
                    input_lebar = int(input("Masukkan Lebar Balok: "))
                    input_tinggi = int(input("Masukkan Tinggi Balok: "))
                    break
                
                except ValueError:
                    print("\nInput tidak valid!\n")
                    continue

            balok = Balok(panjang = input_panjang, lebar = input_lebar, tinggi = input_tinggi)
            balok.balok_2()
            break

        else:
            print("\nSystem Aborted!\n")
            continue

input_handler()
