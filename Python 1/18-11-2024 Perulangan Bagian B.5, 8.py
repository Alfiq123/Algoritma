n = 5
text = str(input("Masukkan Apa Saja: "))

print("\nJawaban Nomor 5")
for i in range(n):
    print("INFORMATIKA")
print()

print("Jawaban Nomor 6")
x = 1
for i in range(n):
    print(f"INFORMATIKE KE-{x}")
    x += 1
print()

print("Jawaban Nomor 7")
for i in text:
    print(i)
print()

print("Jawaban Nomor 8")
for i in text:
    if i == " ":
        text = text.replace(" ", "")
    else:
        print(i)
print()
