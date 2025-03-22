n = 5
p = 5

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
