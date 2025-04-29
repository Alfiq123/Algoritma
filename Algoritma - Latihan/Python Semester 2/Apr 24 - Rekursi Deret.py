def deret1(n):
    """ S = 3 - 6 + 9 - 12 + 15 - 18 + 21 - ... """
    if n == 1:
        return [3]
    else:
        return deret1(n - 1) + [(-1) ** (n + 1) * 3 * n]
    
def deret2(n):
    """ S = 1 - 3 + 5 - 7 + 9 - 11 + 13 - ... """
    if n == 1:
        return [1]
    else:
        return deret2(n - 1) + [round((-1) ** (n - 1) * (2 * n - 1), 4)]
    
def deret3(n):
    """ S = (1/1) - (1/2) + (1/3) - (1/4) + (1/5) - ... """
    if n == 1:
        return [1]
    else:
        return deret3(n - 1) + [round((-1) ** (n + 1) * (1 / n), 4)]
    
def deret4(n):
    """ S = (1/2) - (1/4) + (1/6) - (1/8) + (1/10) - ... """
    if n == 1:
        return [1 / 2]
    else:
        return deret4(n - 1) + [round((-1) ** (n + 1) * (1 / (2 * n)), 4)]

def deret5(n):
    """ S = (2/3) - (4/9) + (8/27) - (16/81) + (32/243) - ... """
    if n == 1:
        return [round(2 / 3, 4)]
    else:
        return deret5(n - 1) + [round((-1) ** (n + 1) * (2 ** n) / (3 ** n), 4)]

print(deret1(10))
print(deret2(10))
print(deret3(10))
print(deret4(10))
print(deret5(10))

print()

print(round(sum(deret1(10)), 4))
print(round(sum(deret2(10)), 4))
print(round(sum(deret3(10)), 4))
print(round(sum(deret4(10)), 4))
print(round(sum(deret5(10)), 4))

print()

def deret_gpt1(n):
    """ S = 5 - 10 + 15 - 20 + 25 - 30 + 35 - ... """
    if n == 1:
        return [5]
    else:
        return deret_gpt1(n - 1) + [(-1) ** (n + 1) * 5 * n]

def deret_gpt2(n):
    """ S = 2 - 4 + 6 - 8 + 10 - 12 + 14 - ... """
    if n == 1:
        return [2]
    else:
        return deret_gpt2(n - 1) + [(-1) ** (n + 1) * 2 * n]
    
def deret_gpt3(n):
    """ S = 1/1 - 2/2 + 3/3 - 4/4 + 5/5 - 6/6 + ... """
    if n == 1:
        return [1]
    else:
        return deret_gpt3(n - 1) + [(-1) ** (n + 1) * 1]

def deret_gpt4(n):
    """ S = 1/3 - 1/6 + 1/9 - 1/12 + 1/15 - ... """
    if n == 1:
        return [round(1 / 3), 4]
    else:
        return deret_gpt4(n - 1) + [round((-1) ** (n + 1) * (1 / (3 * n)), 4)]
    
def deret_gpt5(n):
    """ S = 3/2 - 9/4 + 27/8 - 81/16 + ... """
    if n == 1:
        return [round(3 / 2)]
    else:
        return deret_gpt5(n - 1) + [round((-1) ** (n + 1) * (3 ** n) / (2 ** n), 4)]

print(deret_gpt1(10))
print(deret_gpt2(10))
print(deret_gpt3(10))
print(deret_gpt4(10))
print(deret_gpt5(10))

print()

print(sum(deret_gpt1(10)))
print(sum(deret_gpt2(10)))
print(sum(deret_gpt3(10)))
print(sum(deret_gpt4(10)))
print(sum(deret_gpt5(10)))

print()
