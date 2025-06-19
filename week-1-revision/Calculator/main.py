while True:
    x = int(input("Enter Number1 (or 0 to exit): ")) 
    if x == 0:
        break
    y = int(input("Enter Number2: "))
    a = input("Enter Operation (+, -, *, /, %, //,**): ")
    if a=='+':
         print(x+y)
    elif a=='-':
         print(x-y)
    elif a=='*':
        print(x*y)
    elif a=='/':
        print(x/y)
    elif a=='%':
        print(x%y)
    elif a=='//':
        print(x//y)
    elif a=='**':
        print(x**y)
