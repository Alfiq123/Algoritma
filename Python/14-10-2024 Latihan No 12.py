# Nilai akhir mata kuliah jika diketahui: 
# Persentase Kehadiran (P), 
# Nilai Tugas (T), 
# Nilai UTS (NT),
# Nilai UAS (NS),
# Dengan rumus: (P + 2 * T + 3 * NT + 4 * NS) / 10

# Input
nilai_tugas = int(input("Masukkan Nilai Tugas: "))
nilai_uts = int(input("Masukkan Nilai UTS: "))
nilai_uas = int(input("Masukkan Nilai UAS: "))
persentase_kehadiran = int(input("Masukkan Persentase Kehadiran: "))

# Pengerjaan
nilai_akhir = (persentase_kehadiran + 2 * nilai_tugas + 3 *  nilai_uts + 4 * nilai_uas) / 10

# Hasilnya
print(f"Nilai Akhir Mata Kuliah adalah: {nilai_akhir:.2f}")
