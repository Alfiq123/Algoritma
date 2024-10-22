import math
# Buatlah program untuk Menghitung luas dan volume bangun (datar / ruang) dengan tampilan:

# ==================================================
# *** PILIHAN BANGUN : ***
# ==================================================

# A. BANGUN DATAR (LUAS & KELILING)
#    1. Persegi             5. Jajar Genjang
#    2. Persegi Panjang     6. Belah Ketupat
#    3. Segitiga            7. Layang-Layang
#    4. Lingkaran           8. Trapesium

# B. BANGUN RUANG (LUAS MUKA & VOLUME)
#    1. Kubus      5. Tabung
#    2. Balok      6. Kerucut
#    3. Prisma     7. Bola
#    4. Limas

# ==================================================
# *** PILIHAN BANGUN : ............INPUT ***
# ==================================================

# Referensi Rumus - Bangun Datar

# Persegi:                                  # Jajar Genjang:
# • Luas: sisi x sisi                       # • Luas: alas x tinggi
# • Keliling: 4 x sisi                      # • Keliling: 2 x (sisi atas + sisi samping)

# Persegi Panjang:                          # Belah Ketupat:
# • Luas: panjang x lebar                   # • Luas: 1/2 x diagonal1 x diagonal2
# • Keliling: 2 x (panjang + lebar)         # • Keliling: 4 x sisi

# Segitiga:                                 # Layang-Layang:
# • Luas: 1/2 x alas x tinggi               # • Luas: 1/2 x diagonal1 x diagonal2
# • Keliling: sisi1 + sisi2 + sisi3         # • Keliling: 2 x (AB + BC)

# Lingkaran:                                # Trapesium:
# • Luas: π x r² (π = 22/7 atau 3,14)       # • Luas: 1/2 x (A + B) x tinggi
# • Keliling: 2 x π x r                     # • Keliling: AB + BC + CD + DA

# Referensi Rumus - Bangun Ruang

# Kubus:
# • Luas permukaan: 6 x sisi²
# • Volume: sisi³

# Balok:
# • Luas permukaan: 2 x ((panjang x lebar) + (panjang x tinggi) + (lebar x tinggi))
# • Volume: panjang x lebar x tinggi

# Prisma:
# • Luas permukaan: (2 x luas alas) + (keliling alas x tinggi)
# • Volume: luas alas x tinggi

# Limas:
# • Luas permukaan: luas alas + (1/2 x keliling alas x tinggi sisi tegak)
# • Volume: 1/3 x luas alas x tinggi

# Tabung:
# • Luas permukaan: 2 x π x r x (r + tinggi)
# • Volume: π x r² x tinggi

# Kerucut:
# • Luas permukaan: π x r x (r + tinggi)
# • Volume: 1/3 x π x r² x tinggi

# Bola:
# • Luas permukaan: 4 x π x r²
# • Volume: 4/3 x π x r³

# List untuk memisahkan.
bangun = ["DATAR", "RUANG"]
bangun_datar = [
    "PERSEGI", "PERSEGI PANJANG", "SEGITIGA", "LINGKARAN",
    "JAJAR GENJANG", "BELAH KETUPAT", "LAYANG LAYANG", "TRAPESIUM"
    ]
bangun_ruang = [
    "KUBUS", "BALOK", "PRISMA", "LIMAS",
    "TABUNG", "KERUCUT", "BOLA"
]

# rumus = ["LUAS", "KELILING", "VOLUME", "LUAS PERMUKAAN"]

#   ____                                  _____        _               #
#  |  _ \                                |  __ \      | |              #
#  | |_) | __ _ _ __   __ _ _   _ _ __   | |  | | __ _| |_ __ _ _ __   #
#  |  _ < / _` | '_ \ / _` | | | | '_ \  | |  | |/ _` | __/ _` | '__|  #
#  | |_) | (_| | | | | (_| | |_| | | | | | |__| | (_| | || (_| | |     #
#  |____/ \__,_|_| |_|\__, |\__,_|_| |_| |_____/ \__,_|\__\__,_|_|     #
#                      __/ |                                           #
#                     |___/                                            #

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

# Input - Bangun Datar / Bangun Ruang.
while True:
        input_bangun = str(input("Masukkan pilihan bangun - Datar / Ruang: ")).upper()
        if input_bangun in bangun:
            if input_bangun == "RUANG":
                print("Bangun Ruang Belum Tersedia")
                break
            break
        else:
            print("📢 Pilihan tidak ada, silakan pilih kembali!")

