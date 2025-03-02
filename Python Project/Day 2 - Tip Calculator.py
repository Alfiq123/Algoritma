print("Welcome to the tip Calculator!")

bill = int(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give?: "))
split = int(input("How many people to split the bill?: "))

totaltip = tip / 100 * bill
totalbill = (bill + totaltip) / split

print(bill)
print(tip)
print(split)
print(totaltip)
print("Each person should pay: $", totalbill)