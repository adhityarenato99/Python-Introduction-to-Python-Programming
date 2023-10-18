# Problem 3.2

# Give the user some context.
print("\nWelcome to task analysist. What would you like to do?")

y = ''

# s = 100000

def myfunc():
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

while y != 'q':

    print("\n[1] Enter 1 to continue.")
    print("[q] Enter q to quit.")

    y = input("\nContinue to entering amount of fixed salary? ")
    
    if y == '1':
        s = int(input("Enter sales amount: "))
        myfunc()
    else:
        print("\nI don't understand that choice, please try again.\n")

# Print a message that we are all finished.
print("Thanks again, bye now.")