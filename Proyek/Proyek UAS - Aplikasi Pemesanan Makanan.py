menu_makanan = {
    "Makanan": {
        "Nasi Goreng Spesial": 45000,
        "Ayam Bakar Madu": 55000,
        "Steak Sapi Blackpepper": 90000,
        "Ikan Bakar Sambal Matah": 65000,
        "Spaghetti Carbonara": 50000,
        "Pizza Margherita (Medium)": 85000,
        "Rendang Daging Sapi": 75000,
        "Soto Ayam": 40000,
    },

    "Minuman": {
        "Air Mineral": 10000,
        "Es Teh Manis": 12000,
        "Kopi Latte": 25000,
        "Jus Alpukat": 30000,
        "Milkshake Cokelat": 28000,
        "Lemon Tea": 20000,
        "Smoothie Berry": 35000,
    },

    "Appetizer": {
        "Sup Krim Jamur": 25000,
        "Bruschetta Tomat & Basil": 30000,
        "Lumpia Sayur": 20000,
        "Salad Caesar": 35000,
        "Nachos Keju": 40000,
    },

    "Side_Dish": {
        "Kentang Goreng": 25000,
        "Onion Rings": 28000,
        "Sayur Asem": 18000,
        "Tahu & Tempe Goreng": 20000,
    },

    "Dessert": {
        "Es Krim Cokelat": 25000,
        "Brownies Cokelat": 30000,
        "Pancake Madu": 35000,
        "Puding Mangga": 28000,
        "Cheesecake Strawberry": 40000,
    },
}

# Hanya digunakan untuk memvalidasi pesanan pelanggan.
# 🔑 Key: Menu, 🔒 Value: Harga.
validasi_pesanan = {}

# TODO: 💡 Kenapa tidak dibuat nama dan jumlah pesanan saja?.
# 🔑 Key: Pesanan Pelanggan, 🔒 Value: Total Bayar.
pesanan_pelanggan = {}

# # 💳 Total Pembayaran.
# total_bayar = 0

# Banner.
print(r"""
  ___        _                       ___           _                          _                _   
 | _ \___ __| |_ ___ _ _ __ _ _ _   / __| __ _ _ _| |_ __ _ _ __  __ _ _ _   | |   ___ _____ _| |_ 
 |   / -_|_-<  _/ _ \ '_/ _` | ' \  \__ \/ _` | ' \  _/ _` | '_ \/ _` | ' \  | |__/ -_)_ / _` |  _|
 |_|_\___/__/\__\___/_| \__,_|_||_| |___/\__,_|_||_\__\__,_| .__/\__,_|_||_| |____\___/__\__,_|\__|
                                                           |_|                                     
""")

print("───────────────────────── Menu ─────────────────────────")

for kategori, menu_dan_harga in menu_makanan.items():
    print(f"Kategori: {kategori}")

    for menu, harga in menu_dan_harga.items():
        # validasi_pesanan.append(menu)
        validasi_pesanan[menu] = harga

        # placeholder[menu] = harga
        
        print(f" • {menu:40} - Rp. {harga:,}")

    print()

print("────────────────────────────────────────────────────────")

