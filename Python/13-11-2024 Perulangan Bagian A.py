# Soal Bagian A

print("""
Soal Bagian A:
    1. Terdapat 2 jenis perulangan, Limited & Unlimited. 
       Jelaskan perbedaan dari keduanya beserta contohnya dalam kehidupan sehari-hari (bukan program atau diagram).
    2. Sebutkan 3 bagian utama dari Limited Looping, dan kegunaannya!.
    3. Apa perbedaan Increasing dan Decreasing pada For Properties (Gambar 1) simbol Diagram For?.
    4. (Jangan Tanya Soal yang ini!...)
""")

soal_bagian_a = str(input("Masukkan Soal Bagian A (1 / 2 / 3): "))
while soal_bagian_a not in ("1", "2", "3"):
    print("✨ Nomor Soal Tidak Valid, Silakan Coba Kembali!")
    soal_bagian_a = str(input("Masukkan Soal Bagian A (1 / 2 / 3): "))

if soal_bagian_a == "1":
    print("""

「 Jelaskan perbedaan dari Limited & Unlimited Looping!. 」

Limited: Perulangan terbatas adalah kegiatan yang dilakukan dalam jumlah tertentu atau dalam batasan waktu yang jelas. 
         Setelah mencapai batas tersebut, kegiatan tersebut akan berhenti.
         Contoh: Membaca Buku, Olahraga, Menonton Film.

Unlimited: Perulangan tidak terbatas adalah kegiatan yang dapat dilakukan tanpa batasan jumlah atau waktu tertentu. 
           Kegiatan ini dapat berlangsung terus-menerus selama tidak ada intervensi atau keputusan untuk berhenti.
           Contoh: Makan / Minum, Berbicara, Berjalan, Bernafas.
""")

if soal_bagian_a == "2":
    print("""
「 Sebutkan 3 bagian utama dari Limited Looping, dan kegunaannya!. 」

1. Inisialisasi (Initialization)
   • Definisi: Tahap awal yang menetapkan nilai atau kondisi awal sebelum perulangan dimulai.
   • Kegunaan:
     • Menentukan titik awal perulangan
     • Menyiapkan variabel yang akan digunakan dalam proses perulangan
     • Mengatur parameter awal yang diperlukan

2. Kondisi (Condition)
   • Definisi: Ekspresi atau syarat yang menentukan apakah perulangan akan dilanjutkan atau dihentikan.
   • Kegunaan:
     • Mengontrol jumlah iterasi perulangan
     • Menentukan kapan perulangan harus berhenti
     • Menjaga agar perulangan tidak berlangsung tanpa batas

3. Increment/Decrement
   • Definisi: Proses perubahan nilai variabel setelah setiap iterasi.
   • Kegunaan:
     • Mengubah nilai variabel kontrol
     • Memajukan atau mundurkan perulangan
     • Memastikan perulangan bergerak menuju kondisi akhir

Contoh Sederhana dalam Kehidupan Sehari-hari: Misalnya, proses memasak nasi:
• Inisialisasi: Menyiapkan beras dan air
• Kondisi: Memasak hingga air habis
• Increment: Mengaduk dan mengecek perkembangan nasi setiap beberapa menit
""")

if soal_bagian_a == "3":
    print("""
「 Apa perbedaan Increasing dan Decreasing pada For Properties? (Flowgorithm). 」

Increasing (Bertambah)
• Arah Pergerakan: Dari nilai terkecil menuju nilai terbesar
• Simbol Operasi: Panah naik (↑)
• Proses: Variabel bertambah setiap iterasi
• Contoh: 1, 2, 3, 4, 5
          
Decreasing (Berkurang)
• Arah Pergerakan: Dari nilai terbesar menuju nilai terkecil
• Simbol Operasi: Panah turun (↓)
• Proses: Variabel berkurang setiap iterasi
• Contoh: 5, 4, 3, 2, 1

Perbedaan Utama
• Arah pergerakan berlawanan
• Nilai variabel berubah dengan cara berbeda
• Kondisi berhenti berbeda

Ilustrasi Sederhana
• Increasing: Mendaki tangga dari bawah ke atas,
• Decreasing: Turun tangga dari atas ke bawah.
""")
