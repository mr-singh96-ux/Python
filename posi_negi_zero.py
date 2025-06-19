def func(a):                                    # Create a function "func". 
     if a>0:                                    # Check if the number is positive.
         print("The number is Positive")
     elif a<0:                                  # Check if the number is negative.
         print("The number is Negative")
     else:                                      # The number is zero.
         print("The number is zero")
p=int(input("Enter number: "))                  # Get a number from the user.     
func(p)                                         # Call the function with the user input.