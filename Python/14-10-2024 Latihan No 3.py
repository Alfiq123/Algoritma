import math
# Panjang sisi segitiga sama sisi jika diketahui LUAS-nya.

luas = int(input("Masukkan luas segitiga sama sisi: "))

# sisi = (luas  * 4 / 3 ** 0.5) **  0.5
# print("Panjang sisi segitiga sama sisi tersebut adalah:", sisi, "cm")

sisi = math.sqrt((4 * luas) / math.sqrt(3))
print(f"Panjang sisi segitiga sama sisi tersebut adalah: {sisi:.2f} cm")
