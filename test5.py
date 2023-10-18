# Problem 3.3. 
# ---------------------------------------------------------------
# A labor contractor pays the workers at the end of each week 
# according to the rules given below:
# For the first 35 hours of work, the rate of pay is $15 per hour; for the next 25 
# hours, the rate of pay is $18 per hour; for the rest, the rate of pay is $26 per 
# hour. No worker is allowed to work for more than 80 hours in a week. Develop 
# a flowchart to show how the wages of the workers can be calculated on the 
# basis of valid inputs.

# Give the user some context.
print("\nWelcome to wages calculation. What would you like to do?")

y = ''

def myfunc():
    if (s <= 0):
        exit()
    else:
        if (s > 80):
            print("Invalid hours")  
        else:

            if (s <= 35):
                com = s * 15
            elif (s <= 60):
                com = (35 * 15) + (s - 35) * 18
            else:
                com = 35 * 15 + 25 * 18 + (s - 60) * 25
        
            print("The wage is " + str(com))

while y != 'y':
    print("\n[1] Enter 1 to continue.")
    print("[q] Enter y to finish and quit.")

    y = input("\nContinue to do the calculation? ")
        
    if y == '1':
        s = int(input("Input the total hours: "))
        myfunc()

# Print a message that the calcuation is finished.
print("Thanks again, bye now.")
