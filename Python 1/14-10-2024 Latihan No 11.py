import math

# Panjang Diagonal Ruang jika diketahui VOLUME-nya.

# Input
# volume = int(input("Masukkan nilai volume: "))

print("🧊🚪 ===== Mencari panjang diagonal ruang jika diketahui VOLUME-nya ===== 🚪🧊")

# Input - Volume
while True:
    try:
        volume = float(input("Masukkan nilai volume: "))
    except ValueError:
        print("🚫 Kamu memasukkan karakter lain selain angka 🚫")
        continue
    else:
        break

# Menghitung panjang diagonal ruang
# Rumus diagonal ruang: d = (V^(2/3)) * (3^(1/2))

# Rumus - Diagonal Ruang
diagonal_ruang = (volume ** (2/3)) * (math.sqrt(3))

# Hasil akhir
print("🏁 ===== Hasil ===== 🏁")
print(f"Volume kubus adalah: {volume:.2f} cm³")
print(f"Rumus: {volume:.2f} cm³ ^ (2/3) * √3")
print(f"Panjang diagonal ruang adalah: {diagonal_ruang:.2f} cm")
