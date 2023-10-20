def create_array(n):
    # Step 1: Decide the size of the array
    # Create an array 'A' with 'n' elements
    A = [0] * n

    # Step 3: Initialize the subscript variable
    i = 1

    # Step 4: Loop through the array
    while i <= n:
        # Step 5: Accept data values for the array element A(i)
        data_value = int(input(f"Enter data value for A({i}): "))
        A[i - 1] = data_value  # Subtract 1 to adjust for 0-based indexing

        # Step 6: Increment the subscript
        i += 1

    # Step 7: Stop
    return A

# Input: Decide the size of the array
n = int(input("Enter the size of the array: "))

# Create the array by calling the function
resulting_array = create_array(n)

# Display the resulting array
print("Resulting Array:", resulting_array)
