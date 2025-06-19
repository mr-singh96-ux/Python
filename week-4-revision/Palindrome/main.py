rev=0
a=int(input("Enter any number:"))
c=a
while a>0:
    b=a%10
    rev=rev*10+b
    a=a//10
    print(f"The reverse of the number is {rev}")
if c==rev:
    print("Thus the number is a palindrome")
else:
    print("Thus the number is not a palindrome")
