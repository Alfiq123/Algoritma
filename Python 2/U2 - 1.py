# Program Hitung Absensi Mahasiswa

def input_absensi(jumlah_pertemuan):
    absensi = {}
    for i in range(jumlah_pertemuan):
        pertemuan = f"Pertemuan {i+1}"
        print(f"\n{pertemuan}")
        nama = input("Masukkan nama mahasiswa: ")
        status = input("Hadir (H) / Tidak Hadir (T): ").upper()
        
        if nama not in absensi:
            absensi[nama] = {"Hadir": 0, "Tidak Hadir": 0}
        
        if status == "H":
            absensi[nama]["Hadir"] += 1
        elif status == "T":
            absensi[nama]["Tidak Hadir"] += 1
        else:
            print("Input tidak valid. Masukkan H atau T.")
            return input_absensi(jumlah_pertemuan)
    
    return absensi

def hitung_persentase(absensi, jumlah_pertemuan):
    for nama, data in absensi.items():
        total_hadir = data["Hadir"]
        persentase_hadir = (total_hadir / jumlah_pertemuan) * 100
        absensi[nama]["Persentase Hadir"] = persentase_hadir
    return absensi

def tampilkan_absensi(absensi):
    print("\nLaporan Absensi Mahasiswa:")
    for nama, data in absensi.items():
        print(f"\nNama: {nama}")
        print(f"Hadir: {data['Hadir']} kali")
        print(f"Tidak Hadir: {data['Tidak Hadir']} kali")
        print(f"Persentase Kehadiran: {data['Persentase Hadir']:.2f}%")

def main():
    jumlah_pertemuan = int(input("Masukkan jumlah pertemuan selama satu semester: "))
    absensi = input_absensi(jumlah_pertemuan)
    absensi = hitung_persentase(absensi, jumlah_pertemuan)
    tampilkan_absensi(absensi)

main()
