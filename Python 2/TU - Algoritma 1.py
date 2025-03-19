from math import pi

def topi(D, T, x, y, n):
    """
    Menjumlahkan setiap volume.

    Argumen / Parameter:
        D: Diameter topi terbesar.
        T: Tinggi topi terbesar.
        x: Selisih diameter antar topi berurutan.
        y: Selisih tinggi antar topi berurutan.
        n: Jumlah total topi.
    """

    total_volume = 0

    for i in range(n):

        # Diameter I = Diameter - (Iterasi * Selisih diameter).
        di = D - i * x
        
        # Tinggi I = Tinggi - (Iterasi * Selisih tinggi).
        ti = T - i * y

        # Mengubah diameter ke jari².
        jari = di / 2

        # Rumus kerucut.
        volume = (1 / 3) * pi * (jari ** 2) * ti

        # Menjumlahkan Setiap Volume.
        total_volume += volume

        # Volume setiap iterasi.
        print(f"Iterasi ke-{i + 1}, Dengan hasil: {volume:.2f} cm³")

    # Total volume.
    print(f"\nTotal volume dari topi adalah: {total_volume:.2f} cm³")

# Penggunaan.
# topi(D = 20, T = 30, x = 4, y = 5, n = 5)
topi(D = 15, T = 25, x = 3, y = 4, n = 6)

# Penggunaan + Input.

# D = float(input("Masukkan diameter topi terbesar (D): "))
# T = float(input("Masukkan tinggi topi terbesar (T): "))
# x = float(input("Masukkan selisih diameter antar topi (x): "))
# y = float(input("Masukkan selisih tinggi antar topi (y): "))
# n = int(input("Masukkan jumlah total topi (n): "))

# topi(D, T, x, y, n)