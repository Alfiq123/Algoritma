import math

# Panjang Diagonal Ruang jika diketahui VOLUME-nya.

# Input
volume = int(input("Masukkan nilai volume: "))

# Menghitung panjang diagonal ruang
# Rumus diagonal ruang: d = (V^(2/3)) * (3^(1/2))

# Cara mengerjakkan
diagonal_ruang = (volume ** (2/3)) * (math.sqrt(3))

# Hasil akhir
print(f"Panjang diagonal ruang adalah: {diagonal_ruang:.2f} cm")
