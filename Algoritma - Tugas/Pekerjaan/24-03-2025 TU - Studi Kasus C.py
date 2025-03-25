class StudiC:
    """
    Kelas StudiC menyediakan metode untuk menghitung biaya penggunaan air
    berdasarkan ukuran pelanggan dan jumlah air yang digunakan.
    """
    def kubik(ukuran, air):
        """
        Menghitung biaya air berdasarkan ukuran pelanggan dan jumlah air yang digunakan.
        
        Parameters:
            ukuran (str): Jenis pelanggan, dapat berupa 'f' (Fasilitas umum), 'r' (Rumah biasa), atau 'n' (Niaga).
            air (int): Jumlah penggunaan air dalam meter kubik.
        
        Returns:
            str: Biaya penggunaan air dalam format mata uang Rupiah.
        """
        harga_per_kubik = {
            "f": [(1, 50, 1000), (51, 100, 1500), (101, float("inf"), 2500)],
            "r": [(1, 50, 4000), (51, 100, 7000), (101, float("inf"), 10000)],
            "n": [(1, 50, 7500), (51, 100, 10000), (101, float("inf"), 13500)]
        }

        if ukuran in harga_per_kubik:
            for (batas_bawah, batas_atas, harga) in (harga_per_kubik[ukuran]):
                if batas_bawah <= air <= batas_atas:
                    return f"Rp. {harga * air:,.2f}"
            
def input_handler():
    """
    Fungsi untuk menangani input pengguna dan menghitung biaya penggunaan air.
    
    Meminta input ukuran pelanggan dan jumlah air yang digunakan,
    kemudian menampilkan hasil perhitungan biaya berdasarkan kategori pelanggan.
    """
    while True:
        print("\n===== Perusahaan Daerah Air Minum =====\n")
        ukuran = str(input("Masukkan Ukuran (f/r/n): ")).lower()
        if ukuran not in ["f", "r", "n"]:
            print("\nError: Input tidak valid, Ulang dari awal!\n")
            continue
        while True:
            try:
                air = int(input("Masukkan Jumlah Air: "))
                if air < 0:
                    raise ValueError
            except ValueError:
                print("\nError: Input tidak valid, Ulang dari awal!\n")
                continue
            break
        hasil = StudiC.kubik(ukuran, air)
        print(hasil)
        break

input_handler()
