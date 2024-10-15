# Persentase Diskon yang didapat jika diketahui TOTAL BAYAR & TOTAL BELANJA-nya.

total_bayar = int(input("Masukkan total pembayaran: Rp. "))
total_belanja = int(input("Masukkan total belanja-an: Rp. "))

persentase_diskon = (total_bayar - total_belanja) / total_bayar
print(f"Persentase diskon yang didapat adalah: {persentase_diskon:.2%}")
