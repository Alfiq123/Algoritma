# Persentase Diskon yang didapat jika diketahui TOTAL BAYAR & TOTAL BELANJA-nya.

# Input
# total_bayar = int(input("Masukkan total pembayaran: Rp. "))
# total_belanja = int(input("Masukkan total belanja-an: Rp. "))

# Input - Total belanjaan.
while True:
    try:
        total_belanja = int(input("Masukkan total belanja-an: Rp. "))
    except ValueError:
        print("🚩 Kamu memasukkan huruf atau karakter lain 🚩")
        continue
    else:
        break

# Input - Total pembayaran setelah diskon.
while True:
    try:
        total_bayar = int(input("Masukkan total pembayaran (setelah diskon): Rp. "))
    except ValueError:
        print("🚩 Kamu memasukkan huruf atau karakter lain 🚩")
        continue
    else:
        break

# Rumus diskon
persentase_diskon = (total_belanja - total_bayar) / total_belanja * 100

# Output
print("🏁 ===== Hasil ===== 🏁")
print(f"Total belanjaan: Rp. {total_belanja:,.0f}")
print(f"Total pembayaran: Rp. {total_bayar:,.0f}")
print(f"Mencari diskon: (Rp. {total_belanja:,.0f} - Rp. {total_bayar:,.0f}) / Rp. {total_bayar:,.0f} * 100")
print(f"Persentase diskon yang didapat adalah: {persentase_diskon:.2f}%")
