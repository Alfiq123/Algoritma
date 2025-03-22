class TopiKerucut:
    """Menjumlahkan semua volume dari kerucut"""
    def __init__(self, diameter, tinggi, selisih_x, selisih_y, jumlah):
        self.diameter = diameter
        self.tinggi = tinggi
        self.selisih_x = selisih_x
        self.selisih_y = selisih_y
        self.jumlah = jumlah

    def for_loop(self):
        PI = 3.141592653589793
        total_volume = 0
        print("\n===== For Loop =====\n")

        for i in range(self.jumlah):
            i_diameter = self.diameter - i * self.selisih_x
            i_tinggi = self.tinggi - i * self.selisih_y
            jari_jari = i_diameter / 2
            volume = (1 / 3) * PI * (jari_jari ** 2) * i_tinggi

            if i_diameter <= 0 or i_tinggi <= 0 or volume <= 0:
                break

            total_volume += volume
            print(f"Topi ke-{i + 1}: Diameter = {i_diameter:.2f} cm, Tinggi = {i_tinggi:.2f} cm, Volume = {volume:.2f} cm³")

        print(f"\nTotal volume dari {self.jumlah} topi: {total_volume:.2f} cm³")

    def while_loop(self):
        PI = 3.141592653589793
        total_volume = 0
        i = 0
        print("\n===== While Loop =====\n")

        while i < self.jumlah:
            i_diameter = self.diameter - i * self.selisih_x
            i_tinggi = self.tinggi - i * self.selisih_y
            jari_jari = i_diameter / 2
            volume = (1 / 3) * PI * (jari_jari ** 2) * i_tinggi

            if i_diameter <= 0 or i_tinggi <= 0 or volume <= 0:
                break

            total_volume += volume
            print(f"Topi ke-{i + 1}: Diameter = {i_diameter:.2f} cm, Tinggi = {i_tinggi:.2f} cm, Volume = {volume:.2f} cm³")
            i += 1

        print(f"\nTotal volume dari {self.jumlah} topi: {total_volume:.2f} cm³")

    def while_true(self):
        PI = 3.141592653589793
        total_volume = 0
        i = 0
        print("\n===== While True =====\n")
        
        while True:

            if i == self.jumlah:
                break

            i_diameter = self.diameter - i * self.selisih_x
            i_tinggi = self.tinggi - i * self.selisih_y
            jari_jari = i_diameter / 2
            volume = (1 / 3) * PI * (jari_jari ** 2) * i_tinggi

            if i_diameter <= 0 or i_tinggi <= 0 or volume <= 0:
                break

            total_volume += volume
            print(f"Topi ke-{i + 1}: Diameter = {i_diameter:.2f} cm, Tinggi = {i_tinggi:.2f} cm, Volume = {volume:.2f} cm³")
            i += 1

        print(f"\nTotal volume dari {self.jumlah} topi: {total_volume:.2f} cm³")

class TopiLimas:
    """Menjumlahkan semua volume dari limas"""
    def __init__(self, sisi, tinggi, selisih_x, selisih_y, jumlah):
        self.sisi = sisi
        self.tinggi = tinggi
        self.selisih_x = selisih_x
        self.selisih_y = selisih_y
        self.jumlah = jumlah

    def for_loop(self):
        """For Loop"""
        total_volume = 0
        print("\n===== For Loop ===== \n")

        for i in range(self.jumlah):
            i_sisi = self.sisi - i * self.selisih_x
            i_tinggi = self.tinggi - i * self.selisih_y
            volume = (1/3) * (i_sisi ** 2) * i_tinggi

            if i_sisi <= 0 or i_tinggi <= 0 or volume <= 0:
                break

            total_volume += volume
            print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm, Tinggi: {i_tinggi} cm, Volume: {volume:.2f} cm³")
        print(f"Total Volume: {total_volume:.2f} cm³")

    def while_loop(self):
        """While Loop"""
        total_volume = 0
        i = 0
        print("\n===== While Loop =====\n")

        while i < self.jumlah:
            i_sisi = self.sisi - i * self.selisih_x
            i_tinggi = self.tinggi - i * self.selisih_y
            volume = (1/3) * (i_sisi ** 2) * i_tinggi

            if i_sisi <= 0 or i_tinggi <= 0 or volume <= 0:
                break

            total_volume += volume
            print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm, Tinggi: {i_tinggi} cm, Volume: {volume:.2f} cm³")
            i += 1
        print(f"Total Volume: {total_volume:.2f} cm³")

    def while_true(self):
        """While True"""
        total_volume = 0
        i = 0
        print("\n===== While True =====\n")

        while True:

            if i == self.jumlah:
                break

            i_sisi = self.sisi - i * self.selisih_x
            i_tinggi = self.tinggi - i * self.selisih_y
            volume = (1/3) * (i_sisi ** 2) * i_tinggi

            if i_sisi <= 0 or i_tinggi <= 0 or volume <= 0:
                break
            
            total_volume += volume
            print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm, Tinggi: {i_tinggi} cm, Volume: {volume:.2f} cm³")
            i += 1

        print(f"Total Volume: {total_volume:.2f} cm³")

