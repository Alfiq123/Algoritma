import math

# List - List Bangun.
bangun = ["DATAR", "RUANG"]
bangun_datar = [
    "PERSEGI", "PERSEGI PANJANG", "SEGITIGA", "LINGKARAN",
    "JAJAR GENJANG", "BELAH KETUPAT", "LAYANG LAYANG", "TRAPESIUM",
    "1", "2", "3", "4", "5", "6", "7", "8"
    ]
bangun_ruang = [
    "KUBUS", "BALOK", "PRISMA", "LIMAS",
    "TABUNG", "KERUCUT", "BOLA",
    "1", "2", "3", "4", "5", "6", "7"
]

# Placeholder (Mengakali "Undefined Variable")
input_bangun_datar = ""
input_bangun_ruang = ""

print(r"""
______  _  _  _  _      ______                                    
| ___ \(_)| |(_)| |     | ___ \                                   
| |_/ / _ | | _ | |__   | |_/ /  __ _  _ __    __ _  _   _  _ __  
|  __/ | || || || '_ \  | ___ \ / _` || '_ \  / _` || | | || '_ \ 
| |    | || || || | | | | |_/ /| (_| || | | || (_| || |_| || | | |
\_|    |_||_||_||_| |_| \____/  \__,_||_| |_| \__, | \__,_||_| |_|
                                               __/ |              
                                              |___/               
""")

input_bangun = str(input("Masukkan pilihan bangun - Datar / Ruang: ")).upper()
while True:
    if input_bangun in bangun:
        break
    else:
        print("📢 Pilihan tidak ada, silakan pilih kembali!")
        input_bangun = str(input("Masukkan pilihan bangun - Datar / Ruang: ")).upper()
        continue

if input_bangun == "DATAR":
    print(r"""
  ____                                  _____        _             
 |  _ \                                |  __ \      | |            
 | |_) | __ _ _ __   __ _ _   _ _ __   | |  | | __ _| |_ __ _ _ __ 
 |  _ < / _` | '_ \ / _` | | | | '_ \  | |  | |/ _` | __/ _` | '__|
 | |_) | (_| | | | | (_| | |_| | | | | | |__| | (_| | || (_| | |   
 |____/ \__,_|_| |_|\__, |\__,_|_| |_| |_____/ \__,_|\__\__,_|_|   
                     __/ |                                         
                    |___/                                          
""")

    print(r"""
✦ BANGUN DATAR - MASUKKAN PILIHAN ✦
   1. Persegi             5. Jajar Genjang
   2. Persegi Panjang     6. Belah Ketupat
   3. Segitiga            7. Layang-Layang
   4. Lingkaran           8. Trapesium
""")

while input_bangun == "DATAR":
    input_bangun_datar = str(input("Masukkan Pilihan Bangun Datar: ")).upper()
    if input_bangun_datar in bangun_datar:
        break
    else:
        print("📢 Bangun datar tidak ada yang terpilih, silakan pilih kembali!")
        continue

# Persegi
if input_bangun_datar == "PERSEGI" or input_bangun_datar == "1":
    print(r"""
  ___                           _ 
 | _ \ ___  _ _  ___ ___  __ _ (_)
 |  _// -_)| '_|(_-</ -_)/ _` || |
 |_|  \___||_|  /__/\___|\__, ||_|
                         |___/    
""")

# Input - Sisi Persegi.
while input_bangun_datar == "PERSEGI" or input_bangun_datar == "1":
    try:
        sisi_persegi = float(input("Masukkan sisi persegi: "))

        print(f"""
======= Luas Persegi =======
Sisi Persegi adalah: {sisi_persegi:,.2f} cm
Rumus Luas Persegi adalah: {sisi_persegi:,.2f} cm x {sisi_persegi:.2f} cm
Luas Persegi adalah: {sisi_persegi * sisi_persegi:,.2f} cm²""")

        print(f"""
======= Keliling Persegi =======
Sisi Persegi adalah: {sisi_persegi:,.2f} cm
Rumus Keliling Persegi adalah: 4 x {sisi_persegi:,.2f} cm
Keliling Persegi adalah: {4 * sisi_persegi:,.2f} cm
""")
        break

    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Persegi Panjang.
