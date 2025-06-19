import math
a=int(input("Enter Number1:"))
b=int(input("Enter Number2:"))
def l(a,b):
    g=math.gcd(a,b)
    l=(a*b)//g
    return l
result=l(a,b)
print(f"The lcm of {a} and {b} is {result}")

def lcm():
    a=int(input("Enter Number1:"))
    b=int(input("Enter Number2:"))
    print(f"a={a}")
    print(f"b={b}")
    def gcd(x,y):
        while y!=0:
            x,y=y,x%y
        return x
    l=(a*b)//gcd(a,b)
    print(f"The lcm is {l}")
lcm()
    