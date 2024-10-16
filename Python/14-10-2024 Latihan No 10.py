import math

# Panjang Rusuk sebuah kubus jika diketahui DIAGONAL RUANG-nya.

# Input
diagonal_ruang = int(input("Masukkan Diagonal Ruang dari kubus: "))

# Rumus
rusuk = diagonal_ruang / math.sqrt(3)

# Output
print(f"Panjang rusuk kubus adalah {rusuk:.2f} cm")
