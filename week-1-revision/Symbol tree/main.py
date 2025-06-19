for i in range(1,5):
    print("*"*i) #upper half triangle
    
for i in range(5,0,-1):
    print("*"*i) #lower half triangle
    
for i in range(1,5):
    for k in range(5-i):
        print(" ",end='')
    print("*"*i) #upper half triangle
    
for i in range(5,0,-1):
    for k in range(5-i):
        print(" ",end='')
    print("*"*i) #lower half triangle
    
def s(n):
    for i in range(1,n+1):
        for k in  range(n-i):
            print(" ", end='')
        print("*"*i)
            
    for i in range(n-1,0,-1):
        for k in  range(n-i):
            print(" ", end='')
        print("*"*i)
n=int(input())
s(n)