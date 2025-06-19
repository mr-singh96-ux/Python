def generate_pascals_triangle(n):
    # Initialize an empty list to hold the triangle
    triangle = []

    for row in range(n):
        # Start each row with a list of ones
        current_row = [1] * (row + 1)

        # Update the elements between the first and last element in the row
        for col in range(1, row):
            current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

        # Add the current row to the triangle
        triangle.append(current_row)

    # Print the triangle
    for row in triangle:
        print(" ".join(map(str, row)).center(n * 2))

# Input number of rows
num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
generate_pascals_triangle(num_rows)
