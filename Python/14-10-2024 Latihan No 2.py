# Tinggi suatu segitiga jika diketahui LUAS & ALAS-nya.

# Input
# alas = int(input("Masukkan alas segitiga: "))
# luas = int(input("Masukkan luas segitiga: "))

print("🔺 ===== Mencari tinggi suatu segitiga jika diketahui LUAS & ALAS-nya ===== 🔺")

# Input alas segitiga
while True:
    try:
        alas = int(float(input("Masukkan alas segitiga: ")))
    except ValueError:
        print("⛔️ Tolong masukkan angka ⛔️")
        continue
    else:
        break

# Input luas segitiga
while True:
    try:
        luas = int(float(input("Masukkan luas segitiga: ")))
    except ValueError:
        print("⛔️ Kamu tidak memasukkan angka ⛔️")
        continue
    else:
        break

# Output
# Rumus = luas * (2 / alas) / ATAU \ (2 * luas) / alas.

# tinggi = luas * 2 / alas

# Rumus = (2 * luas) / alas
tinggi = (2 * luas) / alas

# Output
print("🏆 ===== Hasil: ===== 🏆")
print(f"Tinggi segitiga tersebut adalah: {tinggi:.2f} cm")
