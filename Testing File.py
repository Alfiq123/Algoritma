# Dictionary.

# harga_mie = {
#     "indomie": {"goreng": 60000, "kuah": 50000},
#     "sedap": {"goreng": 55000, "kuah": 45000},
#     "sarimi": {"goreng": 52000, "kuah": 47000}
# }

# print(harga_mie)
# print(harga_mie["indomie"])
# print(harga_mie["indomie"]["goreng"])
# print(harga_mie["indomie"]["kuah"])
# print(harga_mie["sedap"]["goreng"])
# print(harga_mie["sedap"]["kuah"])
# print(harga_mie["sarimi"]["goreng"])
# print(harga_mie["sarimi"]["kuah"])

# # Quantity
# jumlah_karton = 64

# print(f"Total Harga Mie: " f"{harga_mie["indomie"]["goreng"] * jumlah_karton:,.0f}")
# print(f"Total Harga Mie: " f"{harga_mie["indomie"]["kuah"] * jumlah_karton:,.0f}")

# Kamus - Harga Mie
harga_mie = {
    "indomie": {"goreng": 60000, "kuah": 50000},
    "sedap": {"goreng": 55000, "kuah": 45000},
    "sarimi": {"goreng": 52000, "kuah": 47000}
}
merk_mie = ["indomie", "sedap", "sarimi"]
jenis_mie = ["goreng", "kuah"]

# Deklarasi Variabel.
bonus = "Tidak ada"
diskon = 0
total_harga = 0

# Input - input dari pengguna.
def input_dari_user():

    # Input 1 - Nama Pembeli.
    nama = input("Masukkan Nama Pembeli: ").strip()
    while nama == "":
        print("⛔ Nama tidak boleh kosong")
        nama = input("Masukkan Nama Pembeli: ").strip()

    # Input 2 - Merk Mie.
    while True:
        merk = input("Masukkan merk mie yang ingin dibeli (Indomie, Sedap, Sarimi): ").lower()
        if merk not in merk_mie:
            print("📢 Merk tidak tersedia, silakan coba lagi.")
            continue
        
        # Input 3 - Jenis Mie.
        while True:
            jenis = input("Masukkan Jenis Mie (Goreng / Kuah): ").lower()
            if jenis not in jenis_mie:
                print("📢 Jenis tidak dikenal, silakan coba lagi")
                continue
            break
        
        # Input 4 - Jumlah Karton.
        while True:
            try:
                jumlah_karton = int(input("Masukkan Jumlah Karton: "))
                if jumlah_karton <= 0:
                    print("🚨 Jumlah karton tidak boleh negatif!")
                    continue
                break
            except ValueError:
                print("⛔ Tolong masukkan angka")

        # Hasil Awal.
        total_harga = harga_mie[merk][jenis] * jumlah_karton
        print(f"Total harga untuk {jumlah_karton} karton Mi {merk} {jenis}: Rp. {total_harga:,.0f}")

        # Input 5 - Beli Lagi
        jawab = input("Beli lagi? (ya / tidak): ").lower()
        if jawab != "ya":
            break

    print("Terima kasih telah berbelanja!")

input_dari_user()
