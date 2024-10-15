# Persentase mahasiswa yang hadir jika diketahui BANYAK MAHASISWA YANG HADIR & BANYAK SELURUH MAHASISWA.

# Cara mengerjakkan
mahasiswa_hadir = int(input("Masukkan banyak mahasiswa yang hadir: "))
total_mahasiswa = int(input("Masukkan banyak mahasiswa: "))

# Hasil
persentase_mahasiswa_hadir = (mahasiswa_hadir / total_mahasiswa)
print(f"Persentase mahasiswa yang hadir adalah: {persentase_mahasiswa_hadir:.2%}")
