# Buatlah program dengan perulangan untuk melakukan operasi hitung:
# 1. Bilangan Berpangkat
# 2. Hasil Akar Bilangan
# 3. Sisa hasil bagi 2 bilangan
# 4. Benar atau salah suatu pernyataan (Operator Kondisi / Ternary)

import math

nomor_pilihan = ("1", "2", "3", "4")

# Pembukaan.
print(r"""
Program untuk melakukan operasi hitung:
    1. Bilangan Berpangkat
    2. Hasil Akar Bilangan
    3. Sisa hasil bagi 2 bilangan
    4. Benar atau salah suatu pernyataan (Operator Kondisi / Ternary)
""")

while True:
    input_nomor = str(input("Masukkan Nomor Soal (1 / 2 / 3 / 4): "))
    if input_nomor not in nomor_pilihan:
        print("🚫 Masukkan Nomor yang sesuai🚫 ")
        continue
    break

# Area Nomor 1 - Bilangan Berpangkat.
while input_nomor == "1":
    print()
    print("「 Menghitung bilangan pangkat 」")
    print()

    while True:
        try:
            bilangan_pangkat = int(input("Masukkan angka: "))
        except ValueError:
            print("🚫 Kamu memasukkan huruf atau karakter lain 🚫")
            continue
        break

    while True:
        try:
            pangkat = int(input("Masukkan pangkat: "))
        except ValueError:
            print("🚫 Kamu memasukkan huruf atau karakter lain 🚫")
            continue
        break

    print()
    print("────────────────────────────────────────────────")
    print(f"Hasil dari {bilangan_pangkat} pangkat {pangkat} adalah: {bilangan_pangkat ** pangkat:,.0f}")
    print("────────────────────────────────────────────────")
    print()

    while True:
        ulang_nomor_1 = input("Apakah kamu ingin mengulanginya lagi? (ya / tidak): ").lower()
        if ulang_nomor_1 in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_nomor_1 in ('tidak', 't'):
        print("👋 Selamat tinggal 👋")
        break

# Area Nomor 2 - Akar Bilangan.
while input_nomor == "2":
    print()
    print("「 Hasil Akar Bilangan 」")
    print()

    while True:
        try:
            bilangan_akar = int(input("Masukkan angka: "))
        except ValueError:
            print("⛔ Kamu memasukkan huruf atau karakter lain ⛔")
            continue
        break

    print()
    print("────────────────────────────────────────")
    print(f"Akar bilangan dari {bilangan_akar} adalah: {math.sqrt(bilangan_akar):.2f}")
    print("────────────────────────────────────────")
    print()

    while True:
        ulang_nomor_2 = input("Apakah kamu ingin mengulanginya lagi? (ya / tidak): ").lower()
        if ulang_nomor_2 in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_nomor_2 in ('tidak', 't'):
        print("👋 Selamat tinggal 👋")
        break

# Area Nomor 3 - Sisa hasil bagi 2 bilangan.
while input_nomor == "3":
    print()
    print("「 Sisa hasil bagi 2 bilangan 」")
    print()

    while True:
        try:
            bilangan_sisa_1 = int(input("Masukkan angka pertama: "))
        except ValueError:
            print("⛔ Kamu memasukkan huruf atau karakter lain ⛔")
            continue
        break

    while True:
        try:
            bilangan_sisa_2 = int(input("Masukkan angka kedua: "))
        except ValueError:
            print("🚧 Kamu memasukkan huruf atau karakter lain 🚧")
            continue
        break

    print()
    print("────────────────────────────────────────")
    print(f"Sisa dari {bilangan_sisa_1} dibagi {bilangan_sisa_2} adalah: {bilangan_sisa_1 % bilangan_sisa_2:,.0f}")
    print("────────────────────────────────────────")
    print()

    while True:
        ulang_nomor_3 = input("Apakah kamu ingin mengulanginya lagi? (ya / tidak): ").lower()
        if ulang_nomor_3 in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_nomor_3 in ('tidak', 't'):
        print("👋 Selamat tinggal 👋")
        break

