# x=[]
# sum=0
# n=int(input())
# for i in range(n):
#     a=int(input())
#     x.append(a)
# print(tuple(x))
# for i in range(n):
#     sum+=x[i]
# print(sum)
# avg=sum/n
# print(avg)

# x=[]
# n=int(input())
# for i in range(n):
#     a=int(input())
#     x.append(a)
# print(tuple(x))
# y=int(input())
# c=0
# for i in x:
#     if y==i:
#         c+=1
# print(c)

# tuple1=(1,2,3,4)
# list1=list(tuple1)
# print(list1)
# i=int(input())
# n=int(input())
# list1.insert(i,n)
# print(tuple(list1))

# tuple1=(1,2,3,4)
# list1=list(tuple1)
# print(list1)
# i=int(input())
# n=int(input())
# list1[i]=n
# print(tuple(list1))

tuple1=(10,20,30,40,50)
list1=list(tuple1)
print(list1)
i=int(input())
del list1[i]
print(tuple(list1))