# Get the range limit from the user
n = int(input("Enter range:"))
# Print a header for odd numbers
print("These numbers are odd:")
# Loop through numbers from 0 to n-1
for i in range(n):
    # Check if the number is odd
    if i%2!=0:
        # Print the odd number
        print(i)
