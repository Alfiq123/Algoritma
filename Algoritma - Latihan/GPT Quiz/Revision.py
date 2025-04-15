import tkinter as tk
from tkinter import ttk

jenis_pupuk = {
    "Pupuk NPK Phonska": {"Kering": 150000, "Cair": 50000},
    "Pupuk Urea": {"Kering": 120000, "Cair": 40000},
    "Pupuk Dolomite": {"Kering": 100000, "Cair": 70000},
    "Pupuk ZK Petro": {"Kering": 805000, "Cair": 125000},
    "Pupuk Mutiara": {"Kering": 365000, "Cair": 25000}
}

class Pupuk:
    
    @staticmethod
    def hitung_harga(merk, jenis, jumlah):
        if merk in jenis_pupuk:
            if jenis in jenis_pupuk[merk]:
                harga = jenis_pupuk[merk][jenis] * jumlah
                return f"Rp. {harga:,.2f}"
        return None
    
print(Pupuk.hitung_harga("Pupuk Dolomite", "Cair", 4))
