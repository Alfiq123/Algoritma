# Persentase Diskon yang didapat jika diketahui TOTAL BAYAR & TOTAL BELANJA-nya.

# Input
total_bayar = int(input("Masukkan total pembayaran: Rp. "))
total_belanja = int(input("Masukkan total belanja-an: Rp. "))

# Rumus
persentase_diskon = (total_bayar - total_belanja) / total_bayar

# Output
print(f"Persentase diskon yang didapat adalah: {persentase_diskon:.2%}")
