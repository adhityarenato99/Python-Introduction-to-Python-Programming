# Problem 3.6. 
# -------------------------------------------------------------
# Devise a procedure to find the sum of first n natural numbers,
# where n is any given integer, without using a formula.

# Give the user some context.
print("\nWelcome to sum first number. What would you like to do?")

y = ''

n = int(input("Please enter number of terms to add : "))

# total = 0
# i = 1
# num = 1

# for num in range(i, n + 1):
#     total += num

# print("Sum is", str(total))


# Alternate using for loop
# sum = 0

# if n < 0:
#     print("Please enter a positive number")
# else:
#     sum = 0

# # use while loop to iterate until zero

# while n > 0:
#     sum += n
#     n -= 1
    
# print("The sum is", sum)

"""
ALTERNATE USING WHILE
"""

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print(sum)