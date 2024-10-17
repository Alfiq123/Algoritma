import math
# Panjang sisi persegi jika diketahui LUAS-nya.

# Input
# luas = int(input("Masukkan luas persegi: "))

print("🟩️ ===== Mencari panjang sisi persegi jika diketahui LUAS-nya ===== 🟩️")

while True:
    try:
        luas = float(input("Masukkan luas persegi: "))
    except ValueError:
        print("🚨 Kamu memasukkan huruf atau karakter lain 🚨")
        continue
    else:
        break

# Rumus = √L - Luas Akar
sisi = math.sqrt(luas)

# Hasil
print("🏆 ===== Output ===== 🏆")
print(f"Luas persegi: {luas:,.2f} cm²")
print(f"Rumus: √{luas:,.2f} cm²")
print(f"Panjang sisi persegi tersebut adalah: {sisi:.2f} cm")
