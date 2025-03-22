"""
1. Membuat Fungsi Penjumlahan
Buat sebuah fungsi bernama add_numbers yang menerima dua parameter dan mengembalikan hasil penjumlahannya.

Tantangan tambahan:
    • Pastikan fungsi dapat menangani input berupa angka desimal.
    • Tambahkan validasi untuk memastikan hanya angka yang dapat dijumlahkan.

Contoh Input/Output:
    📤 print(add_numbers(5, 3))  # Output: 8
    📤 print(add_numbers(4.5, 2.5))  # Output: 7.0
"""

def penjumlahan(nom1, nom2):
    if type(nom1) == str or type(nom2) == str:
        return
    elif type(nom1) == bool or type(nom2) == bool:
        return
    else:
        return nom1 + nom2

print(f"""
Penjumlahan:
{penjumlahan(5, 3)}
{penjumlahan(4.5, 2.5)}
{penjumlahan("Forest", "Beach")}
{penjumlahan(True, False)}
""")
      
"""
2. Memeriksa Bilangan Prima
      Buat sebuah fungsi bernama is_prime yang menerima satu parameter (bilangan bulat), 
      dan mengembalikan True jika bilangan tersebut adalah bilangan prima, dan False jika tidak.

Contoh Input/Output:
    📤 print(is_prime(5))  # Output: True
    📤 print(is_prime(10))  # Output: False
"""

def bilangan_prima(num):
    flag = True
    if num == 0 or num == 1:
        print("Unkown Value!")
    elif num > 0:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
    return flag

print(f"""
Bilangan Prima:
{bilangan_prima(5)}
{bilangan_prima(10)}
{bilangan_prima(13)}
{bilangan_prima(22)}
""")

"""
3. Hitung Total Harga Makanan
      Buat fungsi bernama calculate_total yang menerima daftar harga makanan (list) dan mengembalikan totalnya.

Contoh Input/Output:
    📤 prices = [10000, 15000, 20000, 12000]
    📤 print(calculate_total(prices))  # Output: 57000
"""

def total_kalkulasi(harga):
    harga = [10000, 15000, 20000, 12000]
    total = 0
    for i in harga:
        total += i
    return total

print(f"""
Total Kalkulasi:
{total_kalkulasi(0)}
""")

"""
4. Menghitung Faktorial
      Buat fungsi bernama factorial yang menerima satu parameter (bilangan bulat) dan mengembalikan faktorialnya.
      Gunakan perulangan atau rekursi untuk menyelesaikannya.

Contoh Input/Output:
    📤 print(factorial(5))  # Output: 120
    📤 print(factorial(0))  # Output: 1
"""

def faktorial (num):
    factorial = 1
    for i in range(1,num + 1):
       factorial = factorial*i
    return factorial

print(f"""
Faktorial:
{faktorial(0)}
{faktorial(5)}
""")

"""
5. Konversi Suhu
Buat dua fungsi:
    • celsius_to_fahrenheit untuk mengonversi suhu dari Celsius ke Fahrenheit.
    • fahrenheit_to_celsius untuk mengonversi suhu dari Fahrenheit ke Celsius.

Formula:
    • Fahrenheit = (Celsius × 9/5) + 32
    • Celsius = (Fahrenheit - 32) × 5/9

Contoh Input/Output:
    📤 print(celsius_to_fahrenheit(25))  # Output: 77.0
    📤 print(fahrenheit_to_celsius(77))  # Output: 25.0
"""

def celsius_to_fahrenheit(c_degree):
    return c_degree * (9 / 5) + 32

def fahrenheit_to_celsius(f_degree):
    return (f_degree - 32) * (5 / 9)

print(f"""
Degree Converter:
{celsius_to_fahrenheit(25)}
{fahrenheit_to_celsius(77)}
""")

"""
6. Simulasi Penarikan Uang ATM
Buat fungsi bernama withdraw_money yang menerima dua parameter:
    • balance (saldo awal)
    • amount (jumlah yang ingin ditarik)

Fungsi harus mengembalikan sisa saldo jika penarikan berhasil, atau pesan error jika saldo tidak mencukupi atau jumlah penarikan tidak valid.

Contoh Input/Output
    📤 print(withdraw_money(50000, 20000))  # Output: 30000
    📤 print(withdraw_money(50000, 60000))  # Output: "Saldo tidak mencukupi."
"""

def withdraw_money(balance, amount):
    if type(balance) == str or type(amount) == str:
        return "Jumlah penarikan tidak valid!"
    elif amount > balance:
        return "Saldo tidak mencukupi."
    else:
        return balance - amount

print(f"""
Withdrawal:
{withdraw_money(50000, 20000)}
{withdraw_money(50000, 60000)}
{withdraw_money("Apache", "Running")}
""")

"""
7. Mencari Nilai Tertinggi di List
Buat fungsi bernama find_max yang menerima list angka dan mengembalikan nilai terbesar.

Tantangan tambahan:
    • Jangan gunakan fungsi bawaan seperti max.

Contoh Input/Output
    📤 numbers = [5, 9, 3, 8, 4]
    📤 print(find_max(numbers))  # Output: 9
"""

numbers = [12, 7, 4, 1, 8, 24]
def find_max(numbers):
    max_numbers = 0
    for i in numbers:
        if i > max_numbers:
            max_numbers = i
    return max_numbers

print(f"""
Max Numbers:
{find_max(numbers)}
""")
