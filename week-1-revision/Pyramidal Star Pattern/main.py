# n=6
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range(i):
#         print("*",end='')
#     for j in range(i+1):
#         print("*",end='')
#     print()  

# n=5
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ", end='')
#     for j in range((2*i)-1):
#         print("*",end='')
#     print() 

# n=int(input("Enter Size:"))
# for i in range(n,0,-1):
#     for k in range(n-i):
#         print(" ", end='')
#     for j in range(2*i-1):
#         print("*",end='')
#     print() 

# n=int(input("Enter Size:"))
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ", end='')
#     for j in range((2*i)-1):
#         print(i,end='')
#     print() 
# for i in range(n-1,0,-1):
#     for k in range(n-i):
#         print(" ", end='')
#     for j in range(2*i-1):
#         print(i,end='')
#     print() 

# n=int(input("Enter Size:"))
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ", end='')
#     for j in range((2*i)-1):
#         print("*",end='')
#     print() 
# for i in range(n-1,0,-1):
#     for k in range(n-i):
#         print(" ", end='')
#     for j in range(2*i-1):
#         print("*",end='')
#     print() 

# ascii=65
# n=6
# for i in range(0,n):
#     for j in range(i+1):
#         print(chr(ascii+i),end='')
#     print()   

# n=int(input("Enter Size:"))
# a=1
# for i in range(0,n):
#     for j in range(i+1):
#         print(int(a+i),end='')
#     print()

def s(n):
    for i in range(1,n+1):
        for k in  range(n-i):
            print(" ", end='')
        for j in range(2*i-1):
            print("*", end='')
        print()
            
    for i in range(n-1,0,-1):
        for k in  range(n-i):
            print(" ", end='')
        for j in range(2*i-1):
            print("*", end='')
        print()
n=int(input())
s(n)
        