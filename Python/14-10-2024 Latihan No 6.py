# Harga suatu barang jika diketahui TOTAL BAYAR & BANYAK BARANG-nya.

# Input
# banyak_barang = int(input("Masukkan banyak barang: "))
# total_bayar = int(input("Masukkan total bayar: Rp. "))

print("🛒️ ===== Mencari harga satu barang jika diketahui TOTAL BAYAR & BANYAK BARANG-nya ===== 🛒️")

# Input "banyak barang" dan "total bayar"
while True:
    try:
        banyak_barang = int(input("Masukkan banyak barang: "))
    except ValueError:
        print("🚨 Angka tidak boleh pakai koma, huruf dan karakter lain 🚨")
    else:
        break

while True:
    try:
        total_bayar = int(input("Masukkan total bayar: Rp. "))
    except ValueError:
        print("🚨 Angka tidak boleh pakai koma, huruf dan karakter lain 🚨")
        continue
    else:
        break

# Rumus c = a / b
harga_satuan = total_bayar / banyak_barang

# Output
print("🏆 ===== Output ===== 🏆")
print("Banyak barang yang dibeli:", banyak_barang)
print(f"Total harga yang dikeluarkan: Rp. {total_bayar:,.0f}")
print(f"Harga satu barang tersebut adalah: Rp. {harga_satuan:,.0f}")
