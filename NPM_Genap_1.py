# Buatlah algoritma/program untuk menentukan bilangan terbesar dari input 3 bilangan!!

# Input
x = int(input("Masukkan nilai bilangan 1: "))
y = int(input("Masukkan nilai bilangan 2: "))
z = int(input("Masukkan nilai bilangan 3: "))

# Menentukan bilangan terbesar
if x >= y and x >= z:
    bilangan_terbesar = x
elif y >= x and y >= z:
    bilangan_terbesar = y
else:
    bilangan_terbesar = z

# Output
print("Bilangan terbesar adalah:", bilangan_terbesar)
