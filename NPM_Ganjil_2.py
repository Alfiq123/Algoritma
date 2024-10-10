# Buatlah program untuk menghitung gaji karyawan PT.SUFI.
# Jika terdapat 3 kategori karyawan:
# 1. Karyawan bagian Produksi dengan Gaji Rp.2.500.000, upah lembur per jam sebesar Rp.25.000.
# 2. Karyawan bagian Packing dengan Gaji Rp.2.450.000, upah lembur per jam sebesar Rp.20.000.
# 3. Karyawan bagian Distribusi dengan Gaji Rp.2.350.000, upah lembur per jam sebesar Rp.25.000.

# Data inputan nama pegawai, status, kategori bagian, jumlah anak, dan jumlah jam lembur, dengan ketentuan:
# a. Tunjangan istri diberikan sebesar 15% dari gajipokok,
# b. Tunjangan anak akan diberikan sampai anak ke 3, sebesar 10% dari total gajipokok.
# c. Gaji lembur dihitung dr upah lembur*jumlahjam lembur.
# d. Uang transport akan diberikan kepada pegawai yang lembur lebih dari 10 jam dalam sebulan sebesar 10% dari Gaji lembur.
# e. Gunakan constanta untuk tunjangan istri dan anak.

# 🧑‍🏭️ Karyawan Produksi : Rp. 2.500.000 * (Rp. 25.000 per jam)
# 🧳️ Karyawan Packing : Rp. 2.450.000 * (Rp. 20.000 per jam)
# 📦️ Karyawan Distribusi : Rp. 2.350.000 * (Rp. 25.000 per jam)

# 👩‍🦰️ Tunjangan Istri : 15% * Gaji Pokok
# 🧒️ Tunjangan Anak : 10% * Gaji Pokok * Jumlah Anak (Maksimal 3)
# ⏱️ Gaji Lembur : Upah Lembur * Jumlah Jam Lembur
# 🚗️ Uang Transport : 10% * Upah Lembur (Jike bekerja lebih dari 10 jam)
# 💰️ Total Gaji = Gaji Pokok + Tunjangan Istri + Tunjangan Anak + Gaji Lembur + Uang Transport

# 🔧️ Operator : <, >, <=, >=, ==, +, -, *, /

# Konstanta (Data yang tidak dapat diubah)
tunjangan_istri = 0.15  # 15%
tunjangan_anak = 0.10   # 10%

# Input-an Pegawai
nama_pegawai = input("Masukkan nama pegawai: ")
status = input("Masukkan status (menikah/belum menikah): ")
kategori_bagian = input("Masukkan kategori bagian (produksi/packing/distribusi): ")
jumlah_anak = int(input("Masukkan jumlah anak: "))
jumlah_jam_lembur = int(input("Masukkan jumlah jam lembur: "))

# Menghitung gaji pokok dari karyawan PT.SUFI
# 🧑‍🏭️ Karyawan Produksi
if kategori_bagian == "produksi":
    gaji_pokok = 2500000
    upah_lembur = 25000
# 🧳️ Karyawan Packing
elif kategori_bagian == "packing":
    gaji_pokok = 2450000
    upah_lembur = 20000
# 📦️ Karyawan Distribusi
elif kategori_bagian == "distribusi":
    gaji_pokok = 2350000
    upah_lembur = 25000
else:
    print("Kategori bagian tidak valid.")
    exit()

# 👩‍🦰️ Tunjangan istri (Jika menikah)
if status == "menikah":
    tunjangan_istri = gaji_pokok * tunjangan_istri

# 🧒️ Tunjangan anak (Jika punya & Kurang dari 3)
if jumlah_anak > 0 and jumlah_anak <= 3:
    tunjangan_anak = gaji_pokok * tunjangan_anak * jumlah_anak

# ⏱️ Mencari upah lembur
gaji_lembur = upah_lembur * jumlah_jam_lembur

# 🚗️ Memperkirakan uang transport
uang_transport = 0
if jumlah_jam_lembur > 10:
    uang_transport = gaji_lembur * 0.10

# Total Gaji Karyawan PT.SUFI
total_gaji = gaji_pokok + tunjangan_istri + tunjangan_anak + gaji_lembur + uang_transport

# Output
print("-------------------------------------")
print("Rincian Gaji Karyawan PT.SUFI")
print("-------------------------------------")
print("Nama Pegawai:", nama_pegawai)
print(f"Gaji Pokok: Rp. {gaji_pokok:,.0f}")
print(f"Tunjangan Istri: Rp. {tunjangan_istri:,.0f}")
print(f"Tunjangan Anak: Rp. {tunjangan_anak:,.0f}")
print(f"Gaji Lembur: Rp. {gaji_lembur:,.0f}")
print(f"Uang Transport: Rp. {uang_transport:,.0f}")
print("-------------------------------------")
print(f"Total Gaji: Rp. {total_gaji:,.0f}")
print("-------------------------------------")
