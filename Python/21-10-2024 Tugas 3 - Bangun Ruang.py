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
