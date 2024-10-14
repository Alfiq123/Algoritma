# A = [M = A] + [N = A]
# S = [M = S] + [N = A]
# S = [M = A] * [M = S] + [N ≠ A]
# B = [M = B] + [N = B]
# DA = [M = B] + [N ≠ B] + [N = A]
# DS = [M = B] + [N ≠ B] + [N = S]

# Keterangan:
# S = Nilai Syarat Penjurusan
# N = Nilai Siswa
# M = Jurusan yang diminati siswa
# A = Jurusan IPA
# S = Jurusan IPS
# B = Jurusan Bahasa
# DA = Disarankan Jurusan IPA
# DS = Disarankan Jurusan IPS
# DB = Disarankan Jurusan Bahasa

# Syarat IPA:
# Matematika = 80
# Biologi    = 78
# Fisika     = 78
# Kimia      = 78

# Syarat IPS:
# Matematika = 80
# Geografi   = 78
# Ekonomi    = 80
# Sosiologi  = 78

# Syarat Bahasa:
# Matematika     = 75
# Bhs. Indonesia = 80
# Bhs. Inggris   = 78
# Bhs. Lain      = 75

# Input Siswa
minat_siswa = str(input("Masukkan Minat Siswa: ")).upper

nilai_matematika = int(input("Masukkan Nilai Matematika: "))

nilai_biologi = int(input("Masukkan Nilai Biologi: "))
nilai_fisika = int(input("Masukkan Nilai Fisika: "))
nilai_kimia = int(input("Masukkan Nilai Kimia: "))

nilai_sosiologi = int(input("Masukkan Nilai Sosiologi: "))
nilai_geografi = int(input("Masukkan Nilai Geografi: "))
nilai_ekonomi = int(input("Masukkan Nilai Ekonomi: "))

nilai_bhs_indonesia = int(input("Masukkan Nilai Bhs. Indonesia: "))
nilai_bhs_inggris = int(input("Masukkan Nilai Bhs. Inggris: "))
nilai_bhs_lain = int(input("Masukkan Nilai Bhs. Lain: "))

# Jika minat IPA & Nilai IPA
if minat_siswa == "IPA" and nilai_matematika  >= 80 and nilai_biologi >= 78 and nilai_fisika >= 78 and nilai_kimia >= 78:
    print("SELAMAT, KAMU MASUK IPA")

# Jika minat IPA & Nilai IPS
if minat_siswa == "IPA" and nilai_matematika >= 80 and nilai_geografi >= 78 and nilai_ekonomi >= 80 and nilai_sosiologi >= 78:
    print("NILAI KAMU COCOK DI IPS")

# Jika minat IPS & Nilai IPS
elif minat_siswa == "IPS" and nilai_matematika >= 80 and nilai_geografi >= 78 and nilai_ekonomi >= 80 and nilai_sosiologi >= 78:
    print("SELAMAT, KAMU MASUK IPS")

# Jika minat IPS & Nilai IPA
elif minat_siswa == "IPS" and nilai_matematika >= 80 and nilai_biologi >=78 and nilai_fisika >= 78 and nilai_kimia >= 78:
    print("NILAI KAMU COCOK DI IPA")

# Jika minat Bahasa & Nilai Bahasa
elif  minat_siswa == "Bahasa" and nilai_matematika >= 75 and nilai_bhs_indonesia >= 80 and nilai_bhs_inggris >= 78 and nilai_bhs_lain >= 75:
    print("SELAMAT, KAMU MASUK BAHASA")

else:
    print("MAAF, KAMU TIDAK MASUK KE JURUSAN APAPUN")

