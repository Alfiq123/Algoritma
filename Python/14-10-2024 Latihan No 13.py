# Jarak (Meter) yang ditempuh jika diketahui KECEPATAN (Km/Jam) & WAKTU TEMPUH (Menit).

# Input
kecepatan =  float(input("Masukkan kecepatan (Km/Jam) :"))
waktu_tempuh = float(input("Masukkan waktu tempuh (Menit) :"))

# Rumus dan Output
jarak = kecepatan * (waktu_tempuh / 60)
print(f"Jarak yang ditempuh adalah sekitar: {jarak:.2f} Meter")
