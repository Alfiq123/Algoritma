a = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]
b = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84]
c = [100, 94, 88, 82, 76, 70, 64, 58, 52, 46]
d = [35, 28, 21, 14, 7, 0, -7, -14 -21 -28]
e = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]
f = [30, 29, 27, 24, 20, 15, 9, 2, -6, -15]
g = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

ag = [a, b, c, d, e, f, g]

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

x = 0.1 + 0.2
print(x)

input_huruf = str(input("Masukkan Huruf yang ingin dipilih (a, b, c, d, e, f, g): ")).lower()

def barisan_a(n):
    sequence = [4 * i + 1 for i in range(n)]
    return sequence

while input_huruf == "a":
    try:
        a_input = int(input("Enter a number: "))

        if a_input <= 0:
            print("Nomor tidak boleh negatif atau nol.")
        else:
            # Generate and print the sequence
            sequence = barisan_a(a_input)
            for number in sequence:
                print(number)
    except ValueError:
        print("Nomor Tidak Valid, Silakan Coba Kembali!.")
