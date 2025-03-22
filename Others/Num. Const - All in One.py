n = 5

def increasing() -> None:
    print("Increasing Triangle: \n")
    for i in range(n):
        p = 1
        for j in range(i + 1):
            print(p, end=" ")
            p += 1
        print()
    print()

increasing()

def decreasing() -> None:
    print("Decreasing Triangle: \n")
    for i in range(n):
        p = 1
        for j in range(i, n):
            print(p, end=" ")
            p += 1
        print()
    print()

decreasing()

def left_pascal() -> None:
    print(" Left Pascal Triangle: \n")
    for i in range(n - 1):
        p = 1
        for j in range(i + 1):
            print(p, end=" ")
            p += 1
        print()
    for i in range(n):
        p = 1
        for j in range(i, n):
            print(p, end=" ")
            p += 1
        print()
    print()

left_pascal()

def right_pascal() -> None:
    print("Right Pascal: \n")
    for i in range(n - 1):
        p = 1
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i + 1):
            print(p, end=" ")
            p += 1
        print()
    for i in range(n):
        p = 1
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print(p, end=" ")
            p += 1
        print()
    print()

right_pascal()

def hill() -> None:
    print("Hill: \n")
    for i in range(n):
        p = 1
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print(p, end=" ")
            p += 1
        for j in range(i + 1):
            print(p, end=" ")
            p += 1
        print()
    print()

hill()

def reverse_hill() -> None:
    print("Reverse Hill: \n")
    for i in range(n):
        p = 1
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print(p, end=" ")
            p += 1
        for j in range(i, n - 1):
            print(p, end=" ")
            p += 1
        print()
    print()

reverse_hill()

def diamond() -> None:
    print("Diamond: \n")
    for i in range(n - 1):
        p = 1
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print(p, end=" ")
            p += 1
        for j in range(i + 1):
            print(p, end=" ")
            p += 1
        print()
    for i in range(n):
        p = 1
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print(p, end=" ")
            p += 1
        for j in range(i, n - 1):
            print(p, end=" ")
            p += 1
        print()
    print()

diamond()

def increased() -> None:
    p = 1
    for i in range(n):
        for j in range(i + 1):
            print(p, end=" ")
            p += 1
        print()
    print()

increased()

def increased_2() -> None:
    p = 1
    for i in range(n):
        for j in range(n):
            print(p, end=" ")
            p += 1
        print()
    print()

increased_2()

def insert() -> None:
    baris = 15
    kolom = 5
    name = str(input("Masukkan Nama: "))
    for i in range(baris):
        for j in range(kolom):
            print(f"{name}", end=" ")
        print()
    print()
    
insert()
