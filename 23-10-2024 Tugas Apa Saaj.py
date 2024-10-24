# a = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]
# b = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84]
# c = [100, 94, 88, 82, 76, 70, 64, 58, 52, 46]
# d = [35, 28, 21, 14, 7, 0, -7, -14 -21 -28]
# e = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]
# f = [30, 29, 27, 24, 20, 15, 9, 2, -6, -15]
# g = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# # A
# x = 1
# for xa in range(1, 38):
#     print(xa)

# from random import randint

# loop = 0

# while loop < 10:
#     num = 0
#     odd = 0
#     even = 0
#     loop += 1

#     while num < 100:
#         num += 1
#         rand = randint(1, 1000)
#         if rand % 2 == 0:
#             even += 1
#         else:
#             odd += 1    
#     print("Out of 100 Random Numbers, {0} where even and {1} where Odd".format(even, odd))

# total_pembelian = 0  # Variabel untuk menyimpan total semua pembelian

# while True:
#     # Proses pembelian
#     print("Selamat datang di toko kami!")
#     item = input("Masukkan nama barang yang ingin dibeli: ")
#     quantity = int(input(f"Berapa banyak {item} yang ingin dibeli? "))
#     price = float(input(f"Masukkan harga {item}: "))
    
#     total = quantity * price
#     print(f"Total pembelian untuk {quantity} {item} adalah {total}")
    
#     # Tambahkan total pembelian saat ini ke total keseluruhan
#     total_pembelian += total
    
#     # Tanyakan apakah ingin melakukan pembelian lagi
#     ulang = input("Apakah Anda ingin melakukan pembelian lagi? (ya/tidak): ").lower()
    
#     if ulang != "ya":
#         print(f"Terima kasih telah berbelanja! Total keseluruhan pembelian Anda adalah {total_pembelian}")
#         break

# total_pembelian = 0  # Variabel untuk menyimpan total semua pembelian

# while True:
#     # Proses pembelian
#     print("Selamat datang di toko kami!")
#     item = input("Masukkan nama barang yang ingin dibeli: ")
    
#     # Validasi input jumlah barang
#     while True:
#         try:
#             quantity = int(input(f"Berapa banyak {item} yang ingin dibeli? "))
#             break  # Keluar dari loop jika input benar
#         except ValueError:
#             print("Input tidak valid. Masukkan angka untuk jumlah barang.")
    
#     # Validasi input harga barang
#     while True:
#         try:
#             price = float(input(f"Masukkan harga {item}: "))
#             break  # Keluar dari loop jika input benar
#         except ValueError:
#             print("Input tidak valid. Masukkan angka untuk harga barang.")
    
#     total = quantity * price
#     print(f"Total pembelian untuk {quantity:,.0f} {item} adalah {total:,.0f}")
    
#     # Tambahkan total pembelian saat ini ke total keseluruhan
#     total_pembelian += total
    
#     # Tanyakan apakah ingin melakukan pembelian lagi
#     ulang = input("Apakah Anda ingin melakukan pembelian lagi? (ya/tidak): ").lower()
    
#     if ulang != "ya":
#         print(f"Terima kasih telah berbelanja! Total keseluruhan pembelian Anda adalah {total_pembelian:,.0f}")
#         break

# total_pembelian = 0  # Variabel untuk menyimpan total semua pembelian

# while True:
#     # Proses pembelian
#     print("Selamat datang di toko kami!")
#     item = input("Masukkan nama barang yang ingin dibeli: ")
    
#     # Validasi input jumlah barang (harus angka positif)
#     while True:
#         try:
#             quantity = int(input(f"Berapa banyak {item} yang ingin dibeli? "))
#             if quantity <= 0:
#                 print("Jumlah barang harus lebih dari 0. Silakan coba lagi.")
#             else:
#                 break  # Keluar dari loop jika input benar dan positif
#         except ValueError:
#             print("Input tidak valid. Masukkan angka yang benar untuk jumlah barang.")
    
#     # Validasi input harga barang (harus angka positif)
#     while True:
#         try:
#             price = float(input(f"Masukkan harga {item}: "))
#             if price <= 0:
#                 print("Harga barang harus lebih dari 0. Silakan coba lagi.")
#             else:
#                 break  # Keluar dari loop jika input benar dan positif
#         except ValueError:
#             print("Input tidak valid. Masukkan angka yang benar untuk harga barang.")
    
#     total = quantity * price
#     print(f"Total pembelian untuk {quantity:,.0f} {item} adalah {total:,.0f}")
    
#     # Tambahkan total pembelian saat ini ke total keseluruhan
#     total_pembelian += total
    
#     # Tanyakan apakah ingin melakukan pembelian lagi
#     ulang = input("Apakah Anda ingin melakukan pembelian lagi? (ya/tidak): ").lower()
    
#     if ulang != "ya":
#         print(f"Terima kasih telah berbelanja! Total keseluruhan pembelian Anda adalah {total_pembelian:,.0f}")
#         break

total_pembelian = 0  # Variabel untuk menyimpan total semua pembelian
daftar_pembelian = []  # List untuk menyimpan detail setiap pembelian

while True:
    # Proses pembelian
    print("Selamat datang di toko kami!")
    item = input("Masukkan nama barang yang ingin dibeli: ")
    
    # Validasi input jumlah barang (harus angka positif)
    while True:
        try:
            quantity = int(input(f"Berapa banyak {item} yang ingin dibeli? "))
            if quantity <= 0:
                print("Jumlah barang harus lebih dari 0. Silakan coba lagi.")
            else:
                break  # Keluar dari loop jika input benar dan positif
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar untuk jumlah barang.")
    
    # Validasi input harga barang (harus angka positif)
    while True:
        try:
            price = float(input(f"Masukkan harga {item}: "))
            if price <= 0:
                print("Harga barang harus lebih dari 0. Silakan coba lagi.")
            else:
                break  # Keluar dari loop jika input benar dan positif
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar untuk harga barang.")
    
    total = quantity * price
    print(f"Total pembelian untuk {quantity:,.0f} {item} adalah {total:,.0f}")
    
    # Simpan pembelian ini ke dalam list
    daftar_pembelian.append({
        'nama_barang': item,
        'jumlah': quantity,
        'harga_satuan': price,
        'total_harga': total
    })
    
    # Tambahkan total pembelian saat ini ke total keseluruhan
    total_pembelian += total
    
    # Tanyakan apakah ingin melakukan pembelian lagi
    ulang = input("Apakah Anda ingin melakukan pembelian lagi? (ya/tidak): ").lower()
    
    if ulang != "ya":
        print(f"\nRingkasan pembelian Anda:")
        for pembelian in daftar_pembelian:
            print(f" - {pembelian['nama_barang']}: {pembelian['jumlah']} x {pembelian['harga_satuan']} = {pembelian['total_harga']}")
        print(f"\nTotal keseluruhan pembelian Anda adalah {total_pembelian:,.0f}")
        print("Terima kasih telah berbelanja!")
        break
