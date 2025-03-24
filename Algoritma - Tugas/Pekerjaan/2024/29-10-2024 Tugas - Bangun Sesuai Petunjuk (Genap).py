import math

# Tuple - List Bangun.
bangun = ("DATAR", "RUANG")
bangun_datar = ("1", "JAJAR GENJANG", "2", "TRAPESIUM", "3", "PERSEGI LIMA")
bangun_ruang = ("1", "KUBUS", "2", "TABUNG", "3", "LIMAS")

# Mengakali "Undefined Variable"
input_bangun_datar = ""
input_bangun_ruang = ""

print(r"""
  ___                                     _  _  _  _                       ___                               
 | _ \ _ _  ___  __ _  _ _  __ _  _ __   | || |(_)| |_  _  _  _ _   __ _  | _ ) __ _  _ _   __ _  _  _  _ _  
 |  _/| '_|/ _ \/ _` || '_|/ _` || '  \  | __ || ||  _|| || || ' \ / _` | | _ \/ _` || ' \ / _` || || || ' \ 
 |_|  |_|  \___/\__, ||_|  \__,_||_|_|_| |_||_||_| \__| \_,_||_||_|\__, | |___/\__,_||_||_|\__, | \_,_||_||_|
                |___/                                              |___/                   |___/             
""")

input_bangun = str(input("Masukkan pilihan bangun - Datar / Ruang: ")).upper()
while input_bangun not in bangun:
    print("📢 Pilihan tidak ada, silakan pilih kembali!")
    input_bangun = str(input("Masukkan pilihan bangun - Datar / Ruang: ")).upper()

if input_bangun == "DATAR":
    print(r"""
  ___                                 ___         _              
 | _ ) __ _  _ _   __ _  _  _  _ _   |   \  __ _ | |_  __ _  _ _ 
 | _ \/ _` || ' \ / _` || || || ' \  | |) |/ _` ||  _|/ _` || '_|
 |___/\__,_||_||_|\__, | \_,_||_||_| |___/ \__,_| \__|\__,_||_|  
                  |___/                                          """)

    print(r"""
✦ MASUKKAN PILIHAN - BANGUN DATAR ✦
   1. Jajar Genjang
   2. Trapesium
      • Beraturan (sama miring),
      • Tidak beraturan / Sisi samping yang satu tegak lurus)
   3. Persegi Lima
""")

while input_bangun == "DATAR":
    input_bangun_datar = str(input("Masukkan Pilihan Bangun Datar: ")).upper()
    if input_bangun_datar in bangun_datar:
        break
    else:
        print("📢 Bangun datar tidak ada yang terpilih, silakan pilih kembali!")
        continue

# Jajar Genjang.
if input_bangun_datar == "JAJAR GENJANG":
    print(r"""
     _         _               ___              _                   
  _ | | __ _  (_) __ _  _ _   / __| ___  _ _   (_) __ _  _ _   __ _ 
 | || |/ _` | | |/ _` || '_| | (_ |/ -_)| ' \  | |/ _` || ' \ / _` |
  \__/ \__,_|_/ |\__,_||_|    \___|\___||_||_|_/ |\__,_||_||_|\__, |
            |__/                             |__/             |___/ 
    """)

