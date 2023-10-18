# Problem 3.2

# Give the user some context.
print("\nWelcome to sales commission calculation. What would you like to do?")

y = ''

def myfunc():
    if (s > 5000):
        com = (s - 5000) * 0.12
        result = com + f
    else:
        com = 0
        result = com + f

    # print("The result is " + str(com))
    print("The renumeration is " + str(result))

while y != 'y':
    print("\n[1] Enter 1 to continue.")
    print("[q] Enter y to finish and quit.")

    y = input("\nContinue to input sales amount (SAMT)? ")
    
    if y == '1':
        s = int(input("Enter sales amount (SAMT): "))
        f = int(input("Enter fixed salary (FSAL): "))
        myfunc()
    # else:
    #     print("\nI don't understand that choice, please try again.\n")


# Print a message that we are all finished.
print("Thanks again, bye now.")