import math

# 1. Semua angka yang habis membagi suatu bilangan.
# Misal: Bilangan = 10 → 1, 2, 5, 10

# 2. Kelipatan Persekutuan Kecil (KPK) dari Bilangan1 & Bilangan2.
# Misal: Bilangan1 = 5, Bilangan2 = 14 → KPK = 35

# 3. Faktor Persekutuan Besar (FPB) dari Bilangan1 & Bilangan2.
# Misal: Bilangan1 = 100, Bilangan2 = 80 → FPB = 10

# 4. Semua angka kelipatan Bilangan antara Awal & Akhir.
# Misal: Bilangan = 5, Awal = 73, Akhir = 97 → 75 80 85 90 95

# 5. Semua angka kelipatan Bilangan (besar ke kecil) antara Awal dan Akhir.
# Misal: Bilangan = 5, Awal = 97, Akhir = 73 → 95 90 85 80 75

# 6. Semua angka kelipatan Bilangan antara Awal & Akhir. Jika Awal tampilkan dari kecil ke besar, 
# dan jika Awal lebih besar dari Akhir maka tampilkan dari besar ke kecil.
# Misal: Bilangan = 5, Awal = 73, Akhir = 97 → 75 80 85 90 95
#        Bilangan = 5, Awal = 97, Akhir = 73 → 95 90 85 80 75

soal_valid = (1, 2, 3, 4, 5, 6)

print(r"""
Soal Gabungan, Pilih Salah Satu.

    1. Semua Angka Yang Habis Membagi Suatu Bilangan
    2. Kelipatan Persekutuan Kecil
    3. Faktor Persekutuan Besar
    4. Semua Angka Kelipatan Bilangan (Kecil ke Besar)
    5. Semua Angka Kelipatan Bilangan (Besar ke Kecil)
    6. Semua Angka Kelipatan Bilangan (Gabungan)
""")

pilihan_soal = int(input("Silahkan Pilih Soal yang Tersedia: "))
while pilihan_soal not in soal_valid:
    print("❗ Kamu memasukkan soal yang tidak tersedia, silakan masukkan lagi")
    pilihan_soal = int(input("Silahkan Pilih Soal yang Tersedia: "))

