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
