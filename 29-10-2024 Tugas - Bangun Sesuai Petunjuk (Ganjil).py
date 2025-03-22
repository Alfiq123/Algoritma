import math

# Tuple - List Bangun.
bangun = ("DATAR", "RUANG")
bangun_datar = ("1", "BELAH KETUPAT", "2", "SEGITIGA", "3", "LAYANG LAYANG")
bangun_ruang = ("1", "BALOK", "2", "KERUCUT", "3", "PRISMA")

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
   1. Belah Ketupat
   2. Segitiga
      • Segitiga Sama Sisi
      • Segitiga Sama Kaki 
      • Segitiga Siku Siku
      • Segitiga Lancip
   3. Layang Layang
""")

while input_bangun == "DATAR":
    input_bangun_datar = str(input("Masukkan Pilihan Bangun Datar: ")).upper()
    if input_bangun_datar in bangun_datar:
        break
    else:
        print("📢 Bangun datar tidak ada yang terpilih, silakan pilih kembali!")
        continue

# Belah Ketupat.
if input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "1":
    print(r"""
  ___      _      _      _  __    _                   _   
 | _ ) ___| |__ _| |_   | |/ /___| |_ _  _ _ __  __ _| |_ 
 | _ \/ -_) / _` | ' \  | ' </ -_)  _| || | '_ \/ _` |  _|
 |___/\___|_\__,_|_||_| |_|\_\___|\__|\_,_| .__/\__,_|\__|
                                          |_|             """)

# Input - Diagonal 1 Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "1":
    try:
        diagonal1_belah_ketupat = float(input("Masukkan Diagonal 1 Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Diagonal 2 Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "1":
    try:
        diagonal2_belah_ketupat = float(input("Masukkan Diagonal 2 Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Belah Ketupat.
while input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "1":
    try:
        sisi_belah = float(input("Masukkan Sisi Belah Ketupat: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Output - Belah Ketupat.
if input_bangun_datar == "BELAH KETUPAT" or input_bangun_datar == "1":
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

# Segitiga.
if input_bangun_datar == "SEGITIGA" or input_bangun_datar == "2":
    print(r"""
  ___             _  _    _             
 / __| ___  __ _ (_)| |_ (_) __ _  __ _ 
 \__ \/ -_)/ _` || ||  _|| |/ _` |/ _` |
 |___/\___|\__, ||_| \__||_|\__, |\__,_|
           |___/            |___/       """)

# Ini itu cuma hiasan, ndak ada gunanya.
    print(r"""
1. Segitiga Sama Sisi    3. Segitiga Siku Siku
2. Segitiga Sama Kaki    4. Segitiga Lancip
""")

# Kamu ngapain disini?...
list_segitiga = {"1": "Segitiga Sama Sisi", "2": "Segitiga Sama Kaki", "3": "Segitiga Siku Siku", "4": "Segitiga Lancip"}

# Input Jenis Segitiga.
while input_bangun_datar == "SEGITIGA" or input_bangun_datar == "2":
    jenis_segitiga = str(input("Masukkan Jenis Segitiga: ")).upper()
    if jenis_segitiga in list_segitiga:
        print(f"「 {list_segitiga[jenis_segitiga]} 」")
        break
    else:
        print("📢 Masukkan Jenis Segitiga!")
        continue

# Input - Alas Segitiga.
while input_bangun_datar == "SEGITIGA" or input_bangun_datar == "2" and jenis_segitiga in list_segitiga:
    try:
        alas_segitiga = float(input("Masukkan Alas Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Input - Tinggi Segitiga.
while input_bangun_datar == "SEGITIGA" or input_bangun_datar == "2" and jenis_segitiga in list_segitiga:
    try:
        tinggi_segitiga = float(input("Masukkan Tinggi Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Input - Sisi Segitiga.
while input_bangun_datar == "SEGITIGA" or input_bangun_datar == "2" and jenis_segitiga in list_segitiga:
    try:
        sisi_segitiga = float(input("Masukkan Sisi Segitiga: "))
        break
    except ValueError:
        print("📢 Tolong Masukkan Angka!")
        continue

# Output - Segitiga.
if input_bangun_datar == "SEGITIGA" or input_bangun_datar == "2" and jenis_segitiga in list_segitiga:

        print(f"""
======= Luas {list_segitiga[jenis_segitiga]} =======
"Alas Segitiga: {alas_segitiga:,.2f} cm
"Tinggi Segitiga: {tinggi_segitiga:,.2f} cm
"Rumus Luas Segitiga: 1/2 x {alas_segitiga:,.2f} cm x {tinggi_segitiga:.2f} cm
"Luas Segitiga: {0.5 * alas_segitiga * tinggi_segitiga:,.2f} cm²""")
        
        print(f"""
======= Keliling {list_segitiga[jenis_segitiga]} =======
Sisi Segitiga: {sisi_segitiga:,.2f} cm
Rumus Keliling Segitiga: {sisi_segitiga:,.2f} cm + {sisi_segitiga:.2f} cm + {sisi_segitiga:.2f} cm
Keliling Segitiga: {sisi_segitiga * 3:,.2f} cm
""")

# Layang - Layang.
if input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "3":
    print(r"""
  _                               _                             
 | |   __ _ _  _ __ _ _ _  __ _  | |   __ _ _  _ __ _ _ _  __ _ 
 | |__/ _` | || / _` | ' \/ _` | | |__/ _` | || / _` | ' \/ _` |
 |____\__,_|\_, \__,_|_||_\__, | |____\__,_|\_, \__,_|_||_\__, |
            |__/          |___/             |__/          |___/ 
