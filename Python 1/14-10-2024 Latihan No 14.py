# Kecepatan (Km/Jam) tempuh jika diketahui JARAK TEMPUH (Meter) & WAKTU TEMPUH (Menit).

# Input
# jarak_tempuh = float(input("Masukkan jarak tempuh (Meter): "))
# waktu_tempuh = float(input("Masukkan waktu tempuh (Menit): "))

print("🏎️💨 ===== Mencari kecepatan tempuh jika diketahui jarak tempuh dan waktu tempuh ===== 💨🏎️")

# Input - Jarak Tempuh
while True:
    try:
        jarak_tempuh = float(input("Masukkan jarak tempuh (Meter): "))
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
    
# Rumus - Jarak / Waktu
kecepatan = jarak_tempuh / (waktu_tempuh / 60)

# Output
print("🏁 ===== Hasil ===== 🏁")
print(f"Jarak yang ditempuh adalah: {jarak_tempuh:.2f} Meter")
print(f"Waktu yang ditempuh adalah: {waktu_tempuh:.2f} Menit")
print("==================================================")
print("Kecepatan: Jarak / Waktu")
print(f"Rumus: {jarak_tempuh:.2f} Meter / ({waktu_tempuh:.2f} Menit / 60)")
print(f"Jadi: {jarak_tempuh:.2f} Meter / {waktu_tempuh / 60:.2f} Jam")
print("==================================================")
print(f"Kecepatan yang ditempuh adalah sekitar: {kecepatan:.2f} Km/Jam")
