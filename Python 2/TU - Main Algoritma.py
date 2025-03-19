# TODO: Tambahkan Failsafe.
# TODO: Refactor.
# TODO: Documentasi.

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
            print(f"Topi ke-{i + 1}: Diameter = {i_diameter:.2f}, Tinggi = {i_tinggi:.2f}, Volume = {volume:.2f} cm³")

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
            print(f"Topi ke-{i + 1}: Diameter = {i_diameter:.2f}, Tinggi = {i_tinggi:.2f}, Volume = {volume:.2f} cm³")
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
            print(f"Topi ke-{i + 1}: Diameter = {i_diameter:.2f}, Tinggi = {i_tinggi:.2f}, Volume = {volume:.2f} cm³")
            i += 1

        print(f"\nTotal volume dari {self.jumlah} topi: {total_volume:.2f} cm³")

kerucut_for = TopiKerucut(diameter = 20, tinggi = 30, selisih_x = 4, selisih_y = 5, jumlah = 5)
kerucut_for.for_loop()

kerucut_while = TopiKerucut(diameter = 20, tinggi = 30, selisih_x = 4, selisih_y = 5, jumlah = 5)
kerucut_while.while_loop()

kerucut_true = TopiKerucut(diameter = 20, tinggi = 30, selisih_x = 4, selisih_y = 5, jumlah = 5)
kerucut_true.while_true()



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
            print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm³, Tinggi: {i_tinggi} cm³, Volume: {volume:.2f} cm³ cm³")
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
            print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm³, Tinggi: {i_tinggi} cm³, Volume: {volume:.2f} cm³ cm³")
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
            print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm³, Tinggi: {i_tinggi} cm³, Volume: {volume:.2f} cm³ cm³")
            i += 1

        print(f"Total Volume: {total_volume:.2f} cm³")


limas_for = TopiLimas(sisi = 5, tinggi = 8, selisih_x = 2, selisih_y = 3, jumlah = 4)
limas_for.for_loop()

limas_while = TopiLimas(sisi = 5, tinggi = 8, selisih_x = 2, selisih_y = 3, jumlah = 4)
limas_while.while_loop()

limas_true = TopiLimas(sisi = 5, tinggi = 8, selisih_x = 2, selisih_y = 3, jumlah = 4)
limas_true.while_true()
