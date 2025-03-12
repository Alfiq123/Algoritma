# Jarak (Meter) yang ditempuh jika diketahui KECEPATAN (Km/Jam) & WAKTU TEMPUH (Menit).

# Input
# kecepatan =  float(input("Masukkan kecepatan (Km/Jam) :"))
# waktu_tempuh = float(input("Masukkan waktu tempuh (Menit) :"))

print("🚗💨 ===== Mencari jarak yang ditempuh jika diketahui kecepatan dan waktu tempuh ===== 💨🚗")

# Input - Kecepatan
while True:
    try:
        kecepatan = float(input("Masukkan kecepatan (Km/Jam): "))
    except ValueError:
        print("❗ Kamu memasukkan karakter lain selain angka ❗")
        continue
    else:
        break

# Input - Waktu Tempuh
while True:
    try:
        waktu_tempuh = float(input("Masukkan waktu tempuh (Menit): "))
    except ValueError:
        print("❗ Kamu memasukkan karakter lain selain angka ❗")
        continue
    else:
        break

# Rumus - Kecepatan * Waktu
jarak = kecepatan * (waktu_tempuh / 60)

# Hasil akhir
print("🏁 ===== Hasil ===== 🏁")
print(f"Kecepatan yang ditempuh adalah sekitar: {kecepatan:.2f} Km/Jam")
print(f"Waktu yang ditempuh adalah sekitar: {waktu_tempuh:.2f} Menit")
print("==================================================")
print("Jarak: Kecepatan * Waktu")
print(f"Rumus: {kecepatan:.2f} Km/Jam * ({waktu_tempuh:.2f} Menit / 60)")
print(f"Jadi: {kecepatan:.2f} Km/Jam * {waktu_tempuh / 60:.2f} Jam")
print("==================================================")
print(f"Jarak yang ditempuh adalah sekitar: {jarak:.2f} Meter")
