a=input("Enter String1:")
b=input("Enter String2:")
for i in a:
    print(i, end=",")
for j in b:
    print(j, end=",")
print()
com_char=set(a) & set(b)
print("Common characters are:",",".join(com_char))