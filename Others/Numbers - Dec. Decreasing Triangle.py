n = 5
p = 5

for i in range(n):
    for j in range(i, n):
        print(p, end=" ")
    p -= 1
    print()
