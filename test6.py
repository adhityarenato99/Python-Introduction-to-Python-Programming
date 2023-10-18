# Problem 3.5. 
# ----------------
# The cost of living (CL), the travel allowance (TA), and medical
# allowance (MA) of the employees of a company are decided according to the
# following rules:
# CL = 123.75% of the Basic Pay, subject to a minimum of $2,000 and a
# maximum
# of $5,000.
# TA = 57.5% of the Basic Pay, subject to a minimum of $300.
# MA = 73.5% of the Basic Pay, subject to a maximum of $2,000.
# Draw a flowchart to show how CL, TA, and MA are calculated.

# Give the user some context.
print("\nWelcome to cost of living (CL), trave allowance (TA), and medical allowance (MA) calculation")

y = ''
# cl = ''
result = ''

def myfunc(cl):

    if (cl < 2000):
        result = 2000
    elif (cl > 2000 and cl < 5000):
        result = 3500
    elif (cl > 5000):
        result = 5000
    
    print("The cost of living is " + str(result))

def calcTA(ta):

    if (ta < 300):
        result = 300
    else: 
        result = ta

    print("The cost of travel allowance is " + str(result))

def calcMA(ma):

    if (ma > 2000):
        result = 2000
    else:
        result = ma
    
    print("The cost of medical allowance is " + str(result))


while y != 'n':
    print("\n[y] Enter y to continue.")
    print("[n] Enter n to finish and quit.")

    y = input("\nContinue to do the calculation? ")

    if y == 'y':
        s = int(input("Input basic pay of an employee: "))
        cl = s * 123.75/100
        ta = s * 57.5/100
        ma = s * 0.735
        myfunc(cl)
        calcTA(ta)
        calcMA(ma)
        # print(result)


print("Thanks again, bye now.")