n = 5
p = 1

for i in range(n):
    for j in range(i, n):
        print(i + 1, end=" ")
    print()

print()

for i in range(n):
    for j in range(i, n):
        print(p, end=" ")
    p += 1
    print()
