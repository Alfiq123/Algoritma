# n = 5

n = int(input("Masukkan Angka: "))

# Basics.

def square_pattern():
    print("Square Pattern:\n")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
    print()

square_pattern()

def increasing_triangle():
    print("Increasing Triangle:\n")
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
    print()

increasing_triangle()

def decreasing_triangle():
    print("Decreasing Triangle:\n")
    for i in range(n):
        for j in range(i, n):
            print("*", end=" ")
        print()
    print()

decreasing_triangle()

# Patterns.

def increasing_right_sided_triangle():
    print("Increasing Right Sided Triangle:\n")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    print()

increasing_right_sided_triangle()

def decreasing_right_sided_triangle():
    print("Decreasing Right Sided Triangle:\n")
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    print()

decreasing_right_sided_triangle()

def hill():
    print("Hill:\n")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    print()

hill()

def reverse_hill():
    print("Reverse Hill:\n")
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n - 1):
            print("*", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    print()

reverse_hill()

def diamond():
    print("Diamond:\n")
    for i in range(n - 1):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n - 1):
            print("*", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    print()

diamond()

# Pyramid Groups.

def pyramid():
    print("Pyramid:\n")
    for i in range(n):
        for j in range(i, n):
            print("", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    print()

pyramid()

def reverse_pyramid():
    print("Reverse Pyramid:\n")
    for i in range(n):
        for j in range(i + 1):
            print("", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    print()

reverse_pyramid()

def diamond_pyramid():
    print("Diamond Pyramid:\n")
    for i in range(n - 1):
        for j in range(i, n):
            print("", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(i + 1):
            print("", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    print()

diamond_pyramid()

def sandglass():
    print("Sandglass:\n")
    for i in range(n - 1):
        for j in range(i + 1):
            print("", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(i, n):
            print("", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    print()

sandglass()

def left_pascal_triangle():
    print("Left Pascal Triangle:\n")
    for i in range(n - 1):
        for j in range(i + 1):
            print("*", end=" ")
        print()

    for i in range(n):
        for j in range(i, n):
            print("*", end=" ")
        print()
    print()

left_pascal_triangle()

def right_pascal_triangle():
    print("Right Pascal Triangle:\n")
    for i in range(n - 1):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()

    for i in range(n):
        for j in range(i + 1):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print()
    print()

right_pascal_triangle()

def butterfly():
    print("Butterfly Alpha:\n")
    for i in range(n - 1):

        for j in range(i + 1):
            print("*", end=" ")

        for j in range(n - i - 1):
            print(" ", end=" ")

        for j in range(n - i - 1):
            print(" ", end=" ")

        for j in range(i + 1):
            print("*", end=" ")
            
        print()

    for i in range(n - 1, -1, -1):

        for j in range(i + 1):
            print("*", end=" ")

        for j in range(n - i - 1):
            print(" ", end=" ")
            
        for j in range(n - i - 1):
            print(" ", end=" ")

        for j in range(i + 1):
            print("*", end=" ")

        print()

butterfly()