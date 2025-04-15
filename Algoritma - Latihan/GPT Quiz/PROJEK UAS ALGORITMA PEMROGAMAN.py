# NAMA  :AGASTYA SABIRA ANWAR
# NPM   :2413020091
#KELAS  :1A
#MATKUL :ALGORITMA PEMROGAMAN

# Sambutan.
print("SELAMAT DATANG DITOKO PETANI SEJAHTERA")
print("KAMI MENYEDIAKAN SEGALA JENIS PUPUK\n")

# Meminta Nama dari User.
NamaPembeli = input("Silakan Masukan Nama: ").upper()

# Pilihan Pupuk.
# 🔧 Kodenya bisa dibuat seperti ini.
print("""
1. PUPUK NPK PHONSKA   Kering = Rp. 150.000 / 50 kg   ││   Cair = Rp. 50.000  / liter
2. PUPUK UREA          Kering = Rp. 120.000 / 50 kg   ││   Cair = Rp. 40.000  / liter
3. PUPUK DOLOMITE      Kering = Rp. 100.000 / 50 kg   ││   Cair = Rp. 70.000  / liter
4. PUPUK ZK PETRO      Kering = Rp. 805.000 / 50 kg   ││   Cair = Rp. 125.000 / liter
5. PUPUK MUTIARA       Kering = Rp. 365.000 / 50 kg   ││   Cair = Rp. 25.000  / liter
""")

# Meminta Pilihan Produk Dari User.
merk = int(input("Silakan Pilih Merk Pupuk (1, 2, 3, 4, 5) = "))
# 🔧 Tambahan Pengulangan (Jika Pengguna Salah Memilih.)
while merk not in (1, 2, 3, 4, 5):
    print("Pilihan Tidak Ada, Silakan Coba Kembali.")
    merk = int(input("Silakan Pilih Merk Pupuk (1, 2, 3, 4, 5) = "))

jenis = str(input("Silakan Pilih Jenis Pupuk [Kering (K) / Cair (C)] = ")).upper()
# 🔧 Tambahan Pengulangan (Jika Pengguna Salah Memilih.)
while jenis not in ("K", "C"):
    print("Pilihan Tidak Ada, Silakan Coba Kembali.")
    jenis = str(input("Silakan Pilih Jenis Pupuk [Kering (K) / Cair (C)] = ")).upper()

jumlah = int(input("Silakan Masukan jumlah Barang = "))

# Menghitung Harga.
if merk == 1:
    if jenis == "K":
        HARGA = 150000
        NamaBarang = "PUPUK NPK PHONSKA Kering 50kg"
    elif jenis == "C":
        HARGA = 50000
        NamaBarang = "PUPUK NPK PHONSKA Cair Per 1 liter"

elif merk == 2:
    if jenis == "K":
        HARGA = 120000
        NamaBarang = "PUPUK UREA Kering 50kg"
    elif jenis == "C":
        HARGA = 40000
        NamaBarang = "PUPUK UREA CAIR Per 1 liter"

elif merk == 3:
    if jenis == "K":
        HARGA = 100000
        NamaBarang = "PUPUK DOLOMITE Kering 50kg"
    elif jenis == "C":
        HARGA = 47000
        NamaBarang = "PUPUK DOLOMITE Cair Per 1 liter"

elif merk == 4:
    if jenis == "K":
        HARGA = 805000
        NamaBarang = "PUPUK ZK PETRO Kering 50kg"
    elif jenis == "C":
        HARGA = 125000
        NamaBarang = "PUPUK ZK PETRO CAIR Per 1 liter"

elif merk == 5:
    if jenis == "K":
        HARGA = 365000
        NamaBarang = "PUPUK MUTIARA Kering 50kg"
    elif jenis == "C":
        HARGA = 25000
        NamaBarang = "PUPUK MUTIARA Cair Per 1 liter"

# hitung hasil
HargaAwal = HARGA * jumlah

# cek ptongan
if jumlah > 20 :
    diskon = (10 / 100) * HargaAwal
    TotalHarga = HargaAwal - diskon
else :
    diskon = 0
    TotalHarga = HargaAwal

# bonus
if TotalHarga >= 1000000 and TotalHarga < 2000000 :
    bonus = "Bonus 15 bibit cabai"

elif TotalHarga >= 2000000:
    bonus = "Bonus Kaos dari PETANI SEJAHTERA"

else :
    bonus = "Tidak Ada Bonus"

# Hasil.
print(f"""
────────────────────────────
Nama Pembeli : {NamaPembeli}
{NamaBarang} = {jumlah} barang
──────────────────────────
Harga = Rp. {HargaAwal:,.0f}
Diskon = Rp. {diskon:,.0f}
────────────────────────────
Total Harga = Rp. {TotalHarga:,.0f}
────────────────────────────
{bonus}
""")