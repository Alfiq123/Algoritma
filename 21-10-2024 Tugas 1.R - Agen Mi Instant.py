# Kamus - Harga Mie
harga_mie = {
    "indomie": {"goreng": 60000, "kuah": 50000},
    "sedap": {"goreng": 55000, "kuah": 45000},
    "sarimi": {"goreng": 52000, "kuah": 47000}
}
merk_mie = ["indomie", "sedap", "sarimi"]
jenis_mie = ["goreng", "kuah"]

# Deklarasi Variabel.
bonus = "Tidak ada"
diskon = 0
total_harga = 0

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
nama = str(input("Masukkan Nama Pembeli: "))
while nama == "":
    print("⛔ Nama tidak boleh kosong")
    nama = str(input("Masukkan Nama Pembeli: "))

# Input 2 - Merk Mie.
while nama != "":
    merk = input("Masukkan merk mie yang ingin dibeli (Indomie, Sedap, Sarimi): ").lower()
    if merk not in merk_mie:
        print("📢 Merk tidak tersedia, silakan coba lagi.")
    else:
        break
    
# Input 3 - Jenis Mie.
while merk in merk_mie:
    jenis = str(input("Masukkan Jenis Mie (Goreng / Kuah): ")).lower()
    if jenis not in jenis_mie:
        print("📢 Jenis tidak dikenal, silakan coba lagi")
    else:
        break
    
# Input 4 - Jumlah Karton.
while jenis in jenis_mie:
    try:
        jumlah_karton = int(input("Masukkan Jumlah Karton: "))
        if jumlah_karton <= 0:
            print("🚨 Jumlah karton tidak boleh negatif!")
            continue
        else:
            break
    except ValueError:
        print("⛔ Tolong masukkan angka")
