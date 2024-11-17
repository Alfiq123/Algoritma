n = int(input("Masukkan Angka: "))

def nomor_5():
    for i in range(n):
        print("INFORMATIKA")
    print()

nomor_5()

def nomor_6():
    x = 1
    for i in range(n):
        print(f"INFORMATIKE KE-{x}")
        x += 1
    print()

nomor_6()

text = str(input("Masukkan Teks: "))

def nomor_7():
    for i in text:
        print(i)
    print()

nomor_7()

def nomor_8():
    text = str(input("Masukkan Teks: "))
    for i in text:
        if i == " ":
            text = text.replace(" ", "")
        else:
            print(i)
    print()

nomor_8()

# # Example string
# text = "Hello World! This is a test string."

# # Initialize an empty string to store the result
# result = ""

# # Iterate through each character in the original string
# for char in text:
#     # Only add the character to the result if it's not a space
#     if char != ' ':
#         result += char

# print(result)