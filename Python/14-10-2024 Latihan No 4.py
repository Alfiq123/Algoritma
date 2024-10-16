import math
# Panjang sisi persegi jika diketahui LUAS-nya.

# Input
luas = int(input("Masukkan luas persegi: "))

# Rumus = √L - Luas Akar
sisi = math.sqrt(luas)

# Hasil
print(f"Panjang sisi persegi tersebut adalah: {sisi:.2f} cm")
