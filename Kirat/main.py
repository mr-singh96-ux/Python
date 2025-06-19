# a=int(input("Enter Number:"))
# rev=0
# while a>0:
#     rev=(rev*10)+a%10
#     a=a//10
#     print(rev)

# def fact_value(n):
#     result=1
#     for i in range(2,n+1):
#         result *= i
#     return result
# print(fact_value(5))

for i in range(1,6):
    for k in range(5-i):
        print(" ", end="")
    print("*"*i, end=" ")
    print()