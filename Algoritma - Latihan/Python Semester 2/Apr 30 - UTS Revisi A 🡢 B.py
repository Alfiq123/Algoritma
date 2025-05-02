
# TODO A1: Buatlah kode program dengan konsep fungsi untuk menampilkan 
        #* urut bilangan dari yang terbesar sampai terkecil dari input 3 bilangan!!

# TODO A2: Dengan Konsep Rekursi, buatlah program untuk menentukan nilai total dari deret berikut:
        #* S = -(-1) + 2 - 7 + 14 - 23 + 34 - 47 + ...

# TODO B1: Dalam suatu perhitungan nilai P = X + Y.
        #* Jika P > 100, maka Q = X * Y, selain itu maka nilai Q = X / Y.
        #* Buat program dengan fungsi untuk mengetahui nilai P atau Q yang lebih besar!!.

# TODO B2: Dengan Konsep Rekursi, buatlah program untuk menentukan nilai total dari deret berikut:
        #* S = 2 + 8 - 18 + 32 - 50 + 72 - ...

class A:

    @staticmethod
    def soal_a1(bil_1, bil_2, bil_3):
        return sorted([bil_1, bil_2, bil_3])

    @staticmethod
    def soal_a2(n):
        """ S = -(-1) + 2 - 7 + 14 - 23 + 34 - 47 + ... """
        # ? Tidak tahu.
        if n == 1:
            return [1]
        elif n == 2:
            return [1, 2]
        else:
            return A.soal_a2(n - 1) + [(-1) ** n * (n ** 2 - 2)]


class B:

    @staticmethod
    def soal_b1(x, y):
        p = x + y
        q = x * y if p > 100 else x / y
        return(f"\nP = {p}\nQ = {q}\nBilangan Terbesar: {max(p, q)}")

    @staticmethod
    def soal_b2(n):
        """ S = 2 + 8 - 18 + 32 - 50 + 72 - ... """
        if n == 1:
            return [2]
        else:
            return B.soal_b2(n - 1) + [((-1) ** n) * 2 * (n ** 2)]

# A.
print(
    f"Bilangan Urut: {A.soal_a1(bil_1 = 6, bil_2 = 12, bil_3 = 8)}\n"
    f"Bilangan Deret: {A.soal_a2(10)}\n"
    f"Total Deret: {sum(A.soal_a2(10))}\n"
)

# B.
print(
    f"Bilangan P, Q: {B.soal_b1(x = 8, y = 16)}\n"
    f"Bilangan Deret: {B.soal_b2(10)}\n"
    f"Total Deret: {sum(B.soal_b2(10))}\n"
)
