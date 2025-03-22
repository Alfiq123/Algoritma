# class TopiLimas:
#     def __init__(self, sisi, tinggi, selisih_x, selisih_y, jumlah):
#         """
#         Argumen:
#             sisi: Panjang sisi alas limas
#             tinggi: Tinggi limas
#             selisih_x: Selisih panjang sisi setiap iterasi
#             selisih_y: Selisih tinggi setiap iterasi
#             jumlah: Jumlah iterasi
#         """
#         self.sisi = sisi
#         self.tinggi = tinggi
#         self.selisih_x = selisih_x
#         self.selisih_y = selisih_y
#         self.jumlah = jumlah

#     def hitung_volume(self):
#         """
#         Menghitung total volume dari serangkaian limas.
#         """
#         total_volume = 0

#         for i in range(self.jumlah):
#             i_sisi = self.sisi - i * self.selisih_x
#             i_tinggi = self.tinggi - i * self.selisih_y

#             volume = (1 / 3) * (i_sisi ** 2) * i_tinggi

#             if i_sisi <= 0 or i_tinggi <= 0 or volume <= 0:
#                 break

#             total_volume += volume

#             print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm, Tinggi: {i_tinggi} cm, Volume: {volume:.2f} cm³")

#         print(f"\nTotal Volume: {total_volume:.2f} cm³")


# # Membuat objek dari kelas TopiLimas
# topi = TopiLimas(sisi=5, tinggi=8, selisih_x=2, selisih_y=3, jumlah=4)

# # Memanggil metode untuk menghitung volume
# topi.hitung_volume()



# def topi_limas(sisi, tinggi, selisih_x, selisih_y, jumlah):
#     total_volume = 0

#     for i in range(jumlah):
#         i_sisi = sisi - i * selisih_x
#         i_tinggi = tinggi - i * selisih_y

#         volume = (1/3) * (i_sisi ** 2) * i_tinggi

#         if i_sisi <= 0 or i_tinggi <= 0 or volume <= 0:
#             break

#         total_volume += volume

#         print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm³, Tinggi: {i_tinggi} cm³, Volume: {volume:.2f} cm³ cm³")

#     print(f"\nTotal Volume: {total_volume:.2f} cm³")

# topi_limas(sisi = 5, tinggi = 8, selisih_x = 2, selisih_y = 3, jumlah = 4)



# def topi_limas_while(sisi, tinggi, selisih_x, selisih_y, jumlah):
#     total_volume = 0
#     i = 0

#     while i < jumlah:
#         i_sisi = sisi - i * selisih_x
#         i_tinggi = tinggi - i * selisih_y

#         volume = (1/3) * (i_sisi ** 2) * i_tinggi

#         if i_sisi <= 0 or i_tinggi <= 0 or volume <= 0:
#             break

#         total_volume += volume

#         print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm³, Tinggi: {i_tinggi} cm³, Volume: {volume:.2f} cm³ cm³")

#         i += 1

#     print(f"\nTotal Volume: {total_volume:.2f} cm³")

# topi_limas_while(sisi = 5, tinggi = 8, selisih_x = 2, selisih_y = 3, jumlah = 4)



# def topi_limas_while2(sisi, tinggi, selisih_x, selisih_y, jumlah):
#     total_volume = 0
#     i = 0

#     while True:
#         i_sisi = sisi - i * selisih_x
#         i_tinggi = tinggi - i * selisih_y

#         volume = (1/3) * (i_sisi ** 2) * i_tinggi

#         if i_sisi <= 0 or i_tinggi <= 0 or volume <= 0:
#             break

#         total_volume += volume

#         print(f"Iterasi ke-{i + 1}, Sisi Alas: {i_sisi} cm³, Tinggi: {i_tinggi} cm³, Volume: {volume:.2f} cm³ cm³")

#         i += 1

#         if i == jumlah:
#             break

#     print(f"\nTotal Volume: {total_volume:.2f} cm³")

# topi_limas_while2(sisi = 5, tinggi = 8, selisih_x = 2, selisih_y = 3, jumlah = 4)