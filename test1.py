# Problem 3.1

# s = 100000
s = int(input("Enter sales amount: "))

if (s <= 0):
    exit()

if (s <= 5000):
    com = s * 0.07
else:
    if (s <= 10000):
        com = s * 0.09 + 500
    elif (s <= 20000):
        com = s * 0.11 + 1000
    elif (s <= 25000):
        com = s * 0.13 + 2000
    else:
        com = s * 0.15 + 4000


print(com)