def input_handler():
    while True:
        pilihan = str(input("Masukkan Pilihan Soal (1/2): "))

        if pilihan == "1":

            while True:

                try:
                    i_diameter = int(input("Masukkan Diameter Topi Kerucut: "))
                    i_tinggi = int(input("Masukkan Tinggi Topi Kerucut: "))
                    i_selisih_x = int(input("Masukkan Selisih 'x' Topi Kerucut: "))
                    i_selisih_y = int(input("Masukkan Selisih 'y' Topi Kerucut: "))
                    i_jumlah = int(input("Masukkan Jumlah Topi Kerucut: "))

                    if i_diameter < i_selisih_x:
                        print("\nnError: Selisih 'x' Lebih Tinggi dari 'Diameter Topi'!\n")
                        continue

                    elif i_tinggi < i_selisih_y:
                        print("\nnError: Selisih 'y' Lebih Tinggi dari 'Tinggi Topi'!\n")
                        continue

                    elif (i_diameter <= 0) or (i_tinggi <= 0) or (i_selisih_x <= 0) or (i_selisih_y <= 0) or (i_jumlah <= 0):
                        print("\nnError: Nilai Data Tidak Boleh Negatif!\n")
                        continue

                    kerucut = TopiKerucut(diameter = i_diameter, tinggi = i_tinggi, selisih_x = i_selisih_x, selisih_y = i_selisih_y, jumlah = i_jumlah)

                    kerucut.for_loop()
                    kerucut.while_loop()
                    kerucut.while_true()

                    break


                except ValueError:
                    print("\nError: Salah satu ukuran tidak valid, Aktivitas diulangi...!\n")
                    continue

            break

        elif pilihan == "2":
            while True:

                try:
                    i_sisi = int(input("Masukkan Sisi Topi Limas: "))
                    i_tinggi = int(input("Masukkan Tinggi Topi Limas: "))
                    i_selisih_x = int(input("Masukkan Selisih 'x' Topi Limas: "))
                    i_selisih_y = int(input("Masukkan Selisih 'y' Topi Limas: "))
                    i_jumlah = int(input("Masukkan Jumlah Topi Limas: "))

                    if i_sisi < i_selisih_x:
                        print("\nError: Selisih 'x' Lebih Tinggi dari 'Sisi Topi'!\n")
                        continue

                    elif i_tinggi < i_selisih_y:
                        print("\nError: Selisih 'y' Lebih Tinggi dari 'Tinggi Topi'!\n")
                        continue

                    elif (i_sisi <= 0) or (i_tinggi <= 0) or (i_selisih_x <= 0) or (i_selisih_y <= 0) or (i_jumlah <= 0):
                        print("\nNilai Data Tidak Boleh Negatif!\n")

                    limas = TopiLimas(sisi = i_sisi, tinggi = i_tinggi, selisih_x = i_selisih_x, selisih_y = i_selisih_y, jumlah = i_jumlah)

                    limas.for_loop()
                    limas.while_loop()
                    limas.while_true()

                    break

                except ValueError:
                    print("\nError: Salah satu ukuran tidak valid!\n")
                    continue

            break

        else:
            print("\nError: Pilihan tidak valid!\n")
            continue

input_handler()
