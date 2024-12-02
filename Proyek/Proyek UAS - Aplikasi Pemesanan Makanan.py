menu_makanan = {
    "Appetizer": {
        "Sup Krim Jamur": 25000,
        "Bruschetta Tomat & Basil": 30000,
        "Lumpia Sayur": 20000,
        "Salad Caesar": 35000,
        "Nachos Keju": 40000,
    },

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

    "Minuman": {
        "Air Mineral": 10000,
        "Es Teh Manis": 12000,
        "Kopi Latte": 25000,
        "Jus Alpukat": 30000,
        "Milkshake Cokelat": 28000,
        "Lemon Tea": 20000,
        "Smoothie Berry": 35000,
    }
}

valid_menu_makanan = (
    *menu_makanan["Appetizer"].keys(), 
    *menu_makanan["Makanan"].keys(), 
    *menu_makanan["Side_Dish"].keys(),
    *menu_makanan["Dessert"].keys(),
    *menu_makanan["Minuman"].keys()
)

list_kosong = {}

while True:
    pesanan_pelanggan = str(input("Masukkan Pesanan Pelanggan: ")).title()

    if pesanan_pelanggan not in valid_menu_makanan:
        print("Pesanan tidak tersedia")
        continue

    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
    list_kosong[pesanan_pelanggan] = [jumlah_pesanan]
    print()
    print("Daftar Pesanan Anda:")

    # for pesanan in list_kosong:
    #     print(f"• {pesanan} x {list_kosong[pesanan][0]} = Rp.{menu_makanan['Makanan'][pesanan] * list_kosong[pesanan][0]:,}")
    # print()

    for pesanan in list_kosong:
        kategori = None
        # Cari kategori menu berdasarkan pesanan
        for cat, menu in menu_makanan.items():
            if pesanan in menu:
                kategori = cat
                break
        if kategori:
            harga = menu_makanan[kategori][pesanan]
            total_harga = harga * list_kosong[pesanan][0]
            print(f"• {pesanan} x {list_kosong[pesanan][0]} = Rp.{total_harga:,}")
    print()