if input_bangun_datar == "PERSEGI PANJANG" or input_bangun_datar == "2":
    print(r"""
  ___                           _   ___               _                   
 | _ \ ___  _ _  ___ ___  __ _ (_) | _ \ __ _  _ _   (_) __ _  _ _   __ _ 
 |  _// -_)| '_|(_-</ -_)/ _` || | |  _// _` || ' \  | |/ _` || ' \ / _` |
 |_|  \___||_|  /__/\___|\__, ||_| |_|  \__,_||_||_|_/ |\__,_||_||_|\__, |
                         |___/                     |__/             |___/ 
""")

# Input - Panjang & Lebar Persegi Panjang.
while input_bangun_datar == "PERSEGI PANJANG" or input_bangun_datar == "2":
    try:
        panjang_persegi_panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar_persegi_panjang = float(input("Masukkan lebar persegi panjang: "))

        print(f"""
======= Luas Persegi Panjang =======
Panjang Persegi Panjang: {panjang_persegi_panjang:,.2f} cm
Lebar Persegi Panjang: {lebar_persegi_panjang:,.2f} cm
Rumus Luas Persegi Panjang: {panjang_persegi_panjang:,.2f} cm x {lebar_persegi_panjang:.2f} cm
Luas Persegi Panjang: {panjang_persegi_panjang * lebar_persegi_panjang:,.2f} cm²""")

        print(f"""
======= Keliling Persegi Panjang =======
"Panjang Persegi Panjang: {panjang_persegi_panjang:,.2f} cm
"Lebar Persegi Panjang: {lebar_persegi_panjang:,.2f} cm
"Rumus Keliling Persegi Panjang: 2 x ({panjang_persegi_panjang:,.2f} cm + {lebar_persegi_panjang:.2f} cm)
"Luas Persegi Panjang: {2 * (panjang_persegi_panjang + lebar_persegi_panjang):,.2f} cm
""")
        break

    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Segitiga.
if input_bangun_datar == "SEGITIGA" or input_bangun_datar == "3":
    print(r"""
  ___             _  _    _             
 / __| ___  __ _ (_)| |_ (_) __ _  __ _ 
 \__ \/ -_)/ _` || ||  _|| |/ _` |/ _` |
 |___/\___|\__, ||_| \__||_|\__, |\__,_|
           |___/            |___/       
""")

