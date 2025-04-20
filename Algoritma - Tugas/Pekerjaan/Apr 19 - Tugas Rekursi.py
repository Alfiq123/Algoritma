
# TODO 1: Membuat Fibonacci 👍
    # TODO: Rekursif ✅

# TODO 2: Membuat Prima 👍
    # TODO: Rekursif ✅

# TODO 3: Membuat Deret X 👍
    # TODO: Deret A ✅
    # TODO: Deret B ✅
    # TODO: Deret C ✅


class Fibonacci:

    @staticmethod
    def fibonacci_rekursif(bilangan):
        if bilangan <= 0:
            return []
        elif bilangan == 1:
            return [1]
        elif bilangan == 2:
            return [0, 1]
        else:
            sebelum = Fibonacci.fibonacci_rekursif(bilangan - 1)
            return sebelum + [sebelum[-1] + sebelum[-2]]


# ! Bagian ini di generate oleh ChatGPT-4o.
class Prima:

    @staticmethod
    def prima_rekursif_cek(angka, pembagi = 2):
        """Cek apakah angka adalah bilangan prima (rekursif)"""
        if angka < 2:
            return False
        if pembagi * pembagi > angka:
            return True
        if angka % pembagi == 0:
            return False
        return Prima.prima_rekursif_cek(angka, pembagi + 1)

    @staticmethod
    def prima_rekursif(bilangan, sekarang = 2, prima = None):
        """Menghasilkan deret bilangan prima secara rekursif"""
        if prima is None:
            prima = []
        if len(prima) == bilangan:
            return prima
        if Prima.prima_rekursif_cek(sekarang):
            prima.append(sekarang)
        return Prima.prima_rekursif(bilangan, sekarang + 1, prima)


class DeretA:

    @staticmethod
    def jumlah_deret(bilangan):
        """
            Un = 3n - 2
            S = 1 + 4 + 7 + 10 + 13 + 16 + ...
        """
        if bilangan == 1:
            return [3 * bilangan - 2]
        else:
            return (DeretA.jumlah_deret(bilangan - 1) + [3 * bilangan - 2])


class DeretB:

    @staticmethod
    def jumlah_deret(bilangan):
        """
            Un = n² + 1
            S = 2 + 5 + 10 + 17 + 26 + 37 + 50 + ...
        """
        if bilangan == 1:
            return [bilangan ** 2 + 1]
        else:
            return (DeretB.jumlah_deret(bilangan - 1) + [bilangan ** 2 + 1])


class DeretC:

    @staticmethod
    def jumlah_deret(bilangan):
        """
            Un = n² - 1
            S = 0 + 3 + 8 + 15 + 24 + 35 + ...
        """
        if bilangan == 1:
            return [bilangan ** 2 - 1]
        else:
            return (DeretC.jumlah_deret(bilangan - 1) + [bilangan ** 2 - 1])
        

# * User Error Handle
def user_error(perintah, negatif = False):
    while True:
        try:
            user = int(input(perintah))
            if not negatif and user < 0:
                print("\nError: Bilangan tidak boleh negatif!\n")
                continue
            elif user > 100:
                print("\nError: Bilangan tidak boleh lebih dari 100 deret!\n")
                continue
            else:
                return user
        except ValueError:
            print("\nError: Input harus berupa bilangan bulat positif!\n")
            continue

# * User Input
def user_input():
    print(
        "\nPilihan Deret Bilangan:\n"
        "  1. Fibonacci\n"
        "  2. Prima\n"
        "  3. Deret A\n"
        "  4. Deret B\n"
        "  5. Deret C\n"
    )

    pilihan = user_error(perintah = "Masukkan Pilihan Deret: ")
    jumlah_deret = user_error(perintah = "Masukkan Jumlah Deret: ")
    
    # * Deret Fibonacci
    if pilihan == 1:
        print("\n「 Fibonacci 」")
        print(
            f"\nDeret Bilangan: {Fibonacci.fibonacci_rekursif(jumlah_deret)}\n"
            f"Deret Bilangan Total: {sum(Fibonacci.fibonacci_rekursif(jumlah_deret))}"
        )

    # * Deret Prima
    elif pilihan == 2:
        print("\n「 Prima 」")
        print(
            f"\nDeret Bilangan: {Prima.prima_rekursif(jumlah_deret)}\n"
            f"Deret Bilangan Total: {sum(Prima.prima_rekursif(jumlah_deret))}"
        )

    # * Deret A
    elif pilihan == 3:
        print("\n「 Deret A 」")
        print(
            f"\nDeret Bilangan: {DeretA.jumlah_deret(jumlah_deret)}\n"
            f"Deret Bilangan Total: {sum(DeretA.jumlah_deret(jumlah_deret))}"
        )

    # * Deret B
    elif pilihan == 4:
        print("\n「 Deret B 」")
        print(
            f"\nDeret Bilangan: {DeretB.jumlah_deret(jumlah_deret)}\n"
            f"Deret Bilangan Total: {sum(DeretB.jumlah_deret(jumlah_deret))}"
        )

    # * Deret C
    elif pilihan == 5:
        print("\n「 Deret C 」")
        print(
            f"\nDeret Bilangan: {DeretC.jumlah_deret(jumlah_deret)}\n"
            f"Deret Bilangan Total: {sum(DeretC.jumlah_deret(jumlah_deret))}"
        )

    else:
        print("\nError: Pilihan Tidak Tersedia!")
        user_input()

    coba_lagi = str(input("\nCoba Lagi?: ")).lower()
    if coba_lagi in ("y", "ya"):
        user_input()

user_input()
