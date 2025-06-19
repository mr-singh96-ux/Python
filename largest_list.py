list1=input("Enter list element separated by space: ").split()
print("Your List is:",list1)
lar=list1[0]
for i in list1:
    if i>lar:
        lar=i
print(lar)