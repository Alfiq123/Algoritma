# Buatlah program untuk menghitung pembayaran pembeli pada agen mie instant.

# Harga mie instant:

# Indomie:
# • Mie Goreng - Per Karton = Rp. 60.000
# • Mie Kuah   - Per Karton = Rp. 50.000

# Mie Sedap:
# • Mie Goreng - Per Karton = Rp. 55.000
# • Mie Kuah   - Per Karton = Rp. 45.000

# Sarimi:
# • Mie Goreng - Per Karton = Rp. 52.000
# • Mie Kuah   - Per Karton = Rp. 47.000

# Potongan harga diberikan jika membeli lebih dari 20 karton, 
# sebesar 10% dari total harga.

# Bonus jas hujan diberikan kepada pembeli yang membayar lebih dari 2 juta, 
# dan bonus payung bagi total bayar lebih dari 1 juta.

# > 20 Karton: 🏷️ Diskon 10% / 0.10
# > 1 juta:    ☂️ Payung
# > 2 juta:    🥼 Jas Hujan

# Konstanta
harga_indomie_goreng = 60000     # Rp. 60.000
harga_indomie_kuah = 50000       # Rp. 50.000

harga_sedap_goreng = 55000   # Rp. 55.000
harga_sedap_kuah = 45000     # Rp. 45.000

harga_sarimi_goreng = 52000      # Rp. 52.000
harga_sarimi_kuah = 47000        # Rp. 47.000

print(r"""
========================================
  ___                    ___  ____      
 / _ \                   |  \/  (_)     
/ /_\ \ __ _  ___ _ __   | .  . |_  ___ 
|  _  |/ _` |/ _ \ '_ \  | |\/| | |/ _ \
| | | | (_| |  __/ | | | | |  | | |  __/
\_| |_/\__, |\___|_| |_| \_|  |_/_|\___|
        __/ |                           
       |___/                            
========================================
""")

# List
merk_mie = ["indomie", "sedap", "sarimi"]
jenis_mie = ["goreng", "kuah"]

# Input
nama = str(input("Masukkan Nama Pembeli: "))

while True:
    merk = str(input("Masukkan merk mie: (Indomie, Sedap, Sarimi): ")).lower()
    if merk in merk_mie:
        break
    else:
        print("📢 Merk tidak tersedia, silakan coba lagi.")

while True:
    jenis = str(input("Masukkan Jenis Mie (Goreng / Kuah): ")).lower()
    if jenis in jenis_mie:
        break
    else:
        print("📢 Jenis tidak tersedia, silakan coba lagi.")

while True:
    try:
        jumlah_karton = int(input("Masukkan Jumlah Karton: "))
    except ValueError:
        print("⛔ Jumlah Karton tidak boleh huruf")
    else:
        break

# Deklarasi Awal
bonus = "Tidak ada"
diskon = 0

# Area Indomie
if merk == "indomie":
    # ✦ Goreng
    if jenis == "goreng":
        harga = harga_indomie_goreng * jumlah_karton
    # ✦ Kuah
    else:
        harga = harga_indomie_kuah * jumlah_karton

# Area Mie Sedap
elif merk == "sedap":
    # ✦ Goreng
    if jenis == "goreng":
        harga = harga_sedap_goreng * jumlah_karton
    # ✦ Kuah
    else:
        harga = harga_sedap_kuah * jumlah_karton

# Area Sarimi
elif merk == "sarimi":
    # ✦ Goreng
    if jenis == "goreng":
        harga = harga_sarimi_goreng * jumlah_karton
    # ✦ Kuah
    else:
        harga = harga_sarimi_kuah * jumlah_karton

# Menagkap Diskon dan Bonus
if jumlah_karton > 20:
    diskon = harga * 0.10
if harga > 1000000:
    bonus = "Payung"
if harga > 2000000:
    bonus = "Jas Hujan"

print(r"""
  _   _       _          _____               _          _ _             
 | \ | |     | |        |  __ \             | |        | (_)            
 |  \| | ___ | |_ __ _  | |__) |__ _ __ ___ | |__   ___| |_  __ _ _ __  
 | . ` |/ _ \| __/ _` | |  ___/ _ \ '_ ` _ \| '_ \ / _ \ | |/ _` | '_ \ 
 | |\  | (_) | || (_| | | |  |  __/ | | | | | |_) |  __/ | | (_| | | | |
 |_| \_|\___/ \__\__,_| |_|   \___|_| |_| |_|_.__/ \___|_|_|\__,_|_| |_|
""")

print(f"""
===================================
Nama Pembeli: {nama}
Merk mie yang dipilih: {merk}
Jenis mie yang dipilih: {jenis}
Jumlah Karton: {jumlah_karton} kotak
===================================
Harga Awal Rp. {harga:,.0f}
Diskon: Rp. {diskon:,.0f}
Harga dikurangi Diskon: Rp. {harga:,.0f} - Rp. {diskon:,.0f}
===================================
Total Harga: Rp. {harga - diskon:,.0f}
Bonus: {bonus}
""")
