# Buatlah program untuk menghitung jumlah pembayaran gaji dengan input nama, status (K/TK), golongan pegawai, jumlah anak.
# Gaji pokok golongan A=3 jt, gol B=3,5 jt, gol. C=4 jt.
# Tunjangan istri diberikan sebesar 10% dari gaji pokok, dan tunjangan anak diberikan sebesar 5% dari gaji pokok sampai anak ke-2. 
# Tunjangan beras diberikan kepada anggota keluarga yang menjadi tanggungan, dalam bentuk rupiah.
# Hitung jumlah gaji total yang diterima pegawai.

# 👩‍❤️‍👨️ K = Kawin
# 👦️ TK = Tidak Kawin

# 💵️ A = Rp. 3.000.000
# 💴️ B = Rp. 3.500.000
# 💶️ C = Rp. 4.000.000

# 👩️ Tunjangan Istri = Gaji Pokok * 10%
# 👶️ Tunjangan Anak = Gaji Pokok * 5% * Jumlah Anak
# 🌾️ Tunjangan Beras = (Istri + Jumlah Anak) * Rp. 75.000
# 🍚️ Tunjangan Beras Tanpa Istri = Jumlah Anak * Ro. 75.000

# 🔧️ Operator = +, -, *, /, <, >, <=, >=, ==

# Input Karyawan
nama = input("Masukkan Nama: ")
status = input("Masukkan Status (K/TK): ")
golongan = input("Masukkan Golongan Pegawai (A/B/C): ")
jumlah_anak = int(input("Masukkan Jumlah Anak: "))

# Mencari Gaji Pokok Berdasarkan Golongan
if golongan == "A":
    gaji_pokok = 3000000
elif golongan == "B":
    gaji_pokok = 3500000
elif golongan == "C":
    gaji_pokok = 4000000
else:
    print("Golongan Karyawan Tidak Valid.")
    exit()

# 👩️ Tunjangan Istri ?
tunjangan_istri = 0
if status == "K":
    tunjangan_istri = gaji_pokok * 0.10

# 👶️ Tunjangan Anak ??
tunjangan_anak = 0
if jumlah_anak > 0 and jumlah_anak <= 2:
    tunjangan_anak = gaji_pokok * 0.05 * jumlah_anak

# 🌾️ Tunjangan Beras Dalam Bentuk Rupiah ???
# Anggap saja harga beras 5kg = Rp. 75.000 (Mungkin...)
tunjangan_beras = (1 + jumlah_anak) * 75000 if status == "K" else jumlah_anak * 75000

# 💰️ Menjumlahkan Gaji Karyawan
total_gaji = gaji_pokok + tunjangan_istri + tunjangan_anak + tunjangan_beras

# Real Total Gaji Karyawan
print("=====================================")
print("Rincian Gaji Karyawan")
print("=====================================")
print("Nama Karyawan:", nama)
print(f"Gaji Pokok: Rp. {gaji_pokok:,.0f}")
print(f"Tunjangan Istri: Rp. {tunjangan_istri:,.0f}")
print(f"Tunjangan Anak: Rp. {tunjangan_anak:,.0f}")
print(f"Tunjangan Beras: Rp. {tunjangan_beras:,.0f}")
print("=====================================")
print(f"Total Gaji: Rp. {total_gaji:,.0f}")
print("=====================================")
