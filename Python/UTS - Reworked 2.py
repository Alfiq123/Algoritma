import random

print("Soal No 1 - CYMK")
print("Soal No 2 - Mencari Bilangan")

pilih_soal = input("Pilih Soal (A/B): ").upper()

# Soal Nomor 1A.
if pilih_soal == "A":
    print("Warna Cyan + Warna Yellow = Green")

# Soal Nomor 1B.
if pilih_soal == "B":
    warna_1 = input("Masukkan Warna 1: ")
    warna_2 = input("Masukkan Warna 2: ")
    if warna_1 == ("Magenta" and warna_2 == "Yellow") or (warna_1 == "Yellow" and warna_2 == "Magenta"):
        print("Red")
    elif warna_1 == ("Cyan" and warna_2 == "Yellow") or (warna_1 == "Yellow" and warna_2 == "Cyan"):
        print("Green")
    elif warna_1 == ("Cyan" and warna_2 == "Magenta") or (warna_1 == "Magenta" and warna_2 == "Cyan"):
        print("Blue")

    bilangan_1 = int(input("Masukkan Bilangan 1: "))
    bilangan_2 = int(input("Masukkan Bilangan 2: "))
    bilangan_3 = int(input("Masukkan Bilangan 3: "))

    if bilangan_1 < bilangan_2 < bilangan_3:
        print("Urutan Naik")
    elif bilangan_1 > bilangan_2 > bilangan_3:
        print("Urutan Turun")
    else:
        print("Urutan Acak")
