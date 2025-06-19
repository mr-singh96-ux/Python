n=int(input("Enter Size:"))
print(f"The Even Numbers Between 1 and {n+1} are:")
for i in range(1,n+1):
    if i%2==0:
        print(i)