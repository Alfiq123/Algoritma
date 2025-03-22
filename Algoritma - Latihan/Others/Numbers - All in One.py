n = 5
# n = int(input("Masukkan Angka: "))

# Incrementing Rows.

def increasing_triangle() -> None:
    print("Increasing Triangle: \n")
    for i in range(n):
        for j in range(i + 1):
            print(i + 1, end=" ")
        print()
    print()

increasing_triangle()

def decreasing_triangle() -> None:
    print("Decreasing Triangle: \n")
    for i in range(n):
        for j in range(i, n):
            print(i + 1, end=" ")
        print()
    print()

decreasing_triangle()

def increasing_right_sided_triangle() -> None:
    p = 1
    print("Increasing Right Sided Triangle: \n")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for i in range(i + 1):
            print(p, end=" ")
        p += 1
        print()
    print()

increasing_right_sided_triangle()

def decreasing_right_sided_triangle() -> None:
    p = 1
    print("Decreasing Right Sided Triangle: \n")
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for i in range(i, n):
            print(p, end=" ")
        p += 1
        print()
    print()

decreasing_right_sided_triangle()

def hill() -> None:
    p = 1
    print("Hill: \n")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print(p, end=" ")
        for j in range(i + 1):
            print(p, end=" ")
        p += 1
        print()
    print()

hill ()

def reverse_hill() -> None:
    p = 1
    print("Reverse Hill: \n")
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n - 1):
            print(p, end=" ")
        for j in range(i, n):
            print(p, end=" ")
        p += 1
        print()

reverse_hill()

def diamond() -> None:
    p = 1
    print("Diamond: \n")
    for i in range(n - 1):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print(p, end=" ")
        for j in range(i + 1):
            print(p, end=" ")
        p += 1
        print()
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n - 1):
            print(p, end=" ")
        for j in range(i, n):
            print(p, end=" ")
        p -= 1
        print()
    print()

diamond()

# Decrementing Rows.

def dec_increasing_triangle() -> None:
    p = n
    print("Dec. Increasing Triangle: \n")
    for i in range(n):
        for j in range(i + 1):
            print(p, end=" ")
        p -= 1
        print()
    print()

dec_increasing_triangle()

def dec_decreasing_triangle() -> None:
    p = n
    print("Dec. Decreasing Triangle: \n")
    for i in range(n):
        for j in range(i, n):
            print(p, end=" ")
        p -= 1
        print()
    print()

dec_decreasing_triangle()

def dec_increasing_right_sided_triangle() -> None:
    p = n
    print("Dec. Increasing Right Sided Triangle: \n")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for i in range(i + 1):
            print(p, end=" ")
        p -= 1
        print()
    print()

dec_increasing_right_sided_triangle()

def dec_decreasing_right_sided_triangle() -> None:
    p = n
    print("Dec. Decreasing Right Sided Triangle: \n")
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for i in range(i, n):
            print(p, end=" ")
        p -= 1
        print()
    print()

dec_decreasing_right_sided_triangle()

def dec_hill() -> None:
    p = n
    print("Dec. Hill: \n")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print(p, end=" ")
        for j in range(i + 1):
            print(p, end=" ")
        p -= 1
        print()
    print()

dec_hill ()

def dec_reverse_hill() -> None:
    p = n
    print("Dec. Reverse Hill: \n")
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n - 1):
            print(p, end=" ")
        for j in range(i, n):
            print(p, end=" ")
        p -= 1
        print()
    print()

dec_reverse_hill()

# Randoms.

def odd_numbers() -> None:
    p = 1
    print("Odd Numbers: \n")
    for i in range(n):
        for j in range(i + 1):
            print(p, end=" ")
        p += 2
        print()
    print()

odd_numbers()

def even_numbers() -> None:
    p = 0
    print("Even Numbers: \n")
    for i in range(n):
        for j in range(i + 1):
            print(p, end=" ")
        p += 2
        print()
    print()

even_numbers()

def one_two_numbers() -> None:
    print("One Two Numbers: \n")
    for i in range(n):
        for j in range(i + 1):
            if i % 2 == 0:
                print(1, end=" ")
            else:
                print(2 , end=" ")
        print()
    print()

one_two_numbers()

def hash_dollar() -> None:
    print("Hash Dollar: \n")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("$", end=" ")
        for j in range(i + 1):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("$", end=" ")
        print()
    print()

hash_dollar()

def reverse_hash_dollar() -> None:
    print("Reverse Hash Dollar: \n")
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n - 1):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("$", end=" ")
        for j in range(i, n):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("$", end=" ")
        print()
    print()

reverse_hash_dollar()

def diamond_hash_dollar() -> None:
    print("Diamond Hash Dollar: \n")
    for i in range(n - 1):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("$", end=" ")
        for j in range(i + 1):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("$", end=" ")
        print()
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n - 1):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("$", end=" ")
        for j in range(i, n):
            if i % 2 == 0:
                print("#", end=" ")
            else:
                print("$", end=" ")
        print()

diamond_hash_dollar()