# Dictionary.

harga_mie = {
    "indomie": {"goreng": 60000, "kuah": 50000},
    "sedap": {"goreng": 55000, "kuah": 45000},
    "sarimi": {"goreng": 52000, "kuah": 47000}
}

print(harga_mie)
print(harga_mie["indomie"])
print(harga_mie["indomie"]["goreng"])
print(harga_mie["indomie"]["kuah"])
print(harga_mie["sedap"]["goreng"])
print(harga_mie["sedap"]["kuah"])
print(harga_mie["sarimi"]["goreng"])
print(harga_mie["sarimi"]["kuah"])

# Quantity
jumlah_karton = 64

print(f"Total Harga Mie: " f"{harga_mie["indomie"]["goreng"] * jumlah_karton:,.0f}")
print(f"Total Harga Mie: " f"{harga_mie["indomie"]["kuah"] * jumlah_karton:,.0f}")