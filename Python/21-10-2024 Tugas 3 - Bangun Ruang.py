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

#   ____                                       _____                             
#  |  _ \                                     |  __ \                            
#  | |_) |  __ _  _ __    __ _  _   _  _ __   | |__) |_   _   __ _  _ __    __ _ 
#  |  _ <  / _` || '_ \  / _` || | | || '_ \  |  _  /| | | | / _` || '_ \  / _` |
#  | |_) || (_| || | | || (_| || |_| || | | | | | \ \| |_| || (_| || | | || (_| |
#  |____/  \__,_||_| |_| \__, | \__,_||_| |_| |_|  \_\\__,_| \__,_||_| |_| \__, |
#                         __/ |                                             __/ |
#                        |___/                                             |___/ 

# List untuk memisahkan.
bangun = ["DATAR", "RUANG"]

# bangun_datar = [
#     "PERSEGI", "PERSEGI PANJANG", "SEGITIGA", "LINGKARAN",
#     "JAJAR GENJANG", "BELAH KETUPAT", "LAYANG LAYANG", "TRAPESIUM"
#     ]

bangun_ruang = [
    "KUBUS", "BALOK", "PRISMA", "LIMAS",
    "TABUNG", "KERUCUT", "BOLA"
]

# rumus = ["LUAS", "KELILING", "VOLUME", "LUAS PERMUKAAN"]

print(r"""
  _____  _  _  _  _       ____                                     
 |  __ \(_)| |(_)| |     |  _ \                                    
 | |__) |_ | | _ | |__   | |_) |  __ _  _ __    __ _  _   _  _ __  
 |  ___/| || || || '_ \  |  _ <  / _` || '_ \  / _` || | | || '_ \ 
 | |    | || || || | | | | |_) || (_| || | | || (_| || |_| || | | |
 |_|    |_||_||_||_| |_| |____/  \__,_||_| |_| \__, | \__,_||_| |_|
                                                __/ |              
                                               |___/               
""")

# Input - Bangun Datar / Bangun Ruang.
while True:
        input_bangun = str(input("Masukkan pilihan bangun - Datar / Ruang: ")).upper()
        if input_bangun in bangun:
            if input_bangun == "DATAR":
                print("🔧 Bangun Datar Belum Tersedia")
                continue
            break
        else:
            print("📢 Pilihan tidak ada, silakan pilih kembali!")
            continue

# Input - Bangun Ruang.
while True:
    if input_bangun == "RUANG":
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

if input_bangun_ruang == "KUBUS":
    print(r"""
  _  __      _              
 | |/ /_  _ | |__  _  _  ___
 | ' <| || || '_ \| || |(_-<
 |_|\_\\_,_||_.__/ \_,_|/__/
                            
""")

# Sisi Kubus.
while input_bangun_ruang == "KUBUS":
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

if input_bangun_ruang == "BALOK":
    print(r"""
  ___        _       _   
 | _ ) __ _ | | ___ | |__
 | _ \/ _` || |/ _ \| / /
 |___/\__,_||_|\___/|_\_\
                         
""")

# Panjang Balok.
while input_bangun_ruang == "BALOK":
    try:
        panjang_balok = float(input("Masukkan Panjang Balok: "))
        break
    except ValueError:
        print("📌 Panjang Tidak Valid, silakan coba lagi!")
        continue

