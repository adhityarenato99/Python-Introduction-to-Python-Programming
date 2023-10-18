def sum_of_first_30_natural_numbers():
    # Initialize variables
    SUM = 0
    I = 1
    COUNT = 0

    # Repeat steps 3 through 5 while COUNT <= 30
    while COUNT <= 30:
        # Compute SUM = SUM + I
        SUM = SUM + I

        # Compute COUNT = COUNT + 1
        COUNT = COUNT + 1

        # Compute I = I + 1
        I = I + 1

    # Print the sum
    print("THE SUM IS", SUM)

# Call the function to calculate the sum
sum_of_first_30_natural_numbers()