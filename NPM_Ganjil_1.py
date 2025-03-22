# Dalam suatu perhitungan, nilai P = X + Y, jika
# P genap, maka Q = X * Y, sedangkan jika
# P ganjil maka nilai Q = X / Y,
# Buatlah algoritma/ program untuk mencari nilai P dan Q, dan tampilkan hasilnya.

# Input
X = int(input("Masukkan nilai X: "))
Y = int(input("Masukkan nilai Y: "))

# Deklarasi Variabel
P = X + Y

# Jika nilai "P" genap, maka (Q = X * Y)
if P % 2 == 0:
    Q = X * Y
# Jika nilai "P" ganjil, maka (Q = X / Y)
else:
    Q = X / Y

# Output
print("Nilai P:", P)
print("Nilai Q:", Q)