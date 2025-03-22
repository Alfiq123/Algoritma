from random import randint

print(r"""
  _____    _          _       _             _        
 |_   _|__| |__  __ _| |__   /_\  _ _  __ _| |____ _ 
   | |/ -_) '_ \/ _` | / /  / _ \| ' \/ _` | / / _` |
   |_|\___|_.__/\__,_|_\_\ /_/ \_\_||_\__, |_\_\__,_|
                                      |___/          
""")

nyawa = 0
proses = True
answer = randint(1, 100)
tingkat_kesulitan = str(input("Masukkan tingkat kesulitan (Mudah, Normal, Sulit): "))

if tingkat_kesulitan in ("Mudah", "mudah", "MUDAH"):
    nyawa = 10
elif tingkat_kesulitan in ("Normal", "normal", "NORMAL"):
    nyawa = 7
elif tingkat_kesulitan in ("Sulit", "sulit", "SULIT"):
    nyawa = 5
else:
    print("Tingkat Kesulitan tidak ada yang dipilih, Sesi dimatikan!")

print(f"Kamu memilih: {tingkat_kesulitan}\n")

while proses:
    print(f"️️❤️ = {nyawa}")

    if nyawa <= 0:
        print("\nNyawamu sudah habis! KAMU KALAH 🚨")
        proses = False

    user_choose = int(input("Pilih angka (1 - 100): "))

    if user_choose == answer:
        print("\nTebakanmu Benar! SELAMAT, KAMU MENANG! 🎉")
        proses = False

    elif user_choose < answer:
        nyawa -= 1
        print("\nTebakanmu Terlalu Rendah! COBA LAGI!")

    elif user_choose > answer:
        nyawa -= 1
        print("\nTebakanmu Terlalu Tinggi! COBA LAGI!")
