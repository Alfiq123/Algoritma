# Panjang persegi panjang jika diketahui LUAS & LEBAR-nya.

# Input
# lebar = int(input("Masukkan lebar persegi panjang: "))
# luas = int(input("Masukkan luas persegi panjang: "))

print("🟥️ ===== Mencari panjang persegi panjang jika diketahui LUAS & LEBAR-nya ===== 🟥️")

# Input lebar persegi panjang
while True:
    try:
        lebar = float(input("Masukkan lebar persegi panjang: "))
    except ValueError:
        print("🚨 Kamu memasukkan huruf atau karakter lain 🚨")
        continue
    else:
        break

# Input luas persegi panjang
while True:
    try:
        luas = float(input("Masukkan luas persegi panjang: "))
    except ValueError:
        print("🚨 Kamu memasukkan huruf atau karakter lain 🚨")
        continue
    else:
        break

# Rumus.
panjang = luas / lebar

# Keluar-an.
print("🏆 ===== Output ===== 🏆")
print(f"Lebar persegi panjang: {lebar:.2f} cm")
print(f"Luas persegi panjang: {luas:.2f} cm²")
print(f"Rumus: {luas:.2f} cm² / {lebar:.2f} cm")
print(f"Panjang persegi panjang tersebut adalah: {panjang:.2f} cm")