""")

# Input - Diagonal 1 Layang Layang.
while input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "3":
    try:
        diagonal1_layang = float(input("Masukkan Diagonal 1 Layang Layang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Diagonal 2 Layang Layang.
while input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "3":
    try:
        diagonal2_layang = float(input("Masukkan Diagonal 2 Layang Layang: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Layang Layang AB.
while input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "3":
    try:
        sisi_layang_ab = float(input("Masukkan Sisi Layang Layang AB: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Input - Sisi Layang Layang BC.
while input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "3":
    try:
        sisi_layang_bc = float(input("Masukkan Sisi Layang Layang BC: "))
        break
    except ValueError:
        print("🚨 Jangan Memasukkan Karakter Lain Selain Angka!")
        continue

# Output - Layang Layang
if input_bangun_datar == "LAYANG LAYANG" or input_bangun_datar == "3":
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
   1. Balok
   2. Kerucut
   3. Prisma
      • Prisma Segi Empat
      • Prisma Segi Lima
      • Prisma Segi Enam
""")

while input_bangun == "RUANG":
    input_bangun_ruang = str(input("Masukkan Pilihan Bangun Ruang: ")).upper()
    if input_bangun_ruang in bangun_ruang:
        break
    else:
        print("📢 Bangun Ruang tidak ada yang terpilih, silakan pilih kembali!")
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

# Prisma.
if input_bangun_ruang == "PRISMA" or input_bangun_ruang == "3":
    print(r"""
  ___       _                  
 | _ \ _ _ (_) ___ _ __   __ _ 
 |  _/| '_|| |(_-<| '  \ / _` |
 |_|  |_|  |_|/__/|_|_|_|\__,_|
                               
""")

# Sama saja, cuma hiasan.
    print(r"""
1. Prisma Segi Empat    3. Prisma Segi Enam
2. Prisma Segi Lima
""")

list_prisma = {"1": "Prisma Segi Empat", "2": "Prisma Segi Lima", "3": "Prisma Segi Enam"}

# Input Jenis Prisma.
while input_bangun_ruang == "PRISMA" or input_bangun_ruang == "3":
    jenis_prisma = str(input("Masukkan Jenis Prisma: ")).upper()
    if jenis_prisma in list_prisma:
        print(f"「 {list_prisma[jenis_prisma]} 」")
        break
    else:
        print("📢 Masukkan Jenis Prisma!")
        continue

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
======= Luas Permukaan {list_prisma[jenis_prisma]} =======
Luas Alas Prisma: {luas_alas_prisma:,.2f} cm
Keliling Alas Prisma: {keliling_alas_prisma:,.2f} cm
Tinggi Prisma: {tinggi_prisma:,.2f} cm
Rumus Luas Permukaan Prisma: (2 x {luas_alas_prisma:,.2f} cm) + ({keliling_alas_prisma:,.2f} cm x {tinggi_prisma:,.2f} cm)
Luas Permukaan Prisma: {(2 * luas_alas_prisma) + (keliling_alas_prisma * tinggi_prisma):,.2f} cm²

======= Volume {list_prisma[jenis_prisma]} =======
Luas Alas Prisma: {luas_alas_prisma:,.2f} cm
Tinggi Prisma: {tinggi_prisma:,.2f} cm
Rumus Volume Prisma: {luas_alas_prisma:,.2f} cm x {tinggi_prisma:,.2f} cm
Volume Prisma: {luas_alas_prisma * tinggi_prisma:,.2f} cm³
""")
