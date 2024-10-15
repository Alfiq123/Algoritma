# Panjang Rusuk sebuah kubus jika diketahui DIAGONAL RUANG-nya.

import math

# Input
diagonal_ruang = int(input("Masukkan Diagonal Ruang dari kubus: "))

rusuk = diagonal_ruang / math.sqrt(3)
print(f"Panjang rusuk kubus adalah {rusuk:.2f} cm")
