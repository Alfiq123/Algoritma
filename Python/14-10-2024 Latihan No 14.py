# Kecepatan (Km/Jam) tempuh jika diketahui JARAK TEMPUH (Meter) & WAKTU TEMPUH (Menit).

# Input
jarak_tempuh = float(input("Masukkan jarak tempuh (Meter): "))
waktu_tempuh = float(input("Masukkan waktu tempuh (Menit): "))

# Rumus + Output
kecepatan = jarak_tempuh / (waktu_tempuh / 60)
print(f"Kecepatan yang ditempuh adalah sekitar: {kecepatan:.2f} Km/Jam")
