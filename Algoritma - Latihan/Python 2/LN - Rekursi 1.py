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


def inputan():
    while True:
        try:
            print("Pilihan yang tersedia: \n  1. Pangkat, \n  2. Faktorial, \n  3. Fibonacci")
            pilihan = int(input("\nMasukkan Pilihan: "))

            # Pangkat
            if pilihan == 1:
                while True:
                    try:
                        nomor = int(input("Masukkan Nomor: "))
                        eksponen = int(input("Masukkan Eksponen: "))
                        if nomor < 0 or eksponen < 0:
                            raise ValueError
                    except ValueError:
                        print("\nError: Input tidak valid!\n")
                        continue
                    break
                hitung_pangkat = Pangkat(nomor, eksponen)
                print(f"Rekursi: {nomor}^{eksponen} = {hitung_pangkat.pangkat_rekursi(nomor, eksponen):,}")
                print(f"For Loop: {nomor}^{eksponen} = {hitung_pangkat.pangkat_for(nomor, eksponen):,}")
                break


            # Faktorial
            elif pilihan == 2:
                while True:
                    try:
                        nomor = int(input("Masukkan Nomor: "))
                        if nomor < 0:
                            raise ValueError
                    except ValueError:
                        print("\nError: Input tidak valid!\n")
                        continue
                    break

                hitung_faktorial = Faktorial(nomor)
                print(f"Rekursi: {nomor}! = {hitung_faktorial.faktorial_rekursi(nomor):,}")
                print(f"For Loop: {nomor}! = {hitung_faktorial.factorial_for(nomor):,}")
                break

            # Fibonacci
            elif pilihan == 3:
                while True:
                    try:
                        nomor = int(input("Masukkan Nomor: "))
                        if nomor < 0:
                            raise ValueError
                    except ValueError:
                        print("\nError: Input tidak valid!\n")
                        continue
                    break

                hitung_fibonacci = Fibonacci(nomor)
                print(f"Rekursi: {nomor} = {hitung_fibonacci.fibonacci_rekursi(nomor):,}")
                print(f"For Loop: {nomor} = {hitung_fibonacci.fibonacci_for(nomor):,}")
                break

            # Sisanya
            else:
                print("\nError: Pilihan tidak valid!\n")
                continue
        
        except ValueError:
            print("\nError: Pilihan tidak valid!\n")
            continue
            
inputan()
