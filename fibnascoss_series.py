x = int(input("Enter number:"))
n = int(input("Enter the number you want to check:"))

def fab(a):
    i, j = 0, 1                     # Initialize i and j inside the function
    fib_series = [i, j]             # Start the series with the first two Fibonacci numbers
    print(i)
    print(j)
    for _ in range(a-2):            # Generate Fibonacci numbers until limit
        k = i + j
        fib_series.append(k)        # Add the new Fibonacci number 'k' to the list
        print(f"{i} + {j} = {k}")
        i, j = j, k                 # Update i and j for the next iteration
    return fib_series               # Return the generated Fibonacci series
fibonacci_numbers = fab(x)          # Generate the Fibonacci series
if n in fibonacci_numbers:          # Check if the number n is in the Fibonacci series
    print(f"The number {n} is in the Fibonacci series.")
else:
    print(f"The number {n} is not in the Fibonacci series.")