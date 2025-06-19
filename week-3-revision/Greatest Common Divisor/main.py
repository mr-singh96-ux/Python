def gcd():
    a=int(input("Enter Number1:"))
    b=int(input("Enter Number2:"))
    print(f"a={a}")
    print(f"b={b}")
    while b!=0:
        a,b=b,a%b
    c=a 
    print(f"The GCD is {c}")
gcd()

def gcd(a,b):
    print(f"a={a}")
    print(f"b={b}")
    while b!=0:
        a,b=b,a%b
    c=a 
    print(f"The GCD is {c}")
a=int(input("Enter Number1:"))
b=int(input("Enter Number2:"))
gcd(a,b)


# import math
# a=int(input("Enter Number1:"))
# b=int(input("Enter Number2:"))
# def g(a,b):
#     g=math.gcd(a,b)
#     return g
# result=g(a,b)
# print(f"The hcf of {a} and {b} is {result}")

# x=0
# for x in range(1,11):
#     print(x)