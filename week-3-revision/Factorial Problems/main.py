def f():
    f=1
    i=int(input("Enter Number:"))
    for x in range(1,i+1):
        f*=x
        print(f"The factorial of {i} is:{f}")
f()        