# Soal Nomor 1. Angka yang habis membagi.
while pilihan_soal == 1:
    print()
    print("「 Semua angka yang habis membagi suatu bilangan 」")
    print()

    while True:
        try:
            bilangan_soal_1 = int(input("Masukkan angka: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    for i in range(1, bilangan_soal_1 + 1):
        if bilangan_soal_1 % i == 0:
            print(i)

    while True:
        ulang_soal = input("Apakah kamu ingin mengulangi perhitungan ini lagi? (ya/tidak): ").lower()
        if ulang_soal in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_soal in ('tidak', 't'):
        print("🙏 Terima kasih sudah menggunakan program ini 🙏")
        break

# Soal Nomor 2. KPK.
while pilihan_soal == 2:
    print()
    print("「 Kelipatan Persekutuan Kecil 」")
    print()

    while True:
        try:
            bilangan_soal_2a = int(input("Masukkan bilangan pertama: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    while True:
        try:
            bilangan_soal_2b = int(input("Masukkan bilangan kedua: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    print(f"""
────────────────────────────────────────
KPK dari {bilangan_soal_2a} dan {bilangan_soal_2b} adalah: {math.lcm(bilangan_soal_2a, bilangan_soal_2b)}
────────────────────────────────────────
    """)

    while True:
        ulang_soal = input("Apakah kamu ingin mengulangi perhitungan ini lagi? (ya/tidak): ").lower()
        if ulang_soal in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_soal in ('tidak', 't'):
        print("🙏 Terima kasih sudah menggunakan program ini 🙏")
        break

# Soal Nomor 3. FPB.
while pilihan_soal == 3:
    print()
    print("「 Faktor Persekutuan Besar 」")
    print()

    while True:
        try:
            bilangan_soal_3a = int(input("Masukkan bilangan pertama: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    while True:
        try:
            bilangan_soal_3b = int(input("Masukkan bilangan kedua: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    print(f"""
────────────────────────────────────────
FPB dari {bilangan_soal_3a} dan {bilangan_soal_3b} adalah: {math.gcd(bilangan_soal_3a, bilangan_soal_3b)}
────────────────────────────────────────
    """)

    while True:
        ulang_soal = input("Apakah kamu ingin mengulangi perhitungan ini lagi? (ya/tidak): ").lower()
        if ulang_soal in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_soal in ('tidak', 't'):
        print("🙏 Terima kasih sudah menggunakan program ini 🙏")
        break

# Soal Nomor 4. Angka kelipatan kecil ke besar.
while pilihan_soal == 4:
    print()
    print("「 Semua Angka Kelipatan Bilangan (kecil ke besar) 」")
    print()

    while True:
        try:
            bilangan = int(input("Masukkan angka: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    while True:
        try:
            bilangan_awal = int(input("Masukkan bilangan awal: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    while True:
        try:
            bilangan_akhir = int(input("Masukkan bilangan akhir: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    if bilangan_awal > bilangan_akhir:
        print()
        print("💥 Bilangan awal harus lebih kecil dari bilangan akhir")
        continue

    for i in range(bilangan_awal, bilangan_akhir + 1):
        if i % bilangan == 0:
            print(i)

    while True:
        ulang_soal = input("Apakah kamu ingin mengulangi perhitungan ini lagi? (ya/tidak): ").lower()
        if ulang_soal in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_soal in ('tidak', 't'):
        print("🙏 Terima kasih sudah menggunakan program ini 🙏")
        break

# Soal Nomor 5. Angka kelipatan besar ke kecil.
while pilihan_soal == 5:
    print()
    print("「 Semua Angka Kelipatan Bilangan (Besar ke kecil) 」")
    print()

    while True:
        try:
            bilangan = int(input("Masukkan angka: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    while True:
        try:
            bilangan_awal = int(input("Masukkan bilangan awal: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    while True:
        try:
            bilangan_akhir = int(input("Masukkan bilangan akhir: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    if bilangan_awal < bilangan_akhir:
        print()
        print("💥 Bilangan awal harus lebih besar dari bilangan akhir")
        continue

    for i in reversed(range(bilangan_akhir, bilangan_awal + 1)):
        if i % bilangan == 0:
            print(i)

    while True:
        ulang_soal = input("Apakah kamu ingin mengulangi perhitungan ini lagi? (ya/tidak): ").lower()
        if ulang_soal in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_soal in ('tidak', 't'):
        print("🙏 Terima kasih sudah menggunakan program ini 🙏")
        break

#  Soal Nomor 6. Angka kelipatan Gabungan.
while pilihan_soal == 6:
    print()
    print("「 Semua Angka Kelipatan Bilangan (Gabungan) 」")
    print()

    while True:
        try:
            bilangan = int(input("Masukkan angka: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    while True:
        try:
            bilangan_awal = int(input("Masukkan bilangan awal: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    while True:
        try:
            bilangan_akhir = int(input("Masukkan bilangan akhir: "))
        except ValueError:
            print("🔥 Kamu memasukkan karakter lain ")
            continue
        break

    print("────────────────────────────────────────")

    for i in range(bilangan_awal, bilangan_akhir + 1):
        if i % bilangan == 0:
            print(i, end=" ")

    for i in reversed(range(bilangan_akhir, bilangan_awal + 1)):
        if i % bilangan == 0:
            print(i, end=" ")

    print()
    print()

    while True:
        ulang_soal = input("Apakah kamu ingin mengulangi perhitungan ini lagi? (ya/tidak): ").lower()
        if ulang_soal in ('ya', 'tidak','y', 't'):
            break
        else:
            print("📢 Pilihannya antara 'ya' atau 'tidak''")

    if ulang_soal in ('tidak', 't'):
        print("🙏 Terima kasih sudah menggunakan program ini 🙏")
        break
