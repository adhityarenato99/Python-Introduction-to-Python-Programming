def print_multiplication_tables():
    for i in range(1, 6):  # Loop through the numbers 1 to 5
        print(f"Multiplication Table for {i}:")
        for j in range(1, 11):  # Multiply from 1 to 10
            result = i * j
            print(f"{i} x {j} = {result}")
        print()  # Add a blank line between tables

# Call the function to print the tables
print_multiplication_tables()
