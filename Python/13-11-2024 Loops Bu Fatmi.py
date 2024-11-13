# # Tangga angka

# # Input jumlah anak tangga
# jumlah_anak_tangga = int(input("Masukkan jumlah anak tangga: "))

# # Looping untuk setiap anak tangga
# for i in range(1, jumlah_anak_tangga + 1):
#     # Looping untuk mencetak angka pada setiap anak tangga
#     for j in range(1, i + 1):
#         print(j, end="")
#     # Pindah ke baris baru untuk anak tangga berikutnya
#     print()

# # Pengulangan basic.
# i = 1
# n = int(input("Masukkan angka: "))
# while i <= n:
#     print(f"Pengulangan ke-{i}")
#     i += 1

# # Guide 2.
# n = 7
# for i in range(1, n + 1, 1):
#     print(f"Pengulangan ke-{i}")

# # Guide 3.
# n = int(input("Masukkan Jumlah Penyewa: "))
# for i in range(1, n + 1, 1):
#     print(f"Penyewa ke-{i}")

# Tangga angka

# # Input jumlah anak tangga
# jumlah_anak_tangga = int(input("Masukkan jumlah anak tangga: "))

# # Looping untuk setiap anak tangga
# for i in range(1, jumlah_anak_tangga + 1):
#     # Looping untuk mencetak angka pada setiap anak tangga
#     for j in reversed(range(1, i + 1)):
#         print(j, end="")
#     # Pindah ke baris baru untuk anak tangga berikutnya
#     print()

# # Guide 4.
# for baris in range(7):
#     for kolom in range(7):
#         print("*", end=" ")
#     print()

# # Guide 5.
# for i in range(3):
#     print("Perulangan luar [i] = ", i)
#     for j in range(3):
#         print("Perulangan dalam [i, j] = ", str(i) + ", " + str(j))

# Guide 6.
# Input jumlah anak tangga
jumlah_anak_tangga = int(input("Masukkan jumlah anak tangga: "))

# Pengulangan untuk setiap anak tangga
for i in range(1, jumlah_anak_tangga + 1):
    # Pengulanganm untuk mencetak angka pada setiap anak tangga
    for j in reversed(range(1, i + 1)):
        print("💝", end=" ")
    # Pindah ke baris baru untuk anak tangga berikutnya
    print()
