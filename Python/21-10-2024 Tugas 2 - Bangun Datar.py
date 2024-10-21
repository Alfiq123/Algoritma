import math
# Buatlah program untuk Menghitung luas dan volume bangun (datar / ruang) dengan tampilan:

# ==================================================
# *** PILIHAN BANGUN : ***
# ==================================================

# A. BANGUN DATAR (LUAS & KELILING)
#    1. Persegi             5. Trapesium
#    2. Persegi Panjang     6. Jajar Genjang
#    3. Segitiga            7. Lingkaran
#    4. Lingkaran           8. Belah Ketupat

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
# • Keliling: sisi1 + sisi2 + sisi3         # • Keliling: sisi1 + sisi2 + sisi3 + sisi4

# Lingkaran:                                # Trapesium:
# • Luas: π x r² (π = 22/7 atau 3,14)       # • Luas: 1/2 x (alas atas + alas bawah) x tinggi
# • Keliling: 2 x π x r                     # • Keliling: sisi atas + sisi samping1 + sisi bawah + sisi samping2

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
    "JAJAR GENJANG", "BELAH KETUPAT", "LAYANG-LAYANG", "TRAPESIUM"
    ]
bangun_ruang = [
    "KUBUS", "BALOK", "PRISMA", "LIMAS",
    "TABUNG", "KERUCUT", "BOLA"
]
rumus = ["LUAS", "KELILING", "VOLUME", "LUAS PERMUKAAN"]

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
   1. Persegi             5. Trapesium
   2. Persegi Panjang     6. Jajar Genjang
   3. Segitiga            7. Lingkaran
   4. Lingkaran           8. Belah Ketupat
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

        print("\n======= Luas Persegi =======")
        print(f"Sisi Persegi adalah: {sisi_persegi:,.2f} cm")
        print(f"Rumus Luas Persegi adalah: {sisi_persegi:,.2f} cm x {sisi_persegi:.2f} cm")
        print(f"Luas Persegi adalah: {sisi_persegi * sisi_persegi:,.2f} cm²")

        print("\n======= Keliling Persegi =======")
        print(f"Sisi Persegi adalah: {sisi_persegi:,.2f} cm")
        print(f"Rumus Keliling Persegi adalah: 4 x {sisi_persegi:,.2f} cm")
        print(f"Keliling Persegi adalah: {4 * sisi_persegi:,.2f} cm")

    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue
    else:
        break

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

        print("\n======= Luas Persegi Panjang =======")
        print(f"Panjang Persegi Panjang: {panjang_persegi_panjang:,.2f} cm")
        print(f"Lebar Persegi Panjang: {lebar_persegi_panjang:,.2f} cm")
        print(f"Rumus Luas Persegi Panjang: {panjang_persegi_panjang:,.2f} cm x {lebar_persegi_panjang:.2f} cm")
        print(f"Luas Persegi Panjang: {panjang_persegi_panjang * lebar_persegi_panjang:,.2f} cm²")

        print("\n======= Keliling Persegi Panjang =======")
        print(f"Panjang Persegi Panjang: {panjang_persegi_panjang:,.2f} cm")
        print(f"Lebar Persegi Panjang: {lebar_persegi_panjang:,.2f} cm")
        print(f"Rumus Keliling Persegi Panjang: 2 x ({panjang_persegi_panjang:,.2f} cm + {lebar_persegi_panjang:.2f} cm)")
        print(f"Luas Persegi Panjang: {2 * (panjang_persegi_panjang + lebar_persegi_panjang):,.2f} cm")

    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue
    else:
        break

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
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue
    else:
        break

# Input - Tinggi Segitiga.
while input_bangun_datar == "SEGITIGA":
    try:
        tinggi_segitiga = float(input("Masukkan Tinggi Segitiga: "))
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue
    else:
        break

# Input - Sisi Segitiga.
while input_bangun_datar == "SEGITIGA":
    try:
        sisi_segitiga = float(input("Masukkan Sisi Segitiga: "))
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue
    else:
        break

# Output - Segitiga.
if input_bangun_datar == "SEGITIGA":

        print("\n======= Luas Segitiga =======")
        print(f"Alas Segitiga: {alas_segitiga:,.2f} cm")
        print(f"Tinggi Segitiga: {tinggi_segitiga:,.2f} cm")
        print(f"Rumus Luas Segitiga: 1/2 x {alas_segitiga:,.2f} cm x {tinggi_segitiga:.2f} cm")
        print(f"Luas Segitiga: {0.5 * alas_segitiga * tinggi_segitiga:,.2f} cm²")

        print("\n======= Keliling Segitiga =======")
        print(f"Sisi Segitiga: {sisi_segitiga:,.2f} cm")
        print(f"Rumus Keliling Segitiga: {sisi_segitiga:,.2f} cm + {sisi_segitiga:.2f} cm + {sisi_segitiga:.2f} cm")
        print(f"Keliling Segitiga: {sisi_segitiga * 3:,.2f} cm")

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

        print("\n======= Luas Lingkaran =======")
        print(f"Jari-Jari Lingkaran: {jari_lingkaran:,.2f} cm")
        print(f"Rumus Luas Lingkaran: π x {jari_lingkaran:.2f} cm x {jari_lingkaran:.2f} cm")
        print(f"Luas Lingkaran: {math.pi * jari_lingkaran ** 2:,.2f} cm²")

        print("\n======= Keliling Lingkaran =======")
        print(f"Rumus Keliling Lingkaran: 2 x π x {jari_lingkaran:.2f} cm")
        print(f"Keliling Lingkaran: {2 * math.pi * jari_lingkaran:,.2f} cm")

    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue
    else:
        break

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
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue
    else:
        break

# Input - Tinggi Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG":
    try:
        tinggi_jajar_genjang = float(input("Masukkan Tinggi Jajar Genjang: "))
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue
    else:
        break

# Input - Sisi Atas Jajar Genjang.
while input_bangun_datar == "JAJAR GENJANG":
    try:
        satas_jajar_genjang = float(input("Masukkan Sisi Atas Jajar Genjang: "))
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue
    else:
        break

# Input - Sisi Bawah Genjang.
while input_bangun_datar == "JAJAR GENJANG":
    try:
        ssamping_jajar_genjang = float(input("Masukkan Sisi Samping Jajar Genjang: "))
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue
    else:
        break

# Output - Jajar Genjang
if input_bangun_datar == "JAJAR GENJANG":

    print("\n======= Luas Jajar Genjang =======")
    print(f"Alas Jajar Genjang: {alas_jajar_genjang:,.2f} cm")
    print(f"Tinggi Jajar Genjang: {tinggi_jajar_genjang:,.2f} cm")
    print(f"Rumus Luas Jajar Genjang: {alas_jajar_genjang:,.2f} cm x {tinggi_jajar_genjang:,.2f} cm")
    print(f"Luas Jajar Genjang: {alas_jajar_genjang * tinggi_jajar_genjang:,.2f} cm²")

    print("\n======= Keliling Jajar Genjang =======")
    print(f"Sisi Atas Jajar Genjang: {satas_jajar_genjang:,.2f} cm")
    print(f"Sisi Bawah Jajar Genjang: {ssamping_jajar_genjang:,.2f} cm")
    print(f"Rumus Keliling Jajar Genjang: 2 x ({satas_jajar_genjang:,.2f} cm + 2 x {ssamping_jajar_genjang:,.2f}) cm")
    print(f"Keliling Jajar Genjang: {2 * (satas_jajar_genjang + ssamping_jajar_genjang):,.2f} cm")
