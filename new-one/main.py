# num=[10,20,30,40,50]
# print(num[1],num[2])

# list1=list(range(0,9))
# print(list1)

# num=[10,20,30,40,50]
# for i in num:
#     print(i, end=" ")

# num=[10,20,30,40,50]
# num.append(24)
# print(num)
# num.remove(20)
# print(num)
# del num[2]
# print(num)
# print(num[::-1])

# num=[10,20,30,40,50]
# for i in num[::-1]:
#     print(i)

# list1=[1,2,3,4,5,6]
# list2=[7,8,9,10,11,12]
# print(list1+list2)

# x=[]
# n=int(input("Enter number of elements:"))
# for i in range(n):
#     a=int(input())
#     x.append(a)
# print(x)
# big=x[0]
# small=x[0]
# for i in range(1,n):
#     if x[i]>big:
#         big=x[i]
#     if x[i]<small:
#         small=x[i]
# print(big)
# print(small)

# x=[]
# n=int(input())
# for i in range(n):
#     a=int(input())
#     x.append(a)
# print(x)
# sortt=[]
# while x:
#     small=x[0]
#     for num in x:
#         if num<small:
#             small=num
#     sortt.append(small)
#     x.remove(small)
# print(sortt)

# x=[]
# n=int(input())
# for i in range(n):
#     a=int(input())
#     x.append(a)
# print(x)
# bsort=[]
# while x:
#     big=x[0]
#     for num in x:
#         if num>big:
#             big = num
#     bsort.append(big)
#     x.remove(big)
# print(bsort)

# x=[]
# n=int(input())
# for i in range(n):
#     a=int(input())
#     x.append(a)
# print(x)
# c=0
# y=int(input())
# for i in x:
#     if y==i:
#         c+=1
# print(c)

# x=[]
# n=int(input())
# for i in range(n):
#     a=input()
#     x.append(a)
# y=[]
# for j in range(n):
#     b=input()
#     y.append(b)
# print(x)
# print(y)
# s1=set(x)
# s2=set(y)
# s3=s1.intersection(s2)
# print(list(s3))

# mat=[[1,2,3], [4,5,6], [7,8,9]]
# print(mat)
# for r in mat:
#     print(r)
# for c in mat[0]:
#     print(c,end=" ")
# print()
# for c in mat[1]:
#     print(c,end=" ")
# print()
# for c in mat[2]:
#     print(c,end=" ")
# print()
# for r in mat:
#     for c in r:
#         print(c,end=" ")
#     print()
# result=sum(mat[0])+sum(mat[2])+sum(mat[i][0] for i in range(len(mat)))+sum(mat[i][-1] for i in range(len(mat)))
# print(result)
# for i in range(len(mat)):
#     list1=[(mat[i][0])]
#     print(list1)