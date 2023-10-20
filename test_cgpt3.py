# Step 1: Declare an array (using a list in Python) of size 100
A = [0] * 10

# Step 2: Initialize the subscript variable 'I'
I = 1

# Step 3: Fill the array with natural numbers
while I <= 10:
    A[I - 1] = I  # Subtract 1 to adjust for 0-based indexing
    I += 1

# Step 6: Initialize 'I' again with the starting print location
I = 10

# Step 7: Print the numbers in reverse order
while I >= 1:
    print(A[I - 1])  # Subtract 1 to adjust for 0-based indexing
    I -= 1
