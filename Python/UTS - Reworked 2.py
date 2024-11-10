import random

warna_campuran_1A = ["Warna Cyan + Warna Yellow = Green", "Warna Magenta + Warna Yellow = Red", "Warna Cyan + Warna Magenta = Blue"]

print(r"""
Soal No 1 - CMYK.
        • A) Warna Otomatis
        • B) Campuran 2 Warna

Soal No 2 - Mencari Urutan Bilangan.
""")

input_soal = input("Pilih Nomor Soal (1 / 2): ")

if input_soal == "1":
    input_soal_1 = input("Pilih Soal (A / B): ").upper()
    if input_soal_1 == "A":
        print(random.choice(warna_campuran_1A))

    elif input_soal_1 == "B":
        warna_1 = input("Masukkan Warna 1 (Magenta / Yellow / Cyan): ").capitalize()
        warna_2 = input("Masukkan Warna 2 (Magenta / Yellow / Cyan): ").capitalize()
        if warna_1 == ("Magenta" and warna_2 == "Yellow") or (warna_1 == "Yellow" and warna_2 == "Magenta"):
            print("Red")
        elif warna_1 == ("Cyan" and warna_2 == "Yellow") or (warna_1 == "Yellow" and warna_2 == "Cyan"):
            print("Green")
        elif warna_1 == ("Cyan" and warna_2 == "Magenta") or (warna_1 == "Magenta" and warna_2 == "Cyan"):
            print("Blue")

if input_soal == "2":
    bilangan_1 = int(input("Masukkan Bilangan 1: "))
    bilangan_2 = int(input("Masukkan Bilangan 2: "))
    bilangan_3 = int(input("Masukkan Bilangan 3: "))
    if bilangan_1 < bilangan_2 < bilangan_3:
        print("Urutan Naik")
    elif bilangan_1 > bilangan_2 > bilangan_3:
        print("Urutan Turun")
    else:
        print("Urutan Acak")