# "Fungsi" untuk memesan makanan.
def pemesanan_menu():
    while True:
        pesanan = str(input("Masukkan pesanan Anda ('x' untuk keluar): ")).title()

        if pesanan == "X":
            print("\n🛍️ Terima kasih sudah berbelanja!\n")
            break

        if pesanan not in validasi_pesanan.keys():
            print("\n🔎 Maaf, menu tersebut tidak tersedia.\n")

        # else:
        #     for kategori, menu_dan_harga in menu_makanan.items():

        #         for menu, harga in menu_dan_harga.items():

        #             if pesanan == menu:
        #                 pesanan_pelanggan[menu] = harga
        #                 print(f"\n📋 Berhasil Menambahkan {menu} ke Dalam Pesanan Anda!\n")

        if pesanan in validasi_pesanan.keys():
            try:
                jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

                if jumlah_pesanan <= 0:
                    print("\n🚨 Jumlah Pesanan Harus Lebih Dari 0\n")
                    continue

                elif jumlah_pesanan >= 0:

                    # print("\n🛒 Dafter Pesanan Anda:")
                    # for pesanan, bayar in pesanan_pelanggan.items():
                    #     print(f"• {pesanan:10} x {jumlah_pesanan}")
                    # continue

                    for kategori, menu_dan_harga in menu_makanan.items():
                        for menu, harga in menu_dan_harga.items():
                            if pesanan == menu:
                                pesanan_pelanggan[menu] = jumlah_pesanan
                                print(f"\n📋 Berhasil Menambahkan {menu} ke Dalam Pesanan Anda!\n")

                    print("🛒 Daftar Pesanan Anda:")
                    for pesanan, bayar in pesanan_pelanggan.items():
                        print(f"• {pesanan:} x {bayar}")
                        continue
                    print()

                # if pesanan in pesanan_pelanggan:
                #     # Jika sudah ada, tambahkan jumlahnya
                #     pesanan_pelanggan[pesanan][1] += jumlah_pesanan
                # else:
                #     # Jika belum ada, tambahkan dengan harga dan jumlah
                #     pesanan_pelanggan[pesanan] = [validasi_pesanan[pesanan], jumlah_pesanan]

            except ValueError:
                print("\n🚨 Masukkan Jumlah Pesanan dengan angka, Silakan ulang kembali!\n")
                continue

    # # 💳 Total Pembayaran.
    # total_bayar = 0
    # for pesanan, bayar in pesanan_pelanggan.items():
    #     print(f"• {pesanan:10} x {jumlah_pesanan} - Rp. {bayar * jumlah_pesanan:,}")
    #     total_bayar += bayar * jumlah_pesanan
    # print(f"\nTotal Bayar: Rp. {total_bayar:,}")

        # 💳 Total Pembayaran.

    total_bayar = 0
    print("\n🛒 Daftar Pesanan Anda:")
    for pesanan, (harga, jumlah) in pesanan_pelanggan.items():
        print(f"• {pesanan:10} x {jumlah} - Rp. {harga * jumlah:,}")
        total_bayar += harga * jumlah

pemesanan_menu()

    # if pesanan not in validasi_pesanan:
    #     print("Maaf, pesanan Anda tidak tersedia.")
    #     continue
    # elif pesanan == "":
    #     break
    # jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    # for kategori, items in menu_makanan.items():
    #     for item, harga in items.items():
    #         if pesanan == item:
    #             # pesanan_pelanggan.append((item, harga))
    #             pesanan_pelanggan[item] = harga
    #             print(f"\n📋 Berhasil menambahkan {item} ke dalam pesanan Anda!\n")
    #             break

    # if pesanan == "":
    #     print("🛒 Terima kasih telah berbelanja!")
    #     break

    # elif menu_makanan.items() is not None:
        # print("Ada")
        # print("Pesanan tidak ditemukan. Silakan coba lagi.")
        # pesanan_pelanggan.append(pesanan)

# print(pesanan_pelanggan)

# for item, harga in pesanan_pelanggan.items():
#     print(f"• {item:40} - Rp. {harga:,}")




# list_kosong = {}

# while True:
#     pesanan_pelanggan = str(input("Masukkan Pesanan Pelanggan: ")).title()

#     ada = False
#     for kategori in menu_makanan:
#         if pesanan_pelanggan in menu_makanan[kategori]:
#             ada = True
#             print(f"Pesanan '{pesanan_pelanggan}' tersedia dengan harga: {menu_makanan[kategori][pesanan_pelanggan]}")
#             break

#     if not ada:
#         print("Pesanan tidak tersedia")
#         continue

#     jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
#     list_kosong[pesanan_pelanggan] = [jumlah_pesanan]
#     print()
#     print("Daftar Pesanan Anda:")

#     for pesanan in list_kosong:
#         kategori = None
#         # Cari kategori menu berdasarkan pesanan
#         for cat, menu in menu_makanan.items():
#             if pesanan in menu:
#                 kategori = cat
#                 break
#         if kategori:
#             harga = menu_makanan[kategori][pesanan]
#             total_harga = harga * list_kosong[pesanan][0]
#             print(f"• {pesanan} x {list_kosong[pesanan][0]} = Rp.{total_harga:,}")
#     print()

# dictionaries = {
#     "Makanan": {
#         1: {"Nasi Goreng" : 10000},
#         2: {"Mie Goreng" : 8000},
#     },

#     "Minuman": {
#         1: {"Jus Apel" : 5000},
#         2: {"Jus Jeruk" : 4000},
#     }
# }

# # Accessing top-level keys
# for category in dictionaries.keys():
#     print(f"Category: {category}")

#     # Accessing second-level keys and values
#     for item_number, item_details in dictionaries[category].items():
#         print(f"{item_number}", end=" ")
        
#         # Accessing third-level keys and values
#         for item_name, price in item_details.items():
#             print(f"- {item_name}: {price}")
            
#     print()

