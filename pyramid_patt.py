n=int(input("Enter Size:"))         # Take input from the user for the size of the pattern
for i in range(n,0,-1):             # Outer loop: starts from n and decreases to 1
    for j in range(i):              # Inner loop: runs i times
        print(int(n-i+1),end='')    # Print the current number (1 to n) without a newline
    print()                         # Move to the next line after finishing the inner loop