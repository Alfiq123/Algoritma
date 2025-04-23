class Pangkat:
    def __init__(self, nomor, eksponen):
        self.nomor = nomor
        self.eksponen = eksponen

    def pangkat_rekursi(self, nomor, eksponen):
        if eksponen == 0:
            return 1
        elif eksponen == 1:
            return nomor
        else:
            return nomor * self.pangkat_rekursi(nomor, eksponen - 1)
    
    def pangkat_for(self, nomor, eksponen):
        hasil = 1
        for z in range(eksponen):
            hasil *= nomor
        return hasil


" --- "


class Faktorial:
    def __init__(self, nomor):
        self.nomor = nomor
        
    def faktorial_rekursi(self, nomor):
        if nomor == 0 or nomor == 1:
            return 1
        return nomor * self.faktorial_rekursi(nomor - 1)

    def factorial_for(self, nomor):
        result = 1
        for z in range(1, nomor + 1):
            result *= z
        return result


" --- "


class Fibonacci:
    """ Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ... """
    def __init__(self, nomor):
        self.nomor = nomor

    def fibonacci_rekursi(self, nomor):
        if nomor == 0:
            return 0
        elif nomor == 1:
            return 1
        
        return self.fibonacci_rekursi(nomor - 1) + self.fibonacci_rekursi(nomor - 2)

    def fibonacci_for(self, nomor):
        if nomor == 0:
            return 0
        satu, dua = 0, 1
        for z in range(2, nomor + 1):
            satu, dua = dua, satu + dua
        return dua


" --- "


def cek_integer(perintah, negatif = False):
    while True:
        try:
            integer = int(input(perintah))
            if not negatif and integer < 0:
                raise ValueError
            return integer
        except ValueError:
            print("Input harus berupa bilangan" + ("." if negatif else " bulat positif."))
            continue


def inputan():
    print("\nPilihan yang tersedia: \n  1. Pangkat, \n  2. Faktorial, \n  3. Fibonacci")
    pilihan = cek_integer(perintah = "\nMasukkan pilihan: ", negatif = False)


    # Pangkat
    if pilihan == 1:
        nomor = cek_integer(perintah = "Masukkan Nomor: ")
        eksponen = cek_integer(perintah = "Masukkan Eksponen: ")
        hasil = Pangkat(nomor, eksponen)
        print(f"\nRekursi: {nomor}^{eksponen} = {hasil.pangkat_rekursi(nomor, eksponen):,}")
        print(f"For Loop: {nomor}^{eksponen} = {hasil.pangkat_for(nomor, eksponen):,}")


    # Faktorial
    elif pilihan == 2:
        nomor = cek_integer(perintah = "Masukkan Nomor: ")
        hasil = Faktorial(nomor)
        print(f"\nRekursi: {nomor}! = {hasil.faktorial_rekursi(nomor):,}")
        print(f"For Loop: {nomor}! = {hasil.factorial_for(nomor):,}")


    # Fibonacci
    elif pilihan == 3:
        nomor = cek_integer(perintah = "Masukkan Nomor: ")
        hasil = Fibonacci(nomor)
        print(f"\nRekursi: {nomor} = {hasil.fibonacci_rekursi(nomor):,}")
        print(f"For Loop: {nomor} = {hasil.fibonacci_for(nomor):,}")


    # Sisanya
    else:
        print("\nError: Pilihan tidak valid!")
        
inputan()
