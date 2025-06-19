# fact=1
# i=int(input("Enter Number:"))
# for n in range(1,i+1):
#     fact *=n
#     print(f"The Factorial of {i} is {fact}")

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(f"the factorial of {n} is {fact}")
n=int(input())
fact(n)