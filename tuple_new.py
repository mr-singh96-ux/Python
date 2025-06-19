#basic operations on tuple
# tuple1=(1,2,3,4,5)
# print(max(tuple1))
# print(min(tuple1))
# name=1
# print(name in tuple1)
# tpl=tuple1*3
# print(tpl)

#input to tuple
# a=[]
# sum=0
# for i in range(0,6):
#     print("Enter elements:", end="")
#     a.append(int(input()))
# n=len(a)
# print(tuple(a))
# for i in range(n):
#     sum+=a[i]
# print(sum)
# print(sum/n)

#occurence of element in tuple.
# a=input("Enter elemenmts separated by commas: ").split(',')
# a=[int(i) for i in a]
# print(tuple(a))

# b=int(input("Enter element to check: "))
# if b in a:
#     print(True)
#     print(a.index(b))
# else:
#     print(False)

#Nested Tuple
# emp=((1,'Kirat',2500),(2,"Inder",2900),(3,"Puri",2400))
# print(sorted(emp))
# print(sorted(emp,reverse=True))
# print(sorted(emp, key=lambda x:x[1]))
# print(sorted(emp, key=lambda x:x[2]))

#inserting in tuple
# tuple1=(1,'kirat',2,4,5,'inder')
# print(tuple1)
# name=input('Enter element to insert:')
# pos=int(input('Enter position:'))
# list1=list(tuple1)
# list1.insert(pos,name)
# tuple1=tuple(list1)
# print(tuple1)

#modifying an element in a tuple.
# tuple1=(10,20,30,40,50)
# print(tuple1)
# list1=list(tuple1)
# print(list1)
# n=int(input())
# i=int(input("Position:"))
# list1[i]=n
# tuple1=tuple(list1)
# print(tuple1)

#delete an element from tuple
tuple1=(10,20,30,40,50)
print(tuple1)
list1=list(tuple1)
n=int(input("Position:"))
# del list1[n]
list1.pop(n)
tuple1=tuple(list1)
print(tuple1)