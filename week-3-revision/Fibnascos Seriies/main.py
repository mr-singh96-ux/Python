n=int(input("Enter number:"))

def fib(n,a={}):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))

# x=int(input("Enter any number:"))
# i=0
# j=1

# def fab(i,j):
#     print(i)
#     print(j)
#     for a in range(x):
#         k=i+j
#         print(f"{i}+{j}={k}")
#         i=j
#         j=k
        
# fab(i,j)