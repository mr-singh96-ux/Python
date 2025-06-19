a=int(input("Enter Number1:"))
b=int(input("Enter Number2:"))
print(f"Odd Numbers Between {a} and {b} are as follows:")
for i in range(a,b):
    if i%2!=0:
        print(i)

        