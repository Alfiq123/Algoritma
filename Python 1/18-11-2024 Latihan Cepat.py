n = 7

def jawaban_nomor_1():
    print("\nJawaban Nomor 1")
    for i in range(n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print()

jawaban_nomor_1()

def jawaban_nomor_2():
    print("Jawaban Nomor 2")
    for i in range(n):
        for j in range(i + 1, 0, -1):
            print(j, end=" ")
        print()
    print()

jawaban_nomor_2()

def jawaban_nomor_3():
    print("Jawaban Nomor 3")
    for i in range(n):
        for j in range(i + 1):
            if i % 2 == 0:
                print("$", end=" ")
            else:
                print("#", end=" ")
        print()
    print()

jawaban_nomor_3()

def jawaban_nomor_4():
    print("Jawaban Nomor 4")
    p = 1
    for i in range(n):
        for j in range(n):
            print(p, end=" ")
            p += 1
        print()
    print()

jawaban_nomor_4()

def jawaban_nomor_5():
    print("Jawaban Nomor 5")
    p = 1
    for i in range(n):
        for j in range(i + 1):
            print(p, end=" ")
            p += 1
        print()
    print()

jawaban_nomor_5()

def jawaban_nomor_6():
    print("Jawaban Nomor 6")
    p = 1
    for i in range(n - 1):
        for j in range(i + 1):
            print(p, end=" ")
        p += 1
        print()
    for i in range(n):
        for j in range(i, n):
            print(p, end=" ")
        p -= 1
        print()
    print()

jawaban_nomor_6()

def jawaban_nomor_7():
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                print("-", end=" ")
            elif j == 0 or j == n - 1:
                print("|", end=" ")
            else:
                print(" ", end=" ")
        print()

jawaban_nomor_7()
