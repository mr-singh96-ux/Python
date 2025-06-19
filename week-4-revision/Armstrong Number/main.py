a=int(input("Enter Number: "))
c=a
b=0
i=0
while a>0:
    b=a%10
    i=i+b**3
    a=a//10
print(f"The Sum Of Cubes Of Digits are {i}")
if c==i:
    print(f"The given number {c} is an Armstrong Number.")
else:
    print(f"The given number {c} is not an Armstrong Number.")