# Input - Bangun Datar.
while True:
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
        input_bangun_datar = str(input("Masukkan Pilihan Bangun Datar: ")).upper()
        if input_bangun_datar in bangun_datar:
            break
        else:
            print("📢 Bangun datar tidak ada yang terpilih, silakan pilih kembali!")
            continue

if input_bangun_datar == "PERSEGI":
    print(r"""
  ___                           _ 
 | _ \ ___  _ _  ___ ___  __ _ (_)
 |  _// -_)| '_|(_-</ -_)/ _` || |
 |_|  \___||_|  /__/\___|\__, ||_|
                         |___/    
""")

# Input - Sisi Persegi.
while input_bangun_datar == "PERSEGI":
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

if input_bangun_datar == "PERSEGI PANJANG":
    print(r"""
  ___                           _   ___               _                   
 | _ \ ___  _ _  ___ ___  __ _ (_) | _ \ __ _  _ _   (_) __ _  _ _   __ _ 
 |  _// -_)| '_|(_-</ -_)/ _` || | |  _// _` || ' \  | |/ _` || ' \ / _` |
 |_|  \___||_|  /__/\___|\__, ||_| |_|  \__,_||_||_|_/ |\__,_||_||_|\__, |
                         |___/                     |__/             |___/ 
""")

# Input - Panjang & Lebar Persegi Panjang.
while input_bangun_datar == "PERSEGI PANJANG":
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

if input_bangun_datar == "SEGITIGA":
    print(r"""
  ___             _  _    _             
 / __| ___  __ _ (_)| |_ (_) __ _  __ _ 
 \__ \/ -_)/ _` || ||  _|| |/ _` |/ _` |
 |___/\___|\__, ||_| \__||_|\__, |\__,_|
           |___/            |___/       
""")

