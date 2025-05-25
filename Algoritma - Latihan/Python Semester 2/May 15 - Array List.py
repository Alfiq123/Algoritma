# List Buku
def soal_1():
    buku = [
      {
        "judul": "Laskar Pelangi",
        "penulis": "Andrea Hirata",
        "tahun_terbit": 2005
      },
      {
        "judul": "Bumi Manusia",
        "penulis": "Pramoedya Ananta Toer",
        "tahun_terbit": 1980
      },
      {
        "judul": "Ayat-Ayat Cinta",
        "penulis": "Habiburrahman El Shirazy",
        "tahun_terbit": 2004
      },
      {
        "judul": "Negeri 5 Menara",
        "penulis": "A. Fuadi",
        "tahun_terbit": 2009
      },
      {
        "judul": "Cantik Itu Luka",
        "penulis": "Eka Kurniawan",
        "tahun_terbit": 2002
      },
      {
        "judul": "Perahu Kertas",
        "penulis": "Dee Lestari",
        "tahun_terbit": 2009
      },
      {
        "judul": "Dilan 1990",
        "penulis": "Pidi Baiq",
        "tahun_terbit": 2014
      },
      {
        "judul": "Sang Pemimpi",
        "penulis": "Andrea Hirata",
        "tahun_terbit": 2006
      },
      {
        "judul": "Pulang",
        "penulis": "Tere Liye",
        "tahun_terbit": 2015
      },
      {
        "judul": "Garis Waktu",
        "penulis": "Fiersa Besari",
        "tahun_terbit": 2016
      }
    ]

    for book in buku:
        print(f"Judul: {book['judul']}")
        print(f"Penulis: {book['penulis']}")
        print(f"Tahun Terbit: {book['tahun_terbit']}\n")


soal_1()
