a = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]
b = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84]
c = [100, 94, 88, 82, 76, 70, 64, 58, 52, 46]
d = [35, 28, 21, 14, 7, 0, -7, -14 -21 -28]
e = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]
f = [30, 29, 27, 24, 20, 15, 9, 2, -6, -15]
g = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

ag = [a, b, c, d, e, f, g]

# a = a(n) = 4*n + 1
# b = a(n) = 9*n + 1
# c = a(n) = 106 - 6n  [-6]
# d = a(n) = 42 − 7n [-7]

# e = a(n) = ½(n²) - ½(n) + 1
# e = a(n) = 0.5(n²) - 0.5(n) + 1

# f = a(n) = -½n² + ½n + 30
# f = a(n) = -0.5n² + 0.5n + 30

# g = a(n) = 2 ^ (n-1)

print(r"""
  ____             _                                 _ _                   _   _ _         
 |  _ \           (_)                     /\        (_) |                 | | (_) |        
 | |_) | __ _ _ __ _ ___  __ _ _ __      /  \   _ __ _| |_ _ __ ___   __ _| |_ _| | ____ _ 
 |  _ < / _` | '__| / __|/ _` | '_ \    / /\ \ | '__| | __| '_ ` _ \ / _` | __| | |/ / _` |
 | |_) | (_| | |  | \__ \ (_| | | | |  / ____ \| |  | | |_| | | | | | (_| | |_| |   < (_| |
 |____/ \__,_|_|  |_|___/\__,_|_| |_| /_/    \_\_|  |_|\__|_| |_| |_|\__,_|\__|_|_|\_\__,_|
                                                                                           """)

print("""
a = 1, 5, 9, 13, 17, 21, 25, 29, 33, 37
b = 3, 12, 21, 30, 39, 48, 57, 66, 75, 84
c = 100, 94, 88, 82, 76, 70, 64, 58, 52, 46
d = 35, 28, 21, 14, 7, 0, -7, -14 -21 -28
e = 1, 2, 4, 7, 11, 16, 22, 29, 37, 46]
f = 30, 29, 27, 24, 20, 15, 9, 2, -6, -15
g = 1, 2, 4, 8, 16, 32, 64, 128, 256, 512
""")

input_huruf = str(input("Masukkan Huruf yang ingin dipilih (a, b, c, d, e, f, g): ")).lower()

# Rumus Deret - A
def barisan_a(na):
    urutan_a = [4 * i + 1 for i in range(na)]
    return urutan_a

# Input Deret - A
# • a(n) = 4*n + 1
while input_huruf == "a":
    try:
        a_input = int(input("Masukkan berapa nomor yang ingin dihitung: "))
        if a_input <= 0:
            print("🚩 Nomor tidak boleh negatif atau nol.")
        else:
            urutan_a = barisan_a(a_input)
            for nomor_a in urutan_a:
                print(nomor_a)
    except ValueError:
        print("🚩 Nomor Tidak Valid, Silakan Coba Kembali!.")



# Rumus Deret - B
# • a(n) = 9*n + 1
def barisan_b(nb):
    urutan_b = [9 * bn + 3 for bn in range(nb)]
    return urutan_b

# Input Deret - B
while input_huruf == "b":
    try:
        b_input = int(input("Masukkan berapa nomor yang ingin dihitung: "))
        if b_input <= 0:
            print("🚩 Nomor tidak boleh negatif atau nol.")
        else:
            urutan_b = barisan_b(b_input)
            for nomor_b in urutan_b:
                print(nomor_b)
    except ValueError:
        print("🚩 Nomor Tidak Valid, Silakan Coba Kembali!.")



# Rumus Deret - C
# a(n) = 100 - 6n  [-6]
def barisan_c(nc):
    urutan_c = [100 - 6 * cn for cn in range(nc)]
    return urutan_c

# Input Deret - C
while input_huruf == "c":
    try:
        c_input = int(input("Masukkan berapa nomor yang ingin dihitung: "))
        if c_input <= 0:
            print("🚩 Nomor tidak boleh negatif atau nol.")
        else:
            urutan_c = barisan_c(c_input)
            for nomor_c in urutan_c:
                print(nomor_c)
    except ValueError:
        print("🚩 Nomor Tidak Valid, Silakan Coba Kembali!.")



# Rumus Deret - D
# a(n) = 42 − 7n [-7]
def barisan_d(nd):
    urutan_d = [35 - 7 * dn for dn in range(nd)]
    return urutan_d

# Input Deret - D
while input_huruf == "d":
    try:
        d_input = int(input("Masukkan berapa nomor yang ingin dihitung: "))
        if d_input <= 0:
            print("🚩 Nomor tidak boleh negatif atau nol.")
        else:
            urutan_d = barisan_d(d_input)
            for nomor_d in urutan_d:
                print(nomor_d)
    except ValueError:
        print("🚩 Nomor Tidak Valid, Silakan Coba Kembali!.")



# Rumus Deret - E
# a(n) = 0.5(n²) - 0.5(n) + 1
def barisan_e(ne):
    urutan_e = [0.5 * en ** 2 - 0.5 * en + 1 for en in range(ne)]
    return urutan_e

# Input Deret - E
while input_huruf == "e":
    try:
        e_input = int(input("Masukkan berapa nomor yang ingin dihitung: "))
        if e_input <= 0:
            print("🚩 Nomor tidak boleh negatif atau nol.")
        else:
            urutan_e = barisan_e(e_input)
            for nomor_e in urutan_e:
                print(f"{nomor_e:.0f}")
    except ValueError:
        print("🚩 Nomor Tidak Valid, Silakan Coba Kembali!.")



# Rumus Deret - F
# a(n) = -0.5n² + 0.5n + 30
def barisan_f(nf):
    urutan_f = [-0.5 * fn ** 2 + 0.5 * fn + 30 for fn in range(nf)]
    return urutan_f

# Input Deret - F
while input_huruf == "f":
    try:
        f_input = int(input("Masukkan berapa nomor yang ingin dihitung: "))
        if f_input <= 0:
            print("🚩 Nomor tidak boleh negatif atau nol.")
        else:
            urutan_f = barisan_f(f_input)
            for nomor_f in urutan_f:
                print(f"{nomor_f:.0f}")
    except ValueError:
        print("🚩 Nomor Tidak Valid, Silakan Coba Kembali!.")



# Rumus Deret - G
# a(n) = 2 ^ (n-1)
def barisan_f(ng):
    urutan_g = [2 ** gn for gn in range(ng)]
    return urutan_g

# Input Deret - G
while input_huruf == "g":
    try:
        g_input = int(input("Masukkan berapa nomor yang ingin dihitung: "))
        if g_input <= 0:
            print("🚩 Nomor tidak boleh negatif atau nol.")
        else:
            urutan_g = barisan_f(g_input)
            for nomor_g in urutan_g:
                print(f"{nomor_g:,}")
    except ValueError:
        print("🚩 Nomor Tidak Valid, Silakan Coba Kembali!.")
