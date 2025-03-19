# Soal A:
#   Di dalam sebuah topi berbentuk kerucut dengan ukuran diameter D dan tinggi T terdapat n
#   (ditentukan) topi dengan ukuran yang lebih kecil. Apabila setiap topi yang lebih kecil
#   mempunyai selisih ukuran diameter=x, dan tinggi = y (x,y ditentukan) dari topi yang lebih besar,
#   maka berapakah total volume seluruh topi ?

# Catatan:
#   • Nilai x, y ditentukan
#   • Nilai D, T baru haruslah < dari D, T lama.
#   • Jumlah topi berbatas, dengan nilai D,T baru tidak boleh negative, dan Nilai volume topi terkecil tidak boleh == 0.

# V = 1/3 × π × r × r × t
# Volume = (1/3) * (22/7) * r^2 x t

from math import pi

def total_volume_topi(d, t, x, y, n):
    """
    Argumens:
        d: Diameter topi terbesar.
        t: Tinggi topi terbesar.
        x: Selisih diameter antar topi berurutan.
        y: Selisih tinggi antar topi berurutan.
        n: Jumlah total topi.
    """
    total_volume = 0

    """ Menghitung volume setiap topi dan menjumlahkannya."""
    for i in range(n):
        i_diameter = d - i * x
        i_tinggi = t - i * y

        """Menghitung Jari-Jari topi."""
        jari_jari = i_diameter / 2

        """Menghitung Volume topi."""
        volume = (1 / 3) * pi * (jari_jari ** 2) * i_tinggi
        total_volume += volume
        print(f"Topi ke-{i}: Diameter = {i_diameter:.2f}, Tinggi = {i_tinggi:.2f}, Volume = {volume:.2f}")

    print(f"\nTotal volume dari {n} topi: {total_volume:.2f} satuan kubik")

# Contoh penggunaan.
total_volume_topi(d = 20, t = 30, x = 4, y = 5, n = 5)