print("""
  ___                  _     ___  _  _                               
 |   \  ___  _ _  ___ | |_  | _ )(_)| | __ _  _ _   __ _  __ _  _ _  
 | |) |/ -_)| '_|/ -_)|  _| | _ \| || |/ _` || ' \ / _` |/ _` || ' \ 
 |___/ \___||_|  \___| \__| |___/|_||_|\__,_||_||_|\__, |\__,_||_||_|
                                                   |___/             """)
print("""
Deret bilangan :
    a. 1 2 3 4 5 6 7 8 9 10
    b. 10 9 8 7 6 5 4 3 2 1 0
    c. 1 4 9 16 25 36 49 64 81 100
    d. 1 3 5 7 9 11 13 15
    e. 0 2 4 6 8 10 12 14 16
    f. 1 4 7 10 13 16 19 22
    g. 100 81 64 49 36 25 16 9 4 1 0
    h. 60 55 50 45 40 35 30 25 20 15 10
    i. 1 3 6 10 15 21 28 36 45 55
    j. 1 2 6 24 120 720 5040 40320 362880 3628800
""")

pilihan_deret = str(input("Masukkan Huruf yang ingin dipilih: ")).lower()
while pilihan_deret not in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"):
    print("✨ Tolong masukkan huruf yang benar! ✨")
    pilihan_deret = str(input("Masukkan Huruf yang ingin dipilih: ")).lower()

# A. Normal.
if pilihan_deret == "a":
    print("\n「 Bilangan Berurutan 」\n")
    while pilihan_deret == "a":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print(i, end=" ")

# B. Normal tapi kebalik.
elif pilihan_deret == "b":
    print("\n「 Bilangan Berurutan Tapi Kebalik 」\n")
    while pilihan_deret == "b":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print(11 - 1 * i, end=" ")

# C. Deret Kuadrat Dari Bilangan Asli.
elif pilihan_deret == "c":
    print("\n「 Deret Kuadrat Dari Bilangan Asli 」")
    print("Rumus: Un = n²\n")
    while pilihan_deret == "c":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print(i ** 2, end=" ")

# D. Deret Bilangan Ganjil.
elif pilihan_deret == "d":
    print("\n「 Bilangan Ganjil 」")
    print("Rumus: Un = 2n - 1\n")
    while pilihan_deret == "d":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print(2 * i - 1, end=" ")

# E. Deret Bilangan Genap
elif pilihan_deret == "e":
    print("\n「 Bilangan Genap 」")
    print("Rumus: Un = 2(n - 1) - 1\n")
    while pilihan_deret == "e":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print(2 * (i - 1), end=" ")

# F. Deret dengan beda 3 angka.
elif pilihan_deret == "f":
    print("\nDeret dengan beda 3 angka")
    print("Rumus: Un = 3n - 2\n")
    while pilihan_deret == "f":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print(3 * i - 2, end=" ")

# G. Deret Kuadrat Terbalik Dari Bilangan Asli.
elif pilihan_deret == "g":
    print("\nDeret Kuadrat Terbalik")
    print("Rumus: Un = (11 - n)²\n")
    while pilihan_deret == "g":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print((11 - i) ** 2, end=" ")

# H. Deret Aritmatika Menurun dengan pengurangan -5.
elif pilihan_deret == "h":
    print("\nDeret Aritmatika Menurun")
    print("Rumus: Un = 65 - 5n\n")
    while pilihan_deret == "h":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print(65 - 5 * i, end=" ")

# I. Deret Bilangan Segitiga.
elif pilihan_deret == "i":
    print("\nDeret Bilangan Segitiga")
    print("Rumus: Un = n(n + 1) / 2\n")
    while pilihan_deret == "i":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    for i in range(1, angka + 1):
        print(f"{i * (i + 1) / 2:.0f}", end=" ")

# J. Deret Bilangan Faktorial.
elif pilihan_deret == "j":
    print("\nDeret Bilangan Segitiga")
    print("Rumus: Un = n!\n")
    while pilihan_deret == "j":
        try:
            angka = int(input("Masukkan Berapa Deret: "))
            break
        except ValueError:
            print("🚨 Masukkan Jumlah Deret Dengan Benar!")
            continue
    faktorial = 1
    for i in range(1, angka + 1):
        faktorial *= i
        print(faktorial, end=" ")
