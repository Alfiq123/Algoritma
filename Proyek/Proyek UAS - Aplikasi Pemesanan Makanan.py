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

"""
📝 Fungsi utama di program ini.
"""
def fungsi_utama():
    # Hanya digunakan untuk memvalidasi pesanan pelanggan.
    # 🔑 Key: Menu, 🔒 Value: Harga.
    validasi_pesanan = {}

    # TODO: 💡 Kenapa tidak dibuat nama dan jumlah pesanan saja?.
    # 🔑 Key: Pesanan Pelanggan, 🔒 Value: Total Bayar.
    pesanan_pelanggan = {}

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

    """
    💡 Fitur ini digunakan untuk menginput pesanan pelanggan.
    💡 Perulangan ini juga dapat digunakan untuk melakukan validasi pesanan pelanggan.
    💡 Selain itu, bagian ini juga dapat digunakan untuk menghitung total bayar.
    """
    while True:
        pesanan = str(input("Masukkan pesanan Anda ('X' untuk keluar): ")).title()

        # Jika pelanggan memasukkan "X", maka program akan berhenti.
        if pesanan == "X":
            break

        # Jika pelanggan memasukkan pesanan yang tidak ada di menu, maka program akan menampilkan pesan error.
        # Dan pelanggan dapat mengulangi pemesanan lagi.
        if pesanan not in validasi_pesanan.keys():
            print("\n🔎 Maaf, menu tersebut tidak tersedia.\n")

        """
        </> Kode ini akan memeriksa apakah pesanan yang dimasukkan oleh pelanggan ada dalam daftar menu yang valid. 
            Jika pesanan tidak valid, proses pemesanan tidak akan dilanjutkan.
        """
        if pesanan in validasi_pesanan.keys():
            try:
                jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

                if jumlah_pesanan <= 0:
                    print("\n🚨 Jumlah Pesanan Harus Lebih Dari 0\n")
                    continue

                '''
                📝 Jika pesanan yang diinputkan sama dengan menu yang ada di dictionary, 
                    maka tambahkan ke dalam dictionary pesanan.

                📝 Jika pesanan valid dan jumlah pesanan juga valid, kode ini akan mencari menu yang sesuai dalam struktur data menu_makanan. 
                    Jika ditemukan, pesanan akan ditambahkan ke dalam dictionary pesanan_pelanggan, yang menyimpan jumlah pesanan dan harga.
                '''
                for kategori, menu_dan_harga in menu_makanan.items():
                    for menu, harga in menu_dan_harga.items():
                        if pesanan == menu:
                            pesanan_pelanggan[menu] = [jumlah_pesanan, harga]
                            print(f"\n📋 Berhasil Menambahkan {menu} ke Dalam Pesanan Anda!\n")

                """
                📝 Setelah menambahkan pesanan, kode ini akan menampilkan daftar semua pesanan yang telah dimasukkan oleh pelanggan, 
                    termasuk jumlah masing-masing pesanan.
                """
                print("🛒 Daftar Pesanan Anda:")
                for pesanan, banyak in pesanan_pelanggan.items():
                    print(f"• {pesanan} x {banyak[0]}")
                    continue
                print()

            except ValueError:
                print("\n🚨 Masukkan Jumlah Pesanan dengan angka, Silakan ulang kembali!\n")
                continue

    # 💳 Total Pembayaran.
    if pesanan_pelanggan:
        print("\n───────────────୨ Total Pembayaran ৎ───────────────")
        total_bayar = 0
        pajak = 0.10
        for pesanan, banyak in pesanan_pelanggan.items():
            print(f"・ {pesanan}: Rp, {banyak[1]:,} x {banyak[0]} = Rp. {banyak[0] * banyak[1]:,}")
            total_bayar += banyak[0] * banyak[1]
        print(f"・ PPN: {pajak:.0%}")

        print("──────────────────────────────────────────────────")
        print(f"Total Bayar: Rp. {total_bayar + (total_bayar * pajak):,.0f}")

        # Beneran mengulangi pemesanan lagi.
        while True:
            pilihan = str(input("\nApakah anda ingin melakukan pemesanan lagi? (y/n): ")).lower()
            if pilihan == "y":
                fungsi_utama()
                break
            else:
                print("\n🙏 Terima kasih telah menggunakan layanan kami!")
                break
    else:
        print("\n🙏 Terima kasih telah menggunakan layanan kami!")

fungsi_utama()
