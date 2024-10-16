# Jarak (Meter) yang ditempuh jika diketahui KECEPATAN (Km/Jam) & WAKTU TEMPUH (Menit).

# Input
kecepatan =  float(input("Masukkan kecepatan (Km/Jam) :"))
waktu_tempuh = float(input("Masukkan waktu tempuh (Menit) :"))

# Rumus / Cara
jarak = kecepatan * (waktu_tempuh / 60)

# Hasil akhir
print(f"Jarak yang ditempuh adalah sekitar: {jarak:.2f} Meter")