# Input - Alas Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "1":
    try:
        alas_jajar_genjang = float(input("Masukkan Alas Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Tinggi Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "1":
    try:
        tinggi_jajar_genjang = float(input("Masukkan Tinggi Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Atas Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "1":
    try:
        satas_jajar_genjang = float(input("Masukkan Sisi Atas Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Bawah Genjang.
while input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "1":
    try:
        ssamping_jajar_genjang = float(input("Masukkan Sisi Samping Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Output - Jajar Genjang.
if input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "1":

    print(f"""
======= Luas Jajar Genjang =======
Alas Jajar Genjang: {alas_jajar_genjang:,.2f} cm
Tinggi Jajar Genjang: {tinggi_jajar_genjang:,.2f} cm
Rumus Luas Jajar Genjang: {alas_jajar_genjang:,.2f} cm x {tinggi_jajar_genjang:,.2f} cm
Luas Jajar Genjang: {alas_jajar_genjang * tinggi_jajar_genjang:,.2f} cm²""")

    print(f"""
======= Keliling Jajar Genjang =======
Sisi Atas Jajar Genjang: {satas_jajar_genjang:,.2f} cm
Sisi Bawah Jajar Genjang: {ssamping_jajar_genjang:,.2f} cm
Rumus Keliling Jajar Genjang: 2 x ({satas_jajar_genjang:,.2f} cm + {ssamping_jajar_genjang:,.2f}) cm
Keliling Jajar Genjang: {2 * (satas_jajar_genjang + ssamping_jajar_genjang):,.2f} cm""")

# Trapesium.
if input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2":
    print(r"""
  _____                      _            
 |_   _| _ __ _ _ __  ___ __(_)_  _ _ __  
   | || '_/ _` | '_ \/ -_|_-< | || | '  \ 
   |_||_| \__,_| .__/\___/__/_|\_,_|_|_|_|
               |_|                        
""")
    
    print(r"""
1. Trapesium Beraturan
2. Trapesium Tidak Beraturan
""")

list_trapesium = {"1": "Trapesium Beraturan", "2": "Trapesium Tidak Beraturan"}
rumus_trapesium = ("LUAS", "KELILING")

# Input Jenis Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2":
    jenis_trapesium = str(input("Masukkan Jenis Trapesium (1 / 2): ")).upper()
    if jenis_trapesium in list_trapesium:
        print(f"「 {list_trapesium[jenis_trapesium]} 」")
        break
    else:
        print("📢 Masukkan Jenis Trapesium (Angka!")
        continue

# Input Rumus Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2":
    rumus_trapesium = str(input("Masukkan Rumus Trapesium (Luas / Keliling): ")).upper()
    if rumus_trapesium == "LUAS" or rumus_trapesium == "KELILING":
        print(f"「 {rumus_trapesium} 」")
        break
    else:
        print("🚩 Masukkan Luas atau Keliling")
        continue

#   _                  _____                      _            
#  | |  _  _ __ _ ___ |_   _| _ __ _ _ __  ___ __(_)_  _ _ __  
#  | |_| || / _` (_-<   | || '_/ _` | '_ \/ -_|_-< | || | '  \ 
#  |____\_,_\__,_/__/   |_||_| \__,_| .__/\___/__/_|\_,_|_|_|_|
#                                   |_|                        

# Input - Alas Atas Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "LUAS":
    try:
        alas_atas_trapesium = float(input("Masukkan Alas Atas Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Alas Bawah Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "LUAS":
    try:
        alas_bawah_trapesium = float(input("Masukkan Alas Bawah Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Tinggi Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "LUAS":
    try:
        tinggi_trapesium = float(input("Masukkan Tinggi Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Output - Luas Trapesium
if input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "LUAS":
    print(f"""
======= Luas {list_trapesium[jenis_trapesium]} =======
Alas Atas Trapesium: {alas_atas_trapesium:,.2f} cm
Alas Bawah Trapesium: {alas_bawah_trapesium:,.2f} cm
Tinggi Trapesium: {tinggi_trapesium:,.2f} cm
Rumus Luas Trapesium: 1/2 x ({alas_atas_trapesium:,.2f} cm + {alas_bawah_trapesium:,.2f} cm) x {tinggi_trapesium:,.2f} cm
Luas Trapesium: {0.5 * (alas_atas_trapesium + alas_bawah_trapesium) * tinggi_trapesium:,.2f} cm²
""")

#   _  __    _ _ _ _             _____                      _            
#  | |/ /___| (_) (_)_ _  __ _  |_   _| _ __ _ _ __  ___ __(_)_  _ _ __  
#  | ' </ -_) | | | | ' \/ _` |   | || '_/ _` | '_ \/ -_|_-< | || | '  \ 
#  |_|\_\___|_|_|_|_|_||_\__, |   |_||_| \__,_| .__/\___/__/_|\_,_|_|_|_|
#                        |___/                |_|                        

# Input - Sisi AB Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_ab = float(input("Masukkan Sisi Trapesium AB: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi BC Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_bc = float(input("Masukkan Sisi Trapesium BC: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi CD Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_cd = float(input("Masukkan Sisi Trapesium CD: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi DA Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_da = float(input("Masukkan Sisi Trapesium DA: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Output - Keliling Trapesium
if input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "2" and rumus_trapesium == "KELILING":
    print(f"""
======= Keliling {list_trapesium[jenis_trapesium]} =======
Trapesium Sisi AB: {sisi_trapesium_ab:,.2f} cm
Trapesium Sisi BC: {sisi_trapesium_bc:,.2f} cm
Trapesium Sisi CD: {sisi_trapesium_cd:,.2f} cm
Trapesium Sisi DA: {sisi_trapesium_da:,.2f} cm
Rumus Keliling Trapesium: {sisi_trapesium_ab:,.2f} cm + {sisi_trapesium_bc:,.2f} cm + {sisi_trapesium_cd:,.2f} cm + {sisi_trapesium_da:,.2f} cm
Keliling Trapesium: {sisi_trapesium_ab + sisi_trapesium_bc + sisi_trapesium_cd + sisi_trapesium_da:,.2f} cm
""")

if input_bangun_datar == "PERSEGI LIMA" or input_bangun_datar == "3":
    print(r"""
  ___                           _   _     _              
 | _ \ ___  _ _  ___ ___  __ _ (_) | |   (_) _ __   __ _ 
 |  _// -_)| '_|(_-</ -_)/ _` || | | |__ | || '  \ / _` |
 |_|  \___||_|  /__/\___|\__, ||_| |____||_||_|_|_|\__,_|
                         |___/                           
""")

# Input - Sisi Persegi Lima.
while input_bangun_datar == "PERSEGI LIMA" or input_bangun_datar == "3":
    try:
        sisi_persegi_lima = float(input("Masukkan sisi persegi: "))

        print(f"""
======= Luas Persegi Lima =======
Sisi Persegi Lima adalah: {sisi_persegi_lima:,.2f} cm
Rumus Luas Persegi Lima adalah: (5/4) x {sisi_persegi_lima:,.2f} cm x {sisi_persegi_lima:,.2f} x tan(54°) cm
Luas Persegi Lima adalah: {(5/4) * sisi_persegi_lima ** 2 * math.tan(math.radians(54)):,.2f} cm²""")

        print(f"""
======= Keliling Persegi Lima =======
Sisi Persegi Lima adalah: {sisi_persegi_lima:,.2f} cm
Rumus Keliling Persegi Lima adalah: 5 x {sisi_persegi_lima:,.2f} cm
Keliling Persegi Lima adalah: {5 * sisi_persegi_lima:,.2f} cm
""")
        break

    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

if input_bangun == "RUANG":
    print(r"""
  ___                                 ___                         
 | _ ) __ _  _ _   __ _  _  _  _ _   | _ \ _  _  __ _  _ _   __ _ 
 | _ \/ _` || ' \ / _` || || || ' \  |   /| || |/ _` || ' \ / _` |
 |___/\__,_||_||_|\__, | \_,_||_||_| |_|_\ \_,_|\__,_||_||_|\__, |
                  |___/                                     |___/ 
""")
    print(r"""
✦ BANGUN RUANG - MASUKKAN PILIHAN ✦
   1. Kubus
   2. Tabung
   3. Limas
      • Limas Segi Empat
      • Limas Segi Lima
      • Limas Segi Enam
""")

while input_bangun == "RUANG":
    input_bangun_ruang = str(input("Masukkan Pilihan Bangun Ruang: ")).upper()
    if input_bangun_ruang in bangun_ruang:
        break
    else:
        print("📢 Bangun Ruang tidak ada yang terpilih, silakan pilih kembali!")
        continue

# Kubus.
if input_bangun_ruang == "KUBUS" or input_bangun_ruang == "1":
    print(r"""
  _  __      _              
 | |/ /_  _ | |__  _  _  ___
 | ' <| || || '_ \| || |(_-<
 |_|\_\\_,_||_.__/ \_,_|/__/
                            
""")

# Sisi Kubus.
while input_bangun_ruang == "KUBUS" or input_bangun_ruang == "1":
    try:
        sisi_kubus = float(input("Masukkan Sisi Kubus: "))

        print(f"""
======= Luas Permukaan Kubus =======
Sisi Kubus: {sisi_kubus:,.2f} cm
Rumus Luas Permukaan Kubus: 6 x {sisi_kubus:,.2f} cm x {sisi_kubus:,.2f} cm
Luas Permukaan Kubus: {6 * (sisi_kubus ** 2):,.2f} cm²

======= Volume Kubus =======
Sisi Kubus: {sisi_kubus:,.2f} cm
Rumus Volume Kubus: {sisi_kubus:,.2f} cm x {sisi_kubus:,.2f} cm x {sisi_kubus:,.2f} cm
Luas Permukaan Kubus: {sisi_kubus ** 3:,.2f} cm³
""")

        break
    except ValueError:
        print("📌 Sisi Tidak Valid, silakan coba lagi!")
        continue

# Tabung.
if input_bangun_ruang == "TABUNG" or input_bangun_ruang == "2":
    print(r"""
  _____       _                      
 |_   _|__ _ | |__  _  _  _ _   __ _ 
   | | / _` || '_ \| || || ' \ / _` |
   |_| \__,_||_.__/ \_,_||_||_|\__, |
                               |___/ 
""")

# Jari-Jari Tabung.
while input_bangun_ruang == "TABUNG" or input_bangun_ruang == "2":
    try:
        jari_tabung = float(input("Masukkan Jari-Jari Tabung: "))
        break
    except ValueError:
        print("🔥 Jari-Jari tidak dikenal, silakan coba lagi!")
        continue

# Tinggi Tabung.
while input_bangun_ruang == "TABUNG" or input_bangun_ruang == "2":
    try:
        tinggi_tabung = float(input("Masukkan Tinggi Tabung: "))
        break
    except ValueError:
        print("🔥 Tinggi tidak dikenal, silakan coba lagi!")
        continue

# Output -  Tabung
if input_bangun_ruang == "TABUNG" or input_bangun_ruang == "2":
    print(f"""
======= Luas Permukaan Tabung =======
Jari-Jari Tabung: {jari_tabung:,.2f} cm
Tinggi Tabung: {tinggi_tabung:,.2f} cm
Rumus Luas Permukaan Tabung: 2 x π x {jari_tabung:,.2f} x ({jari_tabung:,.2f} cm + {tinggi_tabung:,.2f} cm)
Luas Permukaan Tabung: {2 * math.pi * jari_tabung * (jari_tabung + tinggi_tabung):,.2f} cm²

======= Volume Tabung =======
Jari-Jari Tabung: {jari_tabung:,.2f} cm
Tinggi Tabung: {tinggi_tabung:,.2f} cm
Rumus Volume Tabung: π x {jari_tabung:,.2f} cm x {jari_tabung:,.2f} cm x {tinggi_tabung:,.2f} cm
Volume Tabung: {math.pi * jari_tabung ** 2 * tinggi_tabung:,.2f} cm³
""")

# Limas.
if input_bangun_ruang == "LIMAS" or input_bangun_ruang == "3":
    print(r"""
  _     _                  
 | |   (_) _ __   __ _  ___
 | |__ | || '  \ / _` |(_-<
 |____||_||_|_|_|\__,_|/__/
                           
""")

    print(r"""
1. Limas Segi Empat    3. Limas Segi Enam
2. Limas Segi Lima
""")

list_limas = {"1": "Limas Segi Empat", "2": "Limas Segi Lima", "3": "Limas Segi Enam"}

# Input Jenis Limas.
while input_bangun_ruang == "PRISMA" or input_bangun_ruang == "3":
    jenis_limas = str(input("Masukkan Jenis Limas (1 / 2 / 3): ")).upper()
    if jenis_limas in list_limas:
        print(f"「 {list_limas[jenis_limas]} 」")
        break
    else:
        print("📢 Masukkan Jenis Limas!")
        continue

# Luas Alas Limas.
while input_bangun_ruang == "LIMAS" or input_bangun_ruang == "3":
    try:
        luas_alas_limas = float(input("Masukkan Luas Alas Limas: "))
        break
    except ValueError:
        print("📌 Luas Alas Tidak Valid, silakan coba lagi!")
        continue

# Keliling Alas Limas.
while input_bangun_ruang == "LIMAS" or input_bangun_ruang == "3":
    try:
        keliling_alas_limas = float(input("Masukkan Keliling Alas Limas: "))
        break
    except ValueError:
        print("📌 Keliling Alas Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Sisi Tegak Limas.
while input_bangun_ruang == "LIMAS" or input_bangun_ruang == "3":
    try:
        sisi_tegak_limas = float(input("Masukkan Tinggi Sisi Tegak Limas: "))
        break
    except ValueError:
        print("📌 Tinggi Sisi Tegak Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Limas.
while input_bangun_ruang == "LIMAS" or input_bangun_ruang == "3":
    try:
        tinggi_limas = float(input("Masukkan Tinggi Limas: "))
        break
    except ValueError:
        print("📌 Tinggi Tidak Valid, silakan coba lagi!")
        continue

# Output - Limas.
if input_bangun_ruang == "LIMAS" or input_bangun_ruang == "3":
    print(f"""
======= Luas Permukaan {list_limas[jenis_limas]} =======
Luas Alas Limas: {luas_alas_limas:,.2f} cm
Keliling Alas Limas: {keliling_alas_limas:,.2f} cm
Tinggi Sisi Tegak Limas: {sisi_tegak_limas:,.2f} cm
Rumus Luas Permukaan Limas: {luas_alas_limas:,.2f} cm + (1/2 x {keliling_alas_limas:,.2f} cm x {sisi_tegak_limas:,.2f} cm)
Luas Permukaan Limas: {luas_alas_limas + (0.5 * keliling_alas_limas * sisi_tegak_limas):,.2f} cm²

======= Volume {list_limas[jenis_limas]} =======
Luas Alas Limas: {luas_alas_limas:,.2f} cm
Tinggi Limas: {tinggi_limas:,.2f} cm
Rumus Volume Limas: 1/3 x {luas_alas_limas:,.2f} cm x {tinggi_limas:,.2f} cm
Volume Limas: {(1/3) * luas_alas_limas * tinggi_limas:,.2f} cm³
""")
