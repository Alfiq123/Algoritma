# Buatlah program dengan perulangan untuk studi kasus berikut:
# Sebuah manejemen persewaan gedung memberlakukan biaya sewa gedung dengan data inputan: 
# • Nama Penyewa, 
# • Kategori Gedung, 
# • lama sewa (hari), dan
# • kelebihan jam. 

# Terdapat 3 kategori gedung:
# 1) Gedung Pertemuan (Rapat) dengan harga sewa per hari Rp.300.000, sewa lebih jam sebesar Rp.50.000/jam.
# 2) Gedung Pentas Seni, harga sewa per hari Rp.450.000, harga sewa lebih jam sebesar Rp.80.000.
# 3) Gedung Pernikahan, per hari Rp.600.000, sewa jam sebesar Rp.100.000.

# Potongan biaya sewa akan diberikan kepada penyewa yang lebih dari 3 hari sebesar sebesar 10% dari total sewa. 
# Total Sewa dihitung dari harga sewa per hari jumlah hari sewa. 
# Biaya lebih jam didapat dari harga lebih jam * jumlah jam.

# Sederhananya.

# Input:
# • Nama Penyewa,
# • Kategori Gedung,
# • lama sewa (hari),
# • kelebihan jam.

# Kategori Gedung:
# • Gedung Pertemuan (Rapat).
# • Gedung Pentas Seni.
# • Gedung Pernikahan.

# Gedung Pertemuan (Rapat):
# • Harga sewa per hari Rp.300.000
# • Harga sewa lebih lama Rp.50.000 / jam.

# Gedung Pentas Seni:
# • Harga sewa per hari Rp.450.000
# • Harga sewa lebih lama Rp.80.000 / jam.

# Gedung Pernikahan:
# • Harga sewa per hari Rp.600.000
# • Harga sewa lebih lama Rp.100.000 / jam.

# Perhitungan:
# • Total Sewa: Dihitung dari harga sewa per hari dikali jumlah hari sewa.
# • Biaya Lebih Jam: Dihitung dari harga sewa per jam dikali jumlah jam tambahan.
# • Potongan: Jika lama sewa lebih dari 3 hari, maka akan ada potongan 10% dari total sewa.

# Output:
# • Total biaya yang harus dibayar oleh penyewa setelah dikurangi potongan (jika ada).

kategori_gedung_valid = {"1": "GEDUNG PERTEMUAN", "2": "GEDUNG PENTAS SENI", "3": "GEDUNG PERNIKAHAN"}
potongan = 0

# gedung_valid = {
#     "GEDUNG PERTEMUAN": {"LAMA SEWA": 300000, "LEBIH JAM": 50000},
#     "GEDUNG PENTAS SENI": {"LAMA SEWA": 450000, "LEBIH JAM": 80000},
#     "GEDUNG PERNIKAHAN": {"LAMA SEWA": 600000, "LEBIH JAM": 100000}
# }

#   ___                    _   
#  |_ _| _ _   _ __  _  _ | |_ 
#   | | | ' \ | '_ \| || ||  _|
#  |___||_||_|| .__/ \_,_| \__|
#             |_|              

