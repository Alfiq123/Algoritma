
# TODO 1: Membuat Fibonacci ✅
    # TODO: • Iteratif ✅
    # TODO: • Rekursif ✅

# TODO 2: Membuat Prima
    # TODO: • Iteratif
    # TODO: • Rekursif

# * Assets
# * ✅ ❌

class Fibonacci:
    """Wilayah Fiboacci"""

    @staticmethod
    def fibonacci_iteratif(bilangan):
        """Mencari deret Fibonacci secara Iteratif"""
        if bilangan <= 0:
            return []
        elif bilangan == 1:
            return [0]
        
        fib = [0, 1]
        for i in range(2, bilangan):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

    @staticmethod
    def fibonacci_sekian(bilangan):
        """Mencari deret ke-n untuk Fibonacci"""
        if bilangan <= 0:
            return None
        elif bilangan == 1:
            return 0
        a, b = 0, 1
        for _ in range(bilangan - 2):
            a, b = b, a + b
        return b
    
    @staticmethod
    def fibonacci_rekursif(bilangan):
        """Mencari deret Fibonacci secara Rekursif"""
        if bilangan <= 0:
            return []
        return [Fibonacci.fibonacci_rekursif_ke_n(i) for i in range(bilangan)]

    @staticmethod
    def fibonacci_rekursif_ke_n(bilangan):
        """Mencari deret ke-n untuk Fibonacci"""
        if bilangan <= 1:
            return bilangan
        return (Fibonacci.fibonacci_rekursif_ke_n(bilangan - 1) + Fibonacci.fibonacci_rekursif_ke_n(bilangan - 2))
    

class Prima:
    """Wilayah Prima"""

    @staticmethod
    def prima_cek(bilangan):
        """Mengecek Apakah Bilangan Prima atau Bukan"""
        if bilangan < 2:
            return False
        for i in range(2, int(bilangan ** 0.5) + 1):
            if bilangan % i == 0:
                return False
        return True

    @staticmethod
    def prima_iteratif(bilangan):
        """Mengecek Bilangan Prima Secara Iteratif"""
        primes = []
        num = 2
        while len(primes) < bilangan:
            if Prima.prima_cek(num):
                primes.append(num)
            num += 1
        return primes

    @staticmethod
    def prima_ke_n(bilangan):
        """Mencari Bilangan Prima Ke-n"""
        count = 0
        num = 2
        while True:
            if Prima.prima_cek(num):
                count += 1
                if count == bilangan:
                    return num
            num += 1

    @staticmethod
    def prima_rekursif_cek(bilangan, pembatas = None):
        """Mengecek Apakah Bilangan Prima atau Bukan"""
        if bilangan < 2:
            return False
        if pembatas is None:
            pembatas = bilangan - 1
        if pembatas == 1:
            return True
        if bilangan % pembatas == 0:
            return False
        return Prima.prima_rekursif_cek(bilangan, pembatas - 1)

    @staticmethod
    def prima_rekursif(bilangan, sekarang = 2, prima = None):
        """Mengecek Bilangan Prima Secara Rekursif"""
        if prima is None:
            prima = []
        if len(prima) == bilangan:
            return prima
        if Prima.prima_rekursif_cek(sekarang):
            prima.append(sekarang)
        return Prima.prima_rekursif(bilangan, sekarang + 1, prima)

    @staticmethod
    def prima_rekursif_ke_n(bilangan, sekarang = 2, jumlah = 0):
        """Mencari Bilangan Prima Ke-n"""
        if jumlah == bilangan:
            return sekarang - 1
        if Prima.prima_rekursif_cek(sekarang):
            return Prima.prima_rekursif_ke_n(bilangan, sekarang + 1, jumlah + 1)
        return Prima.prima_rekursif_ke_n(bilangan, sekarang + 1, jumlah)


def harus_integer(perintah, negatif = False):
    """Error Handling Untuk Mencegah User Memasukkan Selain Integer"""
    while True:
        try:
            integer = int(input(perintah))
            if not negatif and integer < 0:
                raise ValueError
            return integer
        except ValueError:
            print("Error: Input harus berupa bilangan bulat positif!")
            continue

def handle_user():
    """Menghandle User Input"""

    print(
        "\nPilihan Deret yang Tersedia:\n"
        "  1. Fibonacci\n"
        "  2. Prima\n"
    )
    pilihan = harus_integer(perintah = "Masukkan Pilihan Deret: ")


    if pilihan == 1:
        print("\n「 Fibonacci 」\n")
        berapa_deret = harus_integer(perintah = "Masukkan Berapa Deret: ")
        keberapa = harus_integer(perintah = "Masukkan Deret Ke-n: ")

        print(
            f"\nDeret Fibonacci: {Fibonacci.fibonacci_iteratif(berapa_deret)}\n"
            f"Deret Fibonacci ke-{keberapa}: {Fibonacci.fibonacci_sekian(keberapa)}\n"
        )

        print(
            f"Rekursi Fibonacci: {Fibonacci.fibonacci_rekursif(berapa_deret)}\n"
            f"Rekursi Fibonacci ke-{keberapa}: {Fibonacci.fibonacci_rekursif_ke_n(keberapa - 1)}"
        )


    elif pilihan == 2:
        print("\n「 Prima 」\n")
        berapa_deret = harus_integer(perintah = "Masukkan Berapa Deret: ")
        keberapa = harus_integer(perintah = "Masukkan Deret Ke-n: ")

        print(
            f"\nDeret Prima: {Prima.prima_iteratif(berapa_deret)}\n"
            f"Deret Prima ke-{keberapa}: {Prima.prima_ke_n(keberapa)}\n"
        )

        print(
            f"Rekursi Prima: {Prima.prima_rekursif(berapa_deret)}\n"
            f"Rekursi Orima ke-{keberapa}: {Prima.prima_rekursif_ke_n(keberapa)}"
        )


    else:
        print("\nError: Pilihan tidak valid!")
        handle_user()

handle_user()
