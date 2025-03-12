# Nilai akhir mata kuliah jika diketahui: 
# Persentase Kehadiran (P), 
# Nilai Tugas (T), 
# Nilai UTS (NT),
# Nilai UAS (NS),
# Dengan rumus: (P + 2 * T + 3 * NT + 4 * NS) / 10

# Input
# nilai_tugas = int(input("Masukkan Nilai Tugas: "))
# nilai_uts = int(input("Masukkan Nilai UTS: "))
# nilai_uas = int(input("Masukkan Nilai UAS: "))
# persentase_kehadiran = int(input("Masukkan Persentase Kehadiran: "))

print("📚 ===== Mencari nilai akhir mata kuliah ===== 📚")

# Input - Nilai Tugas
while True:
    try:
        nilai_tugas = int(input("Masukkan Nilai Tugas: "))
    except ValueError:
        print("🚫 Kamu memasukkan karakter lain selain angka 🚫")
        continue
    else:
        break

# Input - Nilai UTS
while True:
    try:
        nilai_uts = int(input("Masukkan Nilai UTS: "))
    except ValueError:
        print("🚫 Kamu memasukkan karakter lain selain angka 🚫")
        continue
    else:
        break

# Input - Nilai UAS
while True:
    try:
        nilai_uas = int(input("Masukkan Nilai UAS: "))
    except ValueError:
        print("🚫 Kamu memasukkan karakter lain selain angka 🚫")
        continue
    else:
        break

# Input - Persentase Kehadiran
while True:
    try:
        persentase_kehadiran = int(input("Masukkan Persentase Kehadiran: "))
    except ValueError:
        print("🚫 Kamu memasukkan karakter lain selain angka 🚫")
        continue
    else:
        break

# Pengerjaan
# Rumus: (P + 2 * T + 3 * NT + 4 * NS) / 10
nilai_akhir = (persentase_kehadiran + 2 * nilai_tugas + 3 *  nilai_uts + 4 * nilai_uas) / 10

# Hasilnya
print("🏁 ===== Hasil ===== 🏁")
print(f"Nilai Tugas: {nilai_tugas}")
print(f"Nilai UTS: {nilai_uts}")
print(f"Nilai UAS: {nilai_uas}")
print(f"Persentase Kehadiran: {persentase_kehadiran}")
print("==================================================")
print(f"Rumus: (P + 2 * T + 3 * NT + 4 * NS) / 10")
print(f"Rumus: ({persentase_kehadiran} + 2 * {nilai_tugas} + 3 * {nilai_uts} + 4 * {nilai_uas}) / 10")
print("==================================================")
print(f"Nilai Akhir Mata Kuliah adalah: {nilai_akhir:.2f}")
