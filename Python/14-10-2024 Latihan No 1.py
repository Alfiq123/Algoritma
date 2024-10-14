import math

#  Panjang diameter suatu lingkaran jika diketahui LUAS-nya
luas = int(input("Masukkan luas dari lingkaran: "))

# Rumus = 2 * √(luas / π)
diameter = 2 *  math.sqrt(luas / math.pi)

# Output
print("Diameter lingkaran tersebut adalah:", diameter)
