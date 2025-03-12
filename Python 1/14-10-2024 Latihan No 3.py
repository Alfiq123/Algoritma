import math
# Panjang sisi segitiga sama sisi jika diketahui LUAS-nya.

# Input
# luas = int(input("Masukkan luas segitiga sama sisi: "))

print("🔻 ===== Mencari panjang sisi segitiga sama sisi jika diketahui LUAS-nya ===== 🔻")

# Input di dalam pengulangan
while True:
    try:
        luas = int(float(input("Masukkan luas segitiga sama sisi: ")))
    except ValueError:
        print("⛔️ Kamu tidak memasukkan angka ⛔️")
        continue
    else:
        break

# Rumus

# sisi = (luas  * 4 / 3 ** 0.5) **  0.5
# print("Panjang sisi segitiga sama sisi tersebut adalah:", sisi, "cm")

# Rumus - √(4 * L) / √3
sisi = math.sqrt((4 * luas) / math.sqrt(3))

# Output
print("🏆 ===== Panjangnya adalah: ===== 🏆")
print(f"Panjang sisi segitiga sama sisi tersebut adalah: {sisi:.2f} cm")
