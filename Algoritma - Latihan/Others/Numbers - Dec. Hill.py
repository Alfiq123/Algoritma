n = 5
p = 5

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