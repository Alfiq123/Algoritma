n = int(input("\nMasukkan Angka: "))

def increasing() -> None:
    print("Increasing Triangle: \n")
    for i in range(1, n + 1):
        p = 1
        for j in range(i, 0, -1):
            print(j, end=" ")
            p += 1
        print()
    print()

increasing()
