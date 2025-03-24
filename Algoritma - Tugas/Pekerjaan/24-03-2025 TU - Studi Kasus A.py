class StudiA:

    @staticmethod
    def megabyte(kode, mb):
        if kode == "r":
            if (mb >= 1) and (mb <= 50):
                return f"Rp. {2000 * mb:,.0f}"
            elif (mb >= 51) and (mb <= 80):
                return f"Rp. {4500 * mb:,.0f}"
            elif (mb > 80):
                return f"Rp. {6500 * mb:,.0f}"
            else:
                handle_input()
                return "Error: Input tidak valid"
            
        elif kode == "c":
            if (mb >= 1) and (mb <= 50):
                return f"Rp. {5000 * mb:,.0f}"
            elif (mb >= 51) and (mb <= 80):
                return f"Rp. {7000 * mb:,.0f}"
            elif (mb > 80):
                return f"Rp. {10000 * mb:,.0f}"
            else:
                handle_input()
                return "Error: Input tidak valid"

        elif kode == "v":
            if (mb >= 1) and (mb <= 50):
                return f"Rp. {7500 * mb:,.0f}"
            elif (mb >= 51) and (mb <= 80):
                return f"Rp. {10000 * mb:,.0f}"
            elif (mb > 80):
                return f"Rp. {15000 * mb:,.0f}"
            else:
                handle_input()
                return "Error: Input tidak valid"
            
def handle_input():

    while True:
        print("\n===== Hotspot Modi =====\n")
        pilih = str(input("Masukkan Pilihan (r/c/v): ")).lower()

        if pilih not in ["r", "c", "v"]:
            print("\nError: Input tidak valid, Ulang dari awal!\n")
            continue

        try:
            mb = int(input("Masukkan Jumlah MB: "))

        except ValueError:
            print("\nError: Input tidak valid, Ulang dari awal!\n")
            continue
        
        hasil = StudiA.megabyte(pilih, mb)
        print(hasil)
        break

handle_input()