# Soalnya bikin bingung...
# Area Nomor 4 - Benar atau salah suatu pernyataan (Operator Kondisi / Ternary).
if input_nomor == "4":
    print()
    print("「 Benar atau salah suatu pernyataan 」")

    print(r"""
Karena soalnya membingungkan jadi, pilih salah satu:
    1. Bilangan ganjil atau genap
    2. Bilangan positif atau negatif
    3. Bumi datar atau bulat?
""")
    
    nomor_pilihan_4 = ("1", "2", "3")

    while True:
        input_nomor_4 = str(input("Masukkan Nomor Soal (1 / 2 / 3): "))
        if input_nomor_4 not in nomor_pilihan_4:
            print("🚫 Masukkan Nomor yang sesuai🚫 ")
            continue
        break

    while input_nomor_4 == "1":
        print()
        print("「 Bilangan ganjil atau genap 」")
        print()

        while input_nomor_4 == "1":
            try:
                bilangan_gengen = int(input("Masukkan bilangan: "))
            except ValueError:
                print("⚠️ Kamu memasukkan huruf atau karakter lain ⚠️")
                continue
            break

        genap = "Genap" if bilangan_gengen % 2 == 0 else "Ganjil"
        print("────────────────────────────────────────")
        print(bilangan_gengen, "adalah bilangan", genap)
        print("────────────────────────────────────────")

        while True:
            ulang_nomor_41 = input("Apakah kamu ingin mengulanginya lagi? (ya / tidak): ").lower()
            if ulang_nomor_41 in ('ya', 'tidak','y', 't'):
                break
            else:
                print("📢 Pilihannya antara 'ya' atau 'tidak''")
        
        if ulang_nomor_41 in ('tidak', 't'):
            print("👋 Selamat tinggal 👋")
            break

    while input_nomor_4 == "2":
        print()
        print("「 Bilangan positif atau negatif 」")
        print()

        while input_nomor_4 == "2":
            try:
                bilangan_posneg = int(input("Masukkan bilangan: "))
            except ValueError:
                print("⚠️ Kamu memasukkan huruf atau karakter lain ⚠️")
                continue
            break

        positif = "Positif" if bilangan_posneg > 0 else "Negatif"
        print("────────────────────────────────────────")
        print(bilangan_posneg, "adalah bilangan", positif)
        print("────────────────────────────────────────")

        while True:
            ulang_nomor_42 = input("Apakah kamu ingin mengulanginya lagi? (ya / tidak): ").lower()
            if ulang_nomor_42 in ('ya', 'tidak','y', 't'):
                break
            else:
                print("📢 Pilihannya antara 'ya' atau 'tidak''")
        
        if ulang_nomor_42 in ('tidak', 't'):
            print("👋 Selamat tinggal 👋")
            break

    while input_nomor_4 == "3":
        print()
        print("「 Bumi datar atau bulat? 」")
        print()

        while input_nomor_4 == "3":
            bumi_bulat = str(input("Masukkan jawaban (Datar / Bulat): ")).lower()

            if bumi_bulat == "bulat":
                print("🌍 Jawaban benar, selamat! 🌍")
                break
            elif bumi_bulat == "datar":
                print("❌ Jawaban salah, belajar lagi! ❌")
                break
            else:
                print("⚠️ Kamu memasukkan huruf atau karakter lain ⚠️")
                continue

        while True:
            ulang_nomor_43 = input("Apakah kamu ingin mengulanginya lagi? (ya / tidak): ").lower()
            if ulang_nomor_43 in ('ya', 'tidak','y', 't'):
                break
            else:
                print("📢 Pilihannya antara 'ya' atau 'tidak''")
        
        if ulang_nomor_43 in ('tidak', 't'):
            print("👋 Selamat tinggal 👋")
            break
