matrix=[]                                   # Initialize an empty list to hold the matrix.
row=int(input("Enter no. of rows:"))        # Get the number of rows from the user.
print("Enter elements by adding space.")    # Tell the user for input format.
for i in range(row):                        # Loop to input each row of the matrix.
    row=input(f"Enter {i+1}:").split()      # Get input for the current row and split into elements.
    matrix.append([int(num) for num in row])# Convert each element to an integer and add to the matrix.
print("Matrix is:")                         # Indicate that the matrix will be displayed.
for row in matrix:
    print(row)                              # Print each row of the matrix.

for i in range(len(matrix)):                # Loop to calculate and print the sum of each row.
    print(f"Sum of row {i + 1}: {sum(matrix[i])}") # Calculate and display the sum of the current row.