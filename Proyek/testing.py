menu_makanan = {
    "Makanan": {
        "1a": {"Nasi Goreng Spesial": 45000},
        "2a": {"Ayam Bakar Madu": 55000},
        "3a": {"Steak Sapi Blackpepper": 90000},
        "4a": {"Ikan Bakar Sambal Matah": 65000},
        "5a": {"Spaghetti Carbonara": 50000},
        "6a": {"Pizza Margherita (Medium)": 85000},
        "7a": {"Rendang Daging Sapi": 75000},
        "8a": {"Soto Ayam": 40000},
    },

    "Minuman": {
        "1b": {"Air Mineral": 10000},
        "2b": {"Es Teh Manis": 12000},
        "3b": {"Kopi Latte": 25000},
        "4b": {"Jus Alpukat": 30000},
        "5b": {"Milkshake Cokelat": 28000},
        "6b": {"Lemon Tea": 20000},
        "7b": {"Smoothie Berry": 35000},
    },

    "Appetizer": {
        "1c": {"Sup Krim Jamur": 25000},
        "2c": {"Bruschetta Tomat & Basil": 30000},
        "3c": {"Lumpia Sayur": 20000},
        "4c": {"Salad Caesar": 35000},
        "5c": {"Nachos Keju": 40000},
    },

    "Side_Dish": {
        "1d": {"Kentang Goreng": 25000},
        "2d": {"Onion Rings": 28000},
        "3d": {"Sayur Asem": 18000},
        "4d": {"Tahu & Tempe Goreng": 20000},
    },

    "Dessert": {
        "1e": {"Es Krim Cokelat": 25000},
        "2e": {"Brownies Cokelat": 30000},
        "3e": {"Pancake Madu": 35000},
        "4e": {"Puding Mangga": 28000},
        "5e": {"Cheesecake Strawberry": 40000},
    },
}

daftar_kode = {}
pesanan_palanggan = {}

for kategori, kode in menu_makanan.items():
    # print(f"Kategori: {kategori} Kode: {kode}")
    print()

    for kode_menu, nama_menu in kode.items():
        # print(f"Kode: {kode_menu} - Nama Menu: {nama_menu}")

        for nama, harga in nama_menu.items():
            print(f"{kode_menu} Nama Menu: {nama:40} - Harga: Rp. {harga:,}")
            daftar_kode[nama] = kode_menu

print()

for i, j in daftar_kode.items():
    print(f"{j} {i}")

print()


apa_saja = {
    "nama_makanan": 2
}