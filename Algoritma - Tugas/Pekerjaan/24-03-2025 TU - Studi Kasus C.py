class StudiC:

    @staticmethod
    def kubik(ukuran, air):
        if ukuran == "f":
            print("\n「 Ukuran F 」\n")
            if (air >= 1) and (air <= 50):
                return f"Rp. {1000 * air:,.0f}"
            elif (air >= 51) and (air <= 100):
                return f"Rp. {1500 * air:,.0f}"
            elif (air > 100):
                return f"Rp. {2500 * air:,.0f}"
            else:
                input_handler()
                return "Error: Input tidak valid"
            
        elif ukuran == "r":
            print("\n「 Ukuran R 」\n")
            if (air >= 1) and (air <= 50):
                return f"Rp. {4000 * air:,.0f}"
            elif (air >= 51) and (air <= 100):
                return f"Rp. {7000 * air:,.0f}"
            elif (air > 100):
                return f"Rp. {10000 * air:,.0f}"
            else:
                input_handler()
                return "Error: Input tidak valid"

        elif ukuran == "n":
            print("\n「 Ukuran N 」\n")
            if (air >= 1) and (air <= 50):
                return f"Rp. {7500 * air:,.0f}"
            elif (air >= 51) and (air <= 100):
                return f"Rp. {10000 * air:,.0f}"
            elif (air > 100):
                return f"Rp. {13500 * air:,.0f}"
            else:
                input_handler()
                return "Error: Input tidak valid"
            
def input_handler():

    while True:
        print("\n===== Perusahaan Daerah Air Minum =====\n")
        ukuran = str(input("Masukkan Ukuran (f/r/n): ")).lower()

        if ukuran not in ["f", "r", "n"]:
            print("\nError: Input tidak valid, Ulang dari awal!\n")
            continue

        try:
            air = int(input("Masukkan Jumlah Air: "))

        except ValueError:
            print("\nError: Input tidak valid, Ulang dari awal!\n")
            continue
        
        hasil = StudiC.kubik(ukuran, air)
        print(hasil)
        break

input_handler()