while True:

    # Input - Nama.
    nama_penyewa = str(input("Masukkan nama penyewa: "))
    # Input - Kategori Gedung.
    print("""
    Kategori Gedung:
        • 1. Gedung Pertemuan (Rapat)
        • 2. Gedung Pentas Seni
        • 3. Gedung Pernikahan
    """)

    while True:
        kategori_gedung = str(input("Masukkan kategori gedung (1 / 2 / 3): ")).upper()
        if kategori_gedung not in kategori_gedung_valid:
            print("❌ Kategori Gedung tidak valid, silakan coba lagi!")
            continue

        # Perhitungan 1. Gedung Pertemuan (Rapat).
        elif kategori_gedung == "1":
            print(f"""
    Gedung Pertemuan (Rapat).
        • Harga sewa per hari: Rp.300.000
        • Harga sewa lebih lama: Rp.50.000 / jam.
    """)
            sewa_per_hari = 300000
            sewa_lebih_lama = 50000
            break

        # Perhitungan 2. Gedung Pentas Seni.
        elif kategori_gedung == "2":
            print(f"""
    Gedung Pentas Seni.
        • Harga sewa per hari: Rp.450.000
        • Harga sewa lebih lama: Rp.80.000 / jam.
    """)
            sewa_per_hari = 450000
            sewa_lebih_lama = 80000
            break

        # Perhitungan 3. Gedung Pernikahan.
        elif kategori_gedung == "3":
            print(f"""
    Gedung Pernikahan.
        • Harga sewa per hari: Rp.600.000
        • Harga sewa lebih lama: Rp.100.000 / jam.
    """)
            sewa_per_hari = 600000
            sewa_lebih_lama = 100000
            break
        else:
            break

    # Input Lama Sewa.
    while True:
        try:
            lama_sewa = int(input("Masukkan lama sewa (hari): "))
        except:
            print("❌ Lama sewa tidak valid, pastikan kamu memasukkan angka")
            continue
        break

    # Input Kelebihan Jam.
    while True:
        try:
            kelebihan_jam = int(input("Masukkan kelebihan jam: "))
        except:
            print("❌ Kelebihan jam tidak valid, pastikan kamu memasukkan angka")
            continue
        break

    #   ___            _     _  _                                 
    #  | _ \ ___  _ _ | |_  (_)| |_  _  _  _ _   __ _  __ _  _ _  
    #  |  _// -_)| '_|| ' \ | ||  _|| || || ' \ / _` |/ _` || ' \ 
    #  |_|  \___||_|  |_||_||_| \__| \_,_||_||_|\__, |\__,_||_||_|
    #                                           |___/             

    # Perhitungan 1. Gedung Pertemuan (Rapat).
    if kategori_gedung == "1":
        print(f"""
    Gedung Pertemuan (Rapat).
        • Harga sewa per hari: Rp.300.000
        • Harga sewa lebih lama: Rp.50.000 / jam.
    """)
        sewa_per_hari = 300000
        sewa_lebih_lama = 50000

    # Perhitungan 2. Gedung Pentas Seni.
    elif kategori_gedung == "2":
        print(f"""
    Gedung Pentas Seni.
        • Harga sewa per hari: Rp.450.000
        • Harga sewa lebih lama: Rp.80.000 / jam.
    """)
        sewa_per_hari = 450000
        sewa_lebih_lama = 80000

    # Perhitungan 3. Gedung Pernikahan.
    elif kategori_gedung == "3":
        print(f"""
    Gedung Pernikahan.
        • Harga sewa per hari: Rp.600.000
        • Harga sewa lebih lama: Rp.100.000 / jam.
    """)
        sewa_per_hari = 600000
        sewa_lebih_lama = 100000

    jumlah_harga_sewa = sewa_per_hari * lama_sewa
    biaya_kelebihan_jam = sewa_lebih_lama * kelebihan_jam

    if lama_sewa > 3:
        potongan = 0.1 * jumlah_harga_sewa

    biaya_yang_harus_dibayar = jumlah_harga_sewa + biaya_kelebihan_jam - potongan

    print(f"""
    ────────────────────────────────
    PT Metropolis Office Solutions
    ────────────────────────────────
    Nama Penyewa: {nama_penyewa}
    Lama Sewa: {lama_sewa}
    Kelebihan Jam: {kelebihan_jam}
    Harga Sewa: Rp.{jumlah_harga_sewa:,.0f}
    Biaya kelebihan Jam: Rp.{biaya_kelebihan_jam:,.0f}
    Potongan: Rp.{potongan:,.0f}
    ================================
    Total Biaya yang harus dibayar: Rp.{biaya_yang_harus_dibayar:,.0f}
    """)

    ulang_lagi = str(input("Apakah anda ingin melakukan transaksi lagi? (ya / tidak): ")).upper()
    if ulang_lagi == "YA" or ulang_lagi == "Y":
        continue
    else:
        print("👋🏻 Terima kasih atas kunjungannya 👋🏻")
    break
