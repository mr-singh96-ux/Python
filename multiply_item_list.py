num=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    num1=int(input(f"Enter elements{i+1}: "))
    num.append(num1)

p=1
for a in num:
    p*=a

print("The product is: ", p)

# num=[]
# pr=[]
# n=int(input("Enter number of elements: "))
# for i in range(n):
#     num1=int(input(f"Enter elements{i+1}: "))
#     num.append(num1)

# p=1
# for a in num:
#     p*=a

# pr.append(p)
# print("The product is: ",p)
# print(pr)