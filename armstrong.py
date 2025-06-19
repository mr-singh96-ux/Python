a=int(input("Enter Number: "))              # Get a number from the user.
c=a                                         # Store the original number for comparison later.
b=0                                         # Defining the variables for the digits.
i=0
while a>0:                                  # Loop to extract digits and calculate the sum of their cubes.
    b=a%10                                  # Get the last digit.
    i=i+b**3                                # Add the cube of the digit to the sum.
    a=a//10                                 # Remove the last digit.
print(f"The Sum Of Cubes Of Digits are {i}")# Print the sum of cubes of the digits.
if c==i:                                    # Check if the original number is equal to the sum of cubes.
    print(f"The given number {c} is an Armstrong Number.")
else:
    print(f"The given number {c} is not an Armstrong Number.")