# Lebar Balok.
while input_bangun_ruang == "BALOK":
    try:
        lebar_balok = float(input("Masukkan Lebar Balok: "))
        break
    except ValueError:
        print("📌 Lebar Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Balok.
while input_bangun_ruang == "BALOK":
    try:
        tinggi_balok = float(input("Masukkan Tinggi Balok: "))
        break
    except ValueError:
        print("📌 Tinggi Tidak Valid, silakan coba lagi!")
        continue

# Hasil Balok.
if input_bangun_ruang == "BALOK":
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

if input_bangun_ruang == "PRISMA":
    print(r"""
  ___       _                  
 | _ \ _ _ (_) ___ _ __   __ _ 
 |  _/| '_|| |(_-<| '  \ / _` |
 |_|  |_|  |_|/__/|_|_|_|\__,_|
                               
""")

# Luas Alas Prisma.
while input_bangun_ruang == "PRISMA":
    try:
        luas_alas_prisma = float(input("Masukkan Luas Alas Prisma: "))
        break
    except ValueError:
        print("📌 Luas Alas Tidak Valid, silakan coba lagi!")
        continue

# Keliling Alas Prisma.
while input_bangun_ruang == "PRISMA":
    try:
        keliling_alas_prisma = float(input("Masukkan Keliling Alas Prisma: "))
        break
    except ValueError:
        print("📌 Keliling Alas Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Prisma.
while input_bangun_ruang == "PRISMA":
    try:
        tinggi_prisma = float(input("Masukkan Tinggi Prisma: "))
        break
    except ValueError:
        print("📌 Tinggi Tidak Valid, silakan coba lagi!")
        continue

if input_bangun_ruang == "PRISMA":
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

if input_bangun_ruang == "LIMAS":
    print(r"""
  _     _                  
 | |   (_) _ __   __ _  ___
 | |__ | || '  \ / _` |(_-<
 |____||_||_|_|_|\__,_|/__/
                           
""")

# Luas Alas Limas.
while input_bangun_ruang == "LIMAS":
    try:
        luas_alas_limas = float(input("Masukkan Luas Alas Limas: "))
        break
    except ValueError:
        print("📌 Luas Alas Tidak Valid, silakan coba lagi!")
        continue

# Keliling Alas Limas.
while input_bangun_ruang == "LIMAS":
    try:
        keliling_alas_limas = float(input("Masukkan Keliling Alas Limas: "))
        break
    except ValueError:
        print("📌 Keliling Alas Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Sisi Tegak Limas.
while input_bangun_ruang == "LIMAS":
    try:
        sisi_tegak_limas = float(input("Masukkan Tinggi Sisi Tegak Limas: "))
        break
    except ValueError:
        print("📌 Tinggi Sisi Tegak Tidak Valid, silakan coba lagi!")
        continue

# Tinggi Limas.
while input_bangun_ruang == "LIMAS":
    try:
        tinggi_limas = float(input("Masukkan Tinggi Limas: "))
        break
    except ValueError:
        print("📌 Tinggi Tidak Valid, silakan coba lagi!")
        continue

if input_bangun_ruang == "LIMAS":
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

if input_bangun_ruang == "TABUNG":
    print(r"""
  _____       _                      
 |_   _|__ _ | |__  _  _  _ _   __ _ 
   | | / _` || '_ \| || || ' \ / _` |
   |_| \__,_||_.__/ \_,_||_||_|\__, |
                               |___/ 
""")

# Jari-Jari Tabung.
while input_bangun_ruang == "TABUNG":
    try:
        jari_tabung = float(input("Masukkan Jari-Jari Tabung: "))
        break
    except ValueError:
        print("🔥 Jari-Jari tidak dikenal, silakan coba lagi!")
        continue

# Tinggi Tabung.
while input_bangun_ruang == "TABUNG":
    try:
        tinggi_tabung = float(input("Masukkan Tinggi Tabung: "))
        break
    except ValueError:
        print("🔥 Tinggi tidak dikenal, silakan coba lagi!")
        continue

# Hasil Tabung
if input_bangun_ruang == "TABUNG":
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

if input_bangun_ruang == "KERUCUT":
    print(r"""
  _  __                           _   
 | |/ / ___  _ _  _  _  __  _  _ | |_ 
 | ' < / -_)| '_|| || |/ _|| || ||  _|
 |_|\_\\___||_|   \_,_|\__| \_,_| \__|
                                      
""")
    
# Jari-Jari Kerucut.
while input_bangun_ruang == "KERUCUT":
    try:
        jari_kerucut = float(input("Masukkan Jari-Jari Kerucut: "))
        break
    except ValueError:
        print("🔥 Jari-Jari tidak dikenal, silakan coba lagi!")
        continue

# Tinggi Kerucut.
while input_bangun_ruang == "KERUCUT":
    try:
        tinggi_kerucut = float(input("Masukkan Tinggi Kerucut: "))
        break
    except ValueError:
        print("🔥 Tinggi tidak dikenal, silakan coba lagi!")
        continue

# Hasil Kerucut
if input_bangun_ruang == "KERUCUT":
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

if input_bangun_ruang == "BOLA":
    print(r"""
  ___       _       
 | _ ) ___ | | __ _ 
 | _ \/ _ \| |/ _` |
 |___/\___/|_|\__,_|
                    
""")
    
while input_bangun_ruang == "BOLA":
    try:
        jari_bola = float(input("Masukkan Jari-Jari Bola: "))
        break
    except ValueError:
        print("🔥 Jari-Jari tidak dikenal, silakan coba lagi!")
        continue

# Hasil Bola
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
