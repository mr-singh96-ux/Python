a=int(input("Enter num1: "))            #Get first number from user.
b=int(input("Enter num2: "))            #Get second number from user.
print("Before swaping")                 # Print numbers before swapping.
print(f"num1={a}")
print(f"num2={b}")
a,b=b,a                                 # Swap the values of a and b.
print("After swaping")                  # Print numbers after swapping.
print(f"num1={a}")
print(f"num2={b}")