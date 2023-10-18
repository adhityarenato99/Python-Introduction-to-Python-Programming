# Problem 3.7. 
# ----------------------------------------------------
# Draw a flowchart to show how to obtain the sum of the first
# 30 natural numbers.

sum = 0
i = 1
count = 0

# for count in range(i, 30 + 1):
#     sum += count

# print("Sum is", sum)

while count <= 30:
    sum = sum + i
    count = count + 1

    # comput i = i + 1
    i = i + 1
    
print("The sum of the first 30 natural numbers is:", sum)