# a=int(input("Enter any number: "))
# i=int(input("Enter size:"))
# for i in range(0,i):
#     i+=1
#     result=a*i
#     print(f"{a}*{i}={result}")
    
# def t(a):
#     for i in range(0,a):
#         i+=1
#         result=n*i
#         print(f"{i}*{i}={result}")
# n=int(input())
# a=int(input())
# t(a)

# def T(n):
# 	for i in range(0,6):
# 		result=n*i
# 		print(f"{n}*{i}={result}")
# n=int(input())
# T(n)

def avg(a, b, c, d):
    print((a + b + c + d) / 4)

while True:
    a = input()
    if a == "exit":
        break
    b = input()
    c = input()
    d = input()
    avg(int(a), int(b), int(c), int(d))

    