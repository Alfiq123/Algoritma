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

# Referensi Rumus

# Persegi:
# • Luas: sisi x sisi
# • Keliling: 4 x sisi

# Persegi Panjang
# • Luas: panjang x lebar
# • Keliling: 2 x (panjang + lebar)

# List untuk memisahkan
bangun = ["DATAR", "RUANG"]
bangun_datar = [
    "PERSEGI", "PERSEGI PANJANG", "SEGITIGA", "LINGKARAN",
    "TRAPESIUM", "JAJAR GENJANG", "LINGKARAN", "BELAH KETUPAT"
    ]
bangun_ruang = [
    "KUBUS", "BALOK", "PRISMA", "LIMAS",
    "TABUNG", "KERUCUT", "BOLA"
]

#   ____                                  _____        _               #
#  |  _ \                                |  __ \      | |              #
#  | |_) | __ _ _ __   __ _ _   _ _ __   | |  | | __ _| |_ __ _ _ __   #
#  |  _ < / _` | '_ \ / _` | | | | '_ \  | |  | |/ _` | __/ _` | '__|  #
#  | |_) | (_| | | | | (_| | |_| | | | | | |__| | (_| | || (_| | |     #
#  |____/ \__,_|_| |_|\__, |\__,_|_| |_| |_____/ \__,_|\__\__,_|_|     #
#                      __/ |                                           #
#                     |___/                                            #

# Input - Bangun Datar / Bangun Ruang
while True:
        input_bangun = str(input("Masukkan pilihan bangun - datar / ruang: ")).upper()
        if input_bangun in bangun:
            break
        else:
            print("📢 Pilihan tidak ada, silakan pilih kembali!")

# Input - Bangun Datar
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
        input_bangun_datar = str(input("Masukkan Pilihan Bangun Datar: "))
        if input_bangun_datar in bangun_datar:
            break
        else:
            print("📢 Bangun datar tidak ada yang terpilih, silakan pilih kembali!")
            continue