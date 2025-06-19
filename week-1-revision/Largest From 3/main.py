a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))

if a>b and a>c:
    print(f"a={a} is the largest number")
if b>a and b>c:
    print(f"b={b} is the largest number")
else:
    print(f"c={c} is the largest number")    