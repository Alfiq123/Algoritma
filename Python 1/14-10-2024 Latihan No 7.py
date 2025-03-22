# Persentase mahasiswa yang hadir jika diketahui BANYAK MAHASISWA YANG HADIR & BANYAK SELURUH MAHASISWA.

# Input
# mahasiswa_hadir = int(input("Masukkan banyak mahasiswa yang hadir: "))
# total_mahasiswa = int(input("Masukkan banyak mahasiswa: "))

print("🎓️ ===== Menghitung persentase mahasiswa yang hadir ===== 🎓️")

# Input mahasiswa yang hadir.
while True:
    try:
        mahasiswa_hadir = int(input("Masukkan banyak mahasiswa yang hadir: "))
    except ValueError:
        print("🚩 Kamu memasukkan huruf atau karakter lain 🚩")
        continue
    else:
        break

# Input total dari mahasiswa.
while True:
    try:
        total_mahasiswa = int(input("Masukkan banyaknya mahasiswa: "))
    except ValueError:
        print("🚩 Kamu memasukkan huruf atau karakter lain 🚩")
        continue
    else:
        break

# Pengerjaan.
persentase_mahasiswa_hadir = (mahasiswa_hadir / total_mahasiswa)

# Output.
print("🏆 ===== Hasil ===== 🏆")
print(f"Banyak mahasiswa yang hadir: {mahasiswa_hadir} orang")
print(f"Banyak mahasiswa: {total_mahasiswa} orang")
print(f"Persentase mahasiswa yang hadir adalah: {persentase_mahasiswa_hadir:.2%}")
