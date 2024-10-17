import math

# Panjang Rusuk sebuah kubus jika diketahui DIAGONAL RUANG-nya.

# Input
# diagonal_ruang = int(input("Masukkan Diagonal Ruang dari kubus: "))

print("🧊🦴 ===== Mencari panjang rusuk kubus jika diketahui DIAGONAL RUANG-nya ===== 🦴🧊")

# Input - Diagonal Ruang
while True:
    try:
        diagonal_ruang = float(input("Masukkan Diagonal Ruang dari kubus: "))
    except ValueError:
        print("🚫 Kamu memasukkan karakter lain selain angka 🚫")
        continue
    else:
        break

# Rumus Rusuk - Diagonal Ruang / √3
rusuk = diagonal_ruang / math.sqrt(3)

# Output
print("🏁 ===== Hasil ===== 🏁")
print(f"Diagonal Ruang kubus: {diagonal_ruang:.2f} cm")
print(f"Rumus: {diagonal_ruang:.2f} cm / √3")
print(f"Panjang rusuk kubus adalah {rusuk:.2f} cm")