# Input - Alas Segitiga.
while input_bangun_datar == "SEGITIGA" or input_bangun_datar == "3":
    try:
        alas_segitiga = float(input("Masukkan Alas Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Input - Tinggi Segitiga.
while input_bangun_datar == "SEGITIGA" or input_bangun_datar == "3":
    try:
        tinggi_segitiga = float(input("Masukkan Tinggi Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Input - Sisi Segitiga.
while input_bangun_datar == "SEGITIGA" or input_bangun_datar == "3":
    try:
        sisi_segitiga = float(input("Masukkan Sisi Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Output - Segitiga.
if input_bangun_datar == "SEGITIGA" or input_bangun_datar == "3":

        print(f"""
======= Luas Segitiga =======
"Alas Segitiga: {alas_segitiga:,.2f} cm
"Tinggi Segitiga: {tinggi_segitiga:,.2f} cm
"Rumus Luas Segitiga: 1/2 x {alas_segitiga:,.2f} cm x {tinggi_segitiga:.2f} cm
"Luas Segitiga: {0.5 * alas_segitiga * tinggi_segitiga:,.2f} cm²""")
        
        print(f"""
======= Keliling Segitiga =======
Sisi Segitiga: {sisi_segitiga:,.2f} cm
Rumus Keliling Segitiga: {sisi_segitiga:,.2f} cm + {sisi_segitiga:.2f} cm + {sisi_segitiga:.2f} cm
Keliling Segitiga: {sisi_segitiga * 3:,.2f} cm
""")

if input_bangun_datar == "LINGKARAN" or input_bangun_datar == "4":
    print(r"""
  _     _              _                          
 | |   (_) _ _   __ _ | |__ __ _  _ _  __ _  _ _  
 | |__ | || ' \ / _` || / // _` || '_|/ _` || ' \ 
 |____||_||_||_|\__, ||_\_\\__,_||_|  \__,_||_||_|
                |___/                             
    """)

# Input Jari-Jari Lingkaran.
while input_bangun_datar == "LINGKARAN" or input_bangun_datar == "4":
    try:
        jari_lingkaran = float(input("Masukkan Jari-Jari Lingkaran: "))

        print(f"""
======= Luas Lingkaran =======
Jari-Jari Lingkaran: {jari_lingkaran:,.2f} cm
Rumus Luas Lingkaran: π x {jari_lingkaran:.2f} cm x {jari_lingkaran:.2f} cm
Luas Lingkaran: {math.pi * jari_lingkaran ** 2:,.2f} cm²""")
        
        print(f"""
======= Keliling Lingkaran =======
Rumus Keliling Lingkaran: 2 x π x {jari_lingkaran:.2f} cm
Keliling Lingkaran: {2 * math.pi * jari_lingkaran:,.2f} cm
""")
        break

    except ValueError:
        print("📢 Tolong Masukkan Angka!")
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
while input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "5":
    try:
        alas_jajar_genjang = float(input("Masukkan Alas Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Tinggi Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "5":
    try:
        tinggi_jajar_genjang = float(input("Masukkan Tinggi Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Atas Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "5":
    try:
        satas_jajar_genjang = float(input("Masukkan Sisi Atas Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Bawah Genjang.
while input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "5":
    try:
        ssamping_jajar_genjang = float(input("Masukkan Sisi Samping Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Output - Jajar Genjang.
if input_bangun_datar == "JAJAR GENJANG" or input_bangun_datar == "5":

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

# Belah Ketupat.
if input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "6":
    print(r"""
  ___      _      _      _  __    _                   _   
 | _ ) ___| |__ _| |_   | |/ /___| |_ _  _ _ __  __ _| |_ 
 | _ \/ -_) / _` | ' \  | ' </ -_)  _| || | '_ \/ _` |  _|
 |___/\___|_\__,_|_||_| |_|\_\___|\__|\_,_| .__/\__,_|\__|
                                          |_|             
""")

# Input - Diagonal 1 Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "6":
    try:
        diagonal1_belah_ketupat = float(input("Masukkan Diagonal 1 Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Diagonal 2 Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "6":
    try:
        diagonal2_belah_ketupat = float(input("Masukkan Diagonal 2 Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "6":
    try:
        sisi_belah = float(input("Masukkan Sisi Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

if input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "6":
    print(f"""
======= Luas Belah Ketupat =======
Diagonal 1 Belah Ketupat: {diagonal1_belah_ketupat:,.2f} cm
Diagonal 2 Belah Ketupat: {diagonal2_belah_ketupat:,.2f} cm
Rumus Luas Belah Ketupat: 1/2 x {diagonal1_belah_ketupat:,.2f} cm x {diagonal2_belah_ketupat:,.2f} cm
Luas Belah Ketupat: {0.5 * diagonal1_belah_ketupat * diagonal2_belah_ketupat:,.2f} cm""")
    
    print(f"""
======= Keliling Belah Ketupat =======
Sisi Belah Ketupat: {sisi_belah:,.2f} cm
Rumus Keliling Belah Ketupat: 4 x {sisi_belah:,.2f} cm
Keliling Belah Ketupat: {4 * sisi_belah:,.2f} cm²""")

# Layang - Layang.
if input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "7":
    print(r"""
  _                               _                             
 | |   __ _ _  _ __ _ _ _  __ _  | |   __ _ _  _ __ _ _ _  __ _ 
 | |__/ _` | || / _` | ' \/ _` | | |__/ _` | || / _` | ' \/ _` |
 |____\__,_|\_, \__,_|_||_\__, | |____\__,_|\_, \__,_|_||_\__, |
            |__/          |___/             |__/          |___/ 
""")

# Input - Diagonal 1 Layang Layang.
while input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "7":
    try:
        diagonal1_layang = float(input("Masukkan Diagonal 1 Layang Layang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Diagonal 2 Layang Layang.
while input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "7":
    try:
        diagonal2_layang = float(input("Masukkan Diagonal 2 Layang Layang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Layang Layang AB.
while input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "7":
    try:
        sisi_layang_ab = float(input("Masukkan Sisi Layang Layang AB: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Layang Layang BC.
while input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "7":
    try:
        sisi_layang_bc = float(input("Masukkan Sisi Layang Layang BC: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

if input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "7":
    print(f"""
======= Luas Layang Layang =======
Diagonal 1 Layang Layang: {diagonal1_layang:,.2f} cm
Diagonal 2 Layang Layang: {diagonal2_layang:,.2f} cm
Rumus Luas Layang Layang: 1/2 x {diagonal1_layang:,.2f} cm x {diagonal2_layang:,.2f} cm
Luas Layang Layang: {0.5 * diagonal1_layang * diagonal2_layang:,.2f} cm""")

    print(f"""
======= Keliling Layang Layang =======
Sisi Layang Layang AB: {sisi_layang_ab:,.2f} cm
Sisi Layang Layang BC: {sisi_layang_bc:,.2f} cm
Rumus Keliling Layang Layang: 2 x ({sisi_layang_ab:,.2f} cm +  {sisi_layang_bc:,.2f} cm)
Keliling Layang Layang: {2 * (sisi_layang_ab + sisi_layang_bc):,.2f} cm²
""")

# Trapesium.
if input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8":
    print(r"""
  _____                      _            
 |_   _| _ __ _ _ __  ___ __(_)_  _ _ __  
   | || '_/ _` | '_ \/ -_|_-< | || | '  \ 
   |_||_| \__,_| .__/\___/__/_|\_,_|_|_|_|
               |_|                        
""")

# Input - Untuk Rumus Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8":
    rumus_trapesium = str(input("Masukkan Rumus Trapesium (Luas / Keliling): ")).upper()
    if rumus_trapesium == "LUAS" or rumus_trapesium == "KELILING":
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
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "LUAS":
    try:
        alas_atas_trapesium = float(input("Masukkan Alas Atas Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Alas Bawah Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "LUAS":
    try:
        alas_bawah_trapesium = float(input("Masukkan Alas Bawah Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Tinggi Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "LUAS":
    try:
        tinggi_trapesium = float(input("Masukkan Tinggi Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Output - Luas Trapesium
if input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "LUAS":
    print(f"""
======= Luas Trapesium =======
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
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_ab = float(input("Masukkan Sisi Trapesium AB: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi BC Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_bc = float(input("Masukkan Sisi Trapesium BC: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi CD Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_cd = float(input("Masukkan Sisi Trapesium CD: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi DA Trapesium.
while input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_da = float(input("Masukkan Sisi Trapesium DA: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Output - Keliling Trapesium
if input_bangun_datar == "TRAPESIUM" or input_bangun_datar == "8" and rumus_trapesium == "KELILING":
    print(f"""
======= Keliling Trapesium =======
Trapesium Sisi AB: {sisi_trapesium_ab:,.2f} cm
Trapesium Sisi BC: {sisi_trapesium_bc:,.2f} cm
Trapesium Sisi CD: {sisi_trapesium_cd:,.2f} cm
Trapesium Sisi DA: {sisi_trapesium_da:,.2f} cm
Rumus Keliling Trapesium: {sisi_trapesium_ab:,.2f} cm + {sisi_trapesium_bc:,.2f} cm + {sisi_trapesium_cd:,.2f} cm + {sisi_trapesium_da:,.2f} cm
Keliling Trapesium: {sisi_trapesium_ab + sisi_trapesium_bc + sisi_trapesium_cd + sisi_trapesium_da:,.2f} cm
""")

while input_bangun == "RUANG":
    print(r"""
  ____                                       _____                             
 |  _ \                                     |  __ \                            
 | |_) |  __ _  _ __    __ _  _   _  _ __   | |__) |_   _   __ _  _ __    __ _ 
 |  _ <  / _` || '_ \  / _` || | | || '_ \  |  _  /| | | | / _` || '_ \  / _` |
 | |_) || (_| || | | || (_| || |_| || | | | | | \ \| |_| || (_| || | | || (_| |
 |____/  \__,_||_| |_| \__, | \__,_||_| |_| |_|  \_\\__,_| \__,_||_| |_| \__, |
                        __/ |                                             __/ |
                       |___/                                             |___/ 
""")

    print(r"""
✦ BANGUN RUANG - MASUKKAN PILIHAN ✦
   1. Kubus         5. Tabung
   2. Balok         6. Kerucut
   3. Prisma        7. Bola
   4. Limas
""")

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

# Balok.
if input_bangun_ruang == "BALOK" or input_bangun_ruang == "2":
    print(r"""
  ___        _       _   
 | _ ) __ _ | | ___ | |__
 | _ \/ _` || |/ _ \| / /
 |___/\__,_||_|\___/|_\_\
                         
""")

# Panjang Balok.
while input_bangun_ruang == "BALOK" or input_bangun_ruang == "2":
    try:
        panjang_balok = float(input("Masukkan Panjang Balok: "))
        break
    except ValueError:
        print("📌 Panjang Tidak Valid, silakan coba lagi!")
        continue

# Lebar Balok.
while input_bangun_ruang == "BALOK" or input_bangun_ruang == "2":
    try:
        lebar_balok = float(input("Masukkan Lebar Balok: "))
        break
    except ValueError:
        print("📌 Lebar Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Balok.
while input_bangun_ruang == "BALOK" or input_bangun_ruang == "2":
    try:
        tinggi_balok = float(input("Masukkan Tinggi Balok: "))
        break
    except ValueError:
        print("📌 Tinggi Tidak Valid, silakan coba lagi!")
        continue

# Hasil Balok.
if input_bangun_ruang == "BALOK" or input_bangun_ruang == "2":
    print(f"""
======= Luas Permukaan Balok =======
Panjang Balok: {panjang_balok:,.2f} cm
Lebar Balok: {lebar_balok:,.2f} cm
Tinggi Balok: {tinggi_balok:,.2f} cm
Rumus Luas Permukaan Balok: 2 x (({panjang_balok:,.2f} cm x {lebar_balok:,.2f} cm) + ({panjang_balok:,.2f} cm x {tinggi_balok:,.2f}) cm + ({lebar_balok:,.2f} cm + {tinggi_balok:,.2f} cm))
Luas Permukaan Balok: {2 * ((panjang_balok * lebar_balok) + (panjang_balok * tinggi_balok) + (lebar_balok * tinggi_balok)):,.2f} cm²

======= Volume Balok =======
Panjang Balok: {panjang_balok:,.2f} cm
Lebar Balok: {lebar_balok:,.2f} cm
Tinggi Balok: {tinggi_balok:,.2f} cm
Rumus Volume Balok: {panjang_balok:,.2f} cm x {lebar_balok:,.2f} cm x {tinggi_balok:,.2f} cm
Volume Balok: {panjang_balok * lebar_balok * tinggi_balok:,.2f} cm³
""")

# Prisma.
if input_bangun_ruang == "PRISMA" or input_bangun_ruang == "3":
    print(r"""
  ___       _                  
 | _ \ _ _ (_) ___ _ __   __ _ 
 |  _/| '_|| |(_-<| '  \ / _` |
 |_|  |_|  |_|/__/|_|_|_|\__,_|
                               
""")

# Luas Alas Prisma.
while input_bangun_ruang == "PRISMA" or input_bangun_ruang == "3":
    try:
        luas_alas_prisma = float(input("Masukkan Luas Alas Prisma: "))
        break
    except ValueError:
        print("📌 Luas Alas Tidak Valid, silakan coba lagi!")
        continue

# Keliling Alas Prisma.
while input_bangun_ruang == "PRISMA" or input_bangun_ruang == "3":
    try:
        keliling_alas_prisma = float(input("Masukkan Keliling Alas Prisma: "))
        break
    except ValueError:
        print("📌 Keliling Alas Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Prisma.
while input_bangun_ruang == "PRISMA" or input_bangun_ruang == "3":
    try:
        tinggi_prisma = float(input("Masukkan Tinggi Prisma: "))
        break
    except ValueError:
        print("📌 Tinggi Tidak Valid, silakan coba lagi!")
        continue

# Output - Prisma.
if input_bangun_ruang == "PRISMA" or input_bangun_ruang == "3":
    print(f"""
======= Luas Permukaan Prisma =======
Luas Alas Prisma: {luas_alas_prisma:,.2f} cm
Keliling Alas Prisma: {keliling_alas_prisma:,.2f} cm
Tinggi Prisma: {tinggi_prisma:,.2f} cm
Rumus Luas Permukaan Prisma: (2 x {luas_alas_prisma:,.2f} cm) + ({keliling_alas_prisma:,.2f} cm x {tinggi_prisma:,.2f} cm)
Luas Permukaan Prisma: {(2 * luas_alas_prisma) + (keliling_alas_prisma * tinggi_prisma):,.2f} cm²

======= Volume Prisma =======
Luas Alas Prisma: {luas_alas_prisma:,.2f} cm
Keliling Alas Prisma: {keliling_alas_prisma:,.2f} cm
Tinggi Prisma: {tinggi_prisma:,.2f} cm
Rumus Volume Prisma: {luas_alas_prisma:,.2f} cm x {tinggi_prisma:,.2f} cm
Volume Prisma: {luas_alas_prisma * tinggi_prisma:,.2f} cm³
""")

# Limas.
if input_bangun_ruang == "LIMAS" or input_bangun_ruang == "4":
    print(r"""
  _     _                  
 | |   (_) _ __   __ _  ___
 | |__ | || '  \ / _` |(_-<
 |____||_||_|_|_|\__,_|/__/
                           
""")

# Luas Alas Limas.
while input_bangun_ruang == "LIMAS" or input_bangun_ruang == "4":
    try:
        luas_alas_limas = float(input("Masukkan Luas Alas Limas: "))
        break
    except ValueError:
        print("📌 Luas Alas Tidak Valid, silakan coba lagi!")
        continue

# Keliling Alas Limas.
while input_bangun_ruang == "LIMAS" or input_bangun_ruang == "4":
    try:
        keliling_alas_limas = float(input("Masukkan Keliling Alas Limas: "))
        break
    except ValueError:
        print("📌 Keliling Alas Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Sisi Tegak Limas.
while input_bangun_ruang == "LIMAS" or input_bangun_ruang == "4":
    try:
        sisi_tegak_limas = float(input("Masukkan Tinggi Sisi Tegak Limas: "))
        break
    except ValueError:
        print("📌 Tinggi Sisi Tegak Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Limas.
while input_bangun_ruang == "LIMAS" or input_bangun_ruang == "4":
    try:
        tinggi_limas = float(input("Masukkan Tinggi Limas: "))
        break
    except ValueError:
        print("📌 Tinggi Tidak Valid, silakan coba lagi!")
        continue

# Output - Limas.
if input_bangun_ruang == "LIMAS" or input_bangun_ruang == "4":
    print(f"""
======= Luas Permukaan Limas =======
Luas Alas Limas: {luas_alas_limas:,.2f} cm
Keliling Alas Limas: {keliling_alas_limas:,.2f} cm
Tinggi Sisi Tegak Limas: {sisi_tegak_limas:,.2f} cm
Rumus Luas Permukaan Limas: {luas_alas_limas:,.2f} cm + (1/2 x {keliling_alas_limas:,.2f} cm x {sisi_tegak_limas:,.2f} cm)
Luas Permukaan Limas: {luas_alas_limas + (0.5 * keliling_alas_limas * sisi_tegak_limas):,.2f} cm²

======= Volume Limas =======
Luas Alas Limas: {luas_alas_limas:,.2f} cm
Keliling Alas Limas: {keliling_alas_limas:,.2f} cm
Tinggi Limas: {tinggi_limas:,.2f} cm
Rumus Volume Limas: 1/3 x {luas_alas_limas:,.2f} cm x {tinggi_limas:,.2f} cm
Volume Limas: {(1/3) * luas_alas_limas * tinggi_limas:,.2f} cm³
""")

# Tabung.
if input_bangun_ruang == "TABUNG" or input_bangun_ruang == "5":
    print(r"""
  _____       _                      
 |_   _|__ _ | |__  _  _  _ _   __ _ 
   | | / _` || '_ \| || || ' \ / _` |
   |_| \__,_||_.__/ \_,_||_||_|\__, |
                               |___/ 
""")

# Jari-Jari Tabung.
while input_bangun_ruang == "TABUNG" or input_bangun_ruang == "5":
    try:
        jari_tabung = float(input("Masukkan Jari-Jari Tabung: "))
        break
    except ValueError:
        print("🔥 Jari-Jari tidak dikenal, silakan coba lagi!")
        continue

# Tinggi Tabung.
while input_bangun_ruang == "TABUNG" or input_bangun_ruang == "5":
    try:
        tinggi_tabung = float(input("Masukkan Tinggi Tabung: "))
        break
    except ValueError:
        print("🔥 Tinggi tidak dikenal, silakan coba lagi!")
        continue

# Output -  Tabung
if input_bangun_ruang == "TABUNG" or input_bangun_ruang == "5":
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

# Kerucut.
if input_bangun_ruang == "KERUCUT" or input_bangun_ruang == "6":
    print(r"""
  _  __                           _   
 | |/ / ___  _ _  _  _  __  _  _ | |_ 
 | ' < / -_)| '_|| || |/ _|| || ||  _|
 |_|\_\\___||_|   \_,_|\__| \_,_| \__|
                                      
""")
    
# Jari-Jari Kerucut.
while input_bangun_ruang == "KERUCUT" or input_bangun_ruang == "6":
    try:
        jari_kerucut = float(input("Masukkan Jari-Jari Kerucut: "))
        break
    except ValueError:
        print("🔥 Jari-Jari tidak dikenal, silakan coba lagi!")
        continue

# Tinggi Kerucut.
while input_bangun_ruang == "KERUCUT" or input_bangun_ruang == "6":
    try:
        tinggi_kerucut = float(input("Masukkan Tinggi Kerucut: "))
        break
    except ValueError:
        print("🔥 Tinggi tidak dikenal, silakan coba lagi!")
        continue

# Output -  Kerucut
if input_bangun_ruang == "KERUCUT" or input_bangun_ruang == "6":
    print(f"""
======= Luas Permukaan Kerucut =======
Jari-Jari Kerucut: {jari_kerucut:,.2f} cm
Tinggi Kerucut: {tinggi_kerucut:,.2f} cm
Rumus Luas Permukaan Kerucut: π x {jari_kerucut:,.2f} cm x ({jari_kerucut:,.2f} + {tinggi_kerucut:,.2f} cm)
Luas Permukaan Kerucut: {math.pi * jari_kerucut * (jari_kerucut + tinggi_kerucut):,.2f} cm²

======= Volume Kerucut =======
Jari-Jari Kerucut: {jari_kerucut:,.2f} cm
Tinggi Kerucut: {tinggi_kerucut:,.2f} cm
Rumus Volume Kerucut: 1/3 x π x {jari_kerucut:,.2f} cm x {jari_kerucut:,.2f} cm x {tinggi_kerucut:,.2f} cm
Volume Kerucut: {(1/3) * math.pi * jari_kerucut ** 2 * tinggi_kerucut:,.2f} cm³
""")

# Bola.
if input_bangun_ruang == "BOLA":
    print(r"""
  ___       _       
 | _ ) ___ | | __ _ 
 | _ \/ _ \| |/ _` |
 |___/\___/|_|\__,_|
                    
""")

# Jari - Jari Bola.
while input_bangun_ruang == "BOLA":
    try:
        jari_bola = float(input("Masukkan Jari-Jari Bola: "))
        break
    except ValueError:
        print("🔥 Jari-Jari tidak dikenal, silakan coba lagi!")
        continue

# Output - Bola.
if input_bangun_ruang == "BOLA":
    print(f"""
======= Luas Permukaan Bola =======
Jari-Jari Bola: {jari_bola:,.2f} cm
Rumus Luas Permukaan Bola: 4 x π x {jari_bola:,.2f} cm x {jari_bola:,.2f} cm
Luas Permukaan Bola: {4 * math.pi * jari_bola ** 2:,.2f} cm²

======= Volume Bola =======
Jari-Jari Bola: {jari_bola:,.2f} cm
Rumus Volume Bola: 4/3 x π x {jari_bola:,.2f} cm x {jari_bola:,.2f} cm x {jari_bola:,.2f} cm
Volume Bola: {(4/3) * math.pi * jari_bola **3:,.2f} cm³
""")