# Input - Alas Segitiga.
while input_bangun_datar == "SEGITIGA":
    try:
        alas_segitiga = float(input("Masukkan Alas Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Input - Tinggi Segitiga.
while input_bangun_datar == "SEGITIGA":
    try:
        tinggi_segitiga = float(input("Masukkan Tinggi Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Input - Sisi Segitiga.
while input_bangun_datar == "SEGITIGA":
    try:
        sisi_segitiga = float(input("Masukkan Sisi Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Output - Segitiga.
if input_bangun_datar == "SEGITIGA":

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

if input_bangun_datar == "LINGKARAN":
    print(r"""
  _     _              _                          
 | |   (_) _ _   __ _ | |__ __ _  _ _  __ _  _ _  
 | |__ | || ' \ / _` || / // _` || '_|/ _` || ' \ 
 |____||_||_||_|\__, ||_\_\\__,_||_|  \__,_||_||_|
                |___/                             
    """)

# Input Jari-Jari Lingkaran.
while input_bangun_datar == "LINGKARAN":
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

if input_bangun_datar == "JAJAR GENJANG":
    print(r"""
     _         _               ___              _                   
  _ | | __ _  (_) __ _  _ _   / __| ___  _ _   (_) __ _  _ _   __ _ 
 | || |/ _` | | |/ _` || '_| | (_ |/ -_)| ' \  | |/ _` || ' \ / _` |
  \__/ \__,_|_/ |\__,_||_|    \___|\___||_||_|_/ |\__,_||_||_|\__, |
            |__/                             |__/             |___/ 
    """)

# Input - Alas Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG":
    try:
        alas_jajar_genjang = float(input("Masukkan Alas Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Tinggi Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG":
    try:
        tinggi_jajar_genjang = float(input("Masukkan Tinggi Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Atas Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG":
    try:
        satas_jajar_genjang = float(input("Masukkan Sisi Atas Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Bawah Genjang.
while input_bangun_datar == "JAJAR GENJANG":
    try:
        ssamping_jajar_genjang = float(input("Masukkan Sisi Samping Jajar Genjang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Output - Jajar Genjang.
if input_bangun_datar == "JAJAR GENJANG":

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

if input_bangun_datar == "BELAH KETUPAT":
    print(r"""
  ___      _      _      _  __    _                   _   
 | _ ) ___| |__ _| |_   | |/ /___| |_ _  _ _ __  __ _| |_ 
 | _ \/ -_) / _` | ' \  | ' </ -_)  _| || | '_ \/ _` |  _|
 |___/\___|_\__,_|_||_| |_|\_\___|\__|\_,_| .__/\__,_|\__|
                                          |_|             
""")

# Input - Diagonal 1 Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT":
    try:
        diagonal1_belah_ketupat = float(input("Masukkan Diagonal 1 Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Diagonal 2 Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT":
    try:
        diagonal2_belah_ketupat = float(input("Masukkan Diagonal 2 Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT":
    try:
        sisi_belah = float(input("Masukkan Sisi Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

if input_bangun_datar == "BELAH KETUPAT":
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
    
if input_bangun_datar == "LAYANG LAYANG":
    print(r"""
  _                               _                             
 | |   __ _ _  _ __ _ _ _  __ _  | |   __ _ _  _ __ _ _ _  __ _ 
 | |__/ _` | || / _` | ' \/ _` | | |__/ _` | || / _` | ' \/ _` |
 |____\__,_|\_, \__,_|_||_\__, | |____\__,_|\_, \__,_|_||_\__, |
            |__/          |___/             |__/          |___/ 
""")

# Input - Diagonal 1 Layang Layang.
while input_bangun_datar == "LAYANG LAYANG":
    try:
        diagonal1_layang = float(input("Masukkan Diagonal 1 Layang Layang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Diagonal 2 Layang Layang.
while input_bangun_datar == "LAYANG LAYANG":
    try:
        diagonal2_layang = float(input("Masukkan Diagonal 2 Layang Layang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Layang Layang AB.
while input_bangun_datar == "LAYANG LAYANG":
    try:
        sisi_layang_ab = float(input("Masukkan Sisi Layang Layang AB: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Layang Layang BC.
while input_bangun_datar == "LAYANG LAYANG":
    try:
        sisi_layang_bc = float(input("Masukkan Sisi Layang Layang BC: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

if input_bangun_datar == "LAYANG LAYANG":
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

if input_bangun_datar == "TRAPESIUM":
    print(r"""
  _____                      _            
 |_   _| _ __ _ _ __  ___ __(_)_  _ _ __  
   | || '_/ _` | '_ \/ -_|_-< | || | '  \ 
   |_||_| \__,_| .__/\___/__/_|\_,_|_|_|_|
               |_|                        
""")

# Input - Untuk Rumus Trapesium.
while input_bangun_datar == "TRAPESIUM":
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
while input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "LUAS":
    try:
        alas_atas_trapesium = float(input("Masukkan Alas Atas Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Alas Bawah Trapesium.
while input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "LUAS":
    try:
        alas_bawah_trapesium = float(input("Masukkan Alas Bawah Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Tinggi Trapesium.
while input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "LUAS":
    try:
        tinggi_trapesium = float(input("Masukkan Tinggi Trapesium: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Output - Luas Trapesium
if input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "LUAS":
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
while input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_ab = float(input("Masukkan Sisi Trapesium AB: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi BC Trapesium.
while input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_bc = float(input("Masukkan Sisi Trapesium BC: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi CD Trapesium.
while input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_cd = float(input("Masukkan Sisi Trapesium CD: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Input - Sisi DA Trapesium.
while input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "KELILING":
    try:
        sisi_trapesium_da = float(input("Masukkan Sisi Trapesium DA: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")

# Output - Keliling Trapesium
if input_bangun_datar == "TRAPESIUM" and rumus_trapesium == "KELILING":
    print(f"""
======= Keliling Trapesium =======
Trapesium Sisi AB: {sisi_trapesium_ab:,.2f} cm
Trapesium Sisi BC: {sisi_trapesium_bc:,.2f} cm
Trapesium Sisi CD: {sisi_trapesium_cd:,.2f} cm
Trapesium Sisi DA: {sisi_trapesium_da:,.2f} cm
Rumus Keliling Trapesium: {sisi_trapesium_ab:,.2f} cm + {sisi_trapesium_bc:,.2f} cm + {sisi_trapesium_cd:,.2f} cm + {sisi_trapesium_da:,.2f} cm
Keliling Trapesium: {sisi_trapesium_ab + sisi_trapesium_bc + sisi_trapesium_cd + sisi_trapesium_da:,.2f} cm
""")
