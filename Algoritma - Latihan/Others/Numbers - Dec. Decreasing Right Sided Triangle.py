n = 5
p = 5

print("Dec. Decreasing Right Sided Triangle: \n")

for i in range(n):
    
    for j in range(i + 1):
        print(" ", end=" ")

    for i in range(i, n):
        print(p, end=" ")

    p -= 1
    print()

print()
