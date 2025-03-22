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

total = 0

pilihan_deret = str(input("Masukkan Huruf yang ingin dipilih: ")).lower()
while pilihan_deret not in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"):
    print("✨ Tolong masukkan huruf yang benar! ✨")
    pilihan_deret = str(input("Masukkan Huruf yang ingin dipilih: ")).lower()

# A. Normal.
if pilihan_deret == "a":
    print("\nBilangan Berurutan\n")
    for i in range(1, 11):
        print(i)

# B. Normal tapi kebalik.
elif pilihan_deret == "b":
    print("\nBilangan Berurutan Tapi Kebalik\n")
    for i in range(10, -1, -1):
        print(i)

# C. Deret Kuadrat Dari Bilangan Asli.
elif pilihan_deret == "c":
    print("\nDeret Kuadrat Dari Bilangan Asli")
    print("Rumus: Un = n²\n")
    for i in range(1, 11):
        print(i ** 2)

# D. Deret Bilangan Ganjil.
elif pilihan_deret == "d":
    print("\nBilangan Ganjil")
    print("Rumus: Un = 2n - 1\n")
    for i in range(1, 11):
        print(2 * i - 1)

# E. Deret Bilangan Genap
elif pilihan_deret == "e":
    print("\nBilangan Genap")
    print("Rumus: Un = 2(n - 1) - 1\n")
    for i in range(1, 11):
        print(2 * (i - 1))

# F. Deret dengan beda 3 angka.
elif pilihan_deret == "f":
    print("\nDeret dengan beda 3 angka")
    print("Rumus: Un = 3n - 2\n")
    for i in range(1, 11):
        print(3 * i - 2)

# G. Deret Kuadrat Terbalik Dari Bilangan Asli.
elif pilihan_deret == "g":
    print("\nDeret Kuadrat Terbalik")
    print("Rumus: Un = (11 - n)²\n")
    for i in range(1, 11):
        print((11 - i) ** 2)

# H. Deret Aritmatika Menurun dengan pengurangan -5.
elif pilihan_deret == "h":
    print("\nDeret Aritmatika Menurun")
    print("Rumus: Un = 65 - 5n\n")
    for i in range(1, 11):
        print(65 - 5 * i)

# I. Deret Bilangan Segitiga.
elif pilihan_deret == "i":
    print("\nDeret Bilangan Segitiga")
    print("Rumus: Un = n(n + 1) / 2\n")
    for i in range(1, 11):
        print(f"{i * (i + 1) / 2:.0f}")

# J. Deret Bilangan Faktorial.
elif pilihan_deret == "j":
    print("\nDeret Bilangan Faktorial")
    print("Rumus: Un = n!\n")
    faktorial = 1
    for i in range(1, 11):
        faktorial *= i
        print(faktorial)
