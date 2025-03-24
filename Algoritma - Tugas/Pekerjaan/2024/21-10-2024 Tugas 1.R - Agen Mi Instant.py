# Dictionary - Harga Mie (Pengganti Konstanta)
harga_mie = {
    "indomie": {"goreng": 60000, "kuah": 50000},
    "sedap": {"goreng": 55000, "kuah": 45000},
    "sarimi": {"goreng": 52000, "kuah": 47000}
}
merk_mie = ["indomie", "sedap", "sarimi"]
jenis_mie = ["goreng", "kuah"]
daftar_pembelian = []

# Variabel Awal.
bonus = "Tidak ada"
diskon = 0
total_harga = 0

# Banner (Abaikan Saja).
print(r"""
  ___                    ___  ____   _____          _              _   
 / _ \                   |  \/  (_) |_   _|        | |            | |  
/ /_\ \ __ _  ___ _ __   | .  . |_    | | _ __  ___| |_ __ _ _ __ | |_ 
|  _  |/ _` |/ _ \ '_ \  | |\/| | |   | || '_ \/ __| __/ _` | '_ \| __|
| | | | (_| |  __/ | | | | |  | | |  _| || | | \__ \ || (_| | | | | |_ 
\_| |_/\__, |\___|_| |_| \_|  |_/_|  \___/_| |_|___/\__\__,_|_| |_|\__|
        __/ |                                                          
       |___/                                                           
""")

# Input 1 - Nama Pembeli.
nama = input("Masukkan Nama Pembeli: ").strip()
while nama == "":
    print("⛔ Nama tidak boleh kosong")
    nama = input("Masukkan Nama Pembeli: ").strip()

# Input 2 - Merk Mie.
while True:
    merk = input("Masukkan merk mie yang ingin dibeli (Indomie, Sedap, Sarimi): ").lower()
    if merk not in merk_mie:
        print("📢 Merk tidak tersedia, silakan coba lagi.")
        continue

    # Input 3 - Jenis Mie.
    while True:
        jenis = str(input(f"Pilih jenis {merk}: Goreng atau Kuah?: ")).lower()
        if jenis not in jenis_mie:
            print("📢 Jenis tidak dikenal, silakan coba lagi")
            continue
        break

    # Input 4 - Jumlah Karton.
    while True:
        try:
            jumlah_karton = int(input("Masukkan Jumlah Karton: "))
            if jumlah_karton <= 0:
                print("🚨 Jumlah karton tidak boleh negatif!")
                continue
            else:
                break
        except ValueError:
            print("⛔ Tolong masukkan angka")

    total = harga_mie[merk][jenis] * jumlah_karton
    print(f"Total pembelian untuk {jumlah_karton} Karton {merk} {jenis} adalah Rp. {total:,}")

    # Memasukkan pembelian ke dalam list.
    daftar_pembelian.append({
    "merk_mie": merk,
    "jenis_mie": jenis,
    "jumlah_karton": jumlah_karton,
    "total": f"{total:,}"
    })

    # Digunakan untuk menjumlahkan semua pembelian (Karton & Total).
    total_harga += total

    # Input Terakhir - Jika ingin mengulangi pembelian.
    ulang = input("Apakah Anda ingin melakukan pembelian lagi? (ya / tidak): ").lower()

    # Jika tidak mengulangi.
    if ulang != "ya":
        print(r"""
  _   _       _          _____               _          _ _             
 | \ | |     | |        |  __ \             | |        | (_)            
 |  \| | ___ | |_ __ _  | |__) |__ _ __ ___ | |__   ___| |_  __ _ _ __  
 | . ` |/ _ \| __/ _` | |  ___/ _ \ '_ ` _ \| '_ \ / _ \ | |/ _` | '_ \ 
 | |\  | (_) | || (_| | | |  |  __/ | | | | | |_) |  __/ | | (_| | | | |
 |_| \_|\___/ \__\__,_| |_|   \___|_| |_| |_|_.__/ \___|_|_|\__,_|_| |_|
""")

        # Menagkap Diskon dan Bonus.
        if total_harga > 2000000:
            bonus = "Jas Hujan"
        elif total_harga > 1000000:
            bonus = "Payung"
        if jumlah_karton > 20:
            diskon = total_harga * 0.10

        # Ringkasan semua pembelian.
        print(f"Ringkasan pembelian Anda:")

        # Menampilkan semua list pembelian.
        for beli in daftar_pembelian:
            print(f" • {beli['merk_mie']} {beli['jenis_mie']} x {beli['jumlah_karton']} = Rp. {beli['total']}")

        # Lain - Lainnya.
        print(f"\nTotal keseluruhan pembelian Anda adalah Rp. {total_harga:,}")
        print(f"Diskon: Rp. {diskon:,.0f}")
        print(f"Bonus: {bonus}")
        print("Terima kasih telah berbelanja!\n")
        break
