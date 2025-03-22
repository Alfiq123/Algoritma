n = 5
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
