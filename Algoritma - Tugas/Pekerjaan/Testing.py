class StudiA:

    @staticmethod
    def megabyte(kode, mb):
        """ Menghitung harga berdasarkan rentang MB. """
        harga_per_mb = {
            "r": [(1, 50, 2000), (51, 80, 4500), (81, float("inf"), 6500)],
            "c": [(1, 50, 5000), (51, 80, 7000), (81, float("inf"), 10000)],
            "v": [(1, 50, 7500), (51, 80, 10000), (81, float("inf"), 15000)]
        }

        if kode in harga_per_mb:
            for (batas_bawah, batas_atas, harga) in (harga_per_mb[kode]):
                if batas_bawah <= mb <= batas_atas:
                    return f"Rp. {harga * mb:,.2f}"
                
            return "Error: Input tidak valid"
        
print(StudiA.megabyte("v", 100))