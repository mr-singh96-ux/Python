# Displaying the elements of a list.
# num=[11,12,13,14,15]
# num=['kirat','bir','singh','avneet','kaur']
# print("Total List:", num)
# print('First=%s,Last=%s'%(num[0],num[4]))

# list1=list(range(0,10))
# print(list1)

# list2=range(5,10)
# for i in list2:
#     print(i,end=",")
# print()

# list1=[11,12,13,14,15]
# print('Using While Loop')
# i=0
# while i<len(list1):
#     print(list1[i])
#     i+=1

# print('Using For Loop')
# for i in list1:
#     print(i)

#simple operations in a list.
# list1=[11,12,13,14,15]
# list1[1]=5
# print(list1)
# list1.append(16)
# print(list1)
# list1[0:3]=1,2,3
# print(list1)
# del list1[2]
# print(list1)
# list1.remove(1)
# print(list1)
# list1.reverse()
# print(list1)
# print(list1[::-1])

#Reversing a list.
# days=['Monday','Tuesday','Wednesday']
# print(days[::-1])

#Concatination in a list.
# x=[1,2,3,4,5]
# y=[100,101]
# print(x+y)
# print(x*2)
# a=20
# print(a in x+y)

#List processing methods.
# num=[10,20,30,40,50]
# n=len(num)
# print("Number of elements:",n)

# num.append(60)
# print("After appending:",num)

# num.remove(30)
# print("After removing:",num)

# num.reverse()
# print("After Reversing:",num)

# num1=num.copy()
# print("After copying:",num1)

# num.extend(num1)
# print("After extending:",num)

# num.pop()
# print("After removing last element:",num)

# lar=num1[0]
# for i in num1:
#     if i>lar:
#         lar=i
# print(lar)
# num.sort()
# print("After sorting:",num)
# print(set(num))
# num.clear()
# print("After clearing:",num)

# finding occurence
# x=[]
# n=int(input("Enter number of elements:"))
# for i in range(n):
#     print(f"Enter element{i+1}:",end="")
#     x.append(int(input()))
# print("The list is:",x)
# y=int(input("Enter number you want to check:"))
# c=0
# for i in x:
#     if y==i:
#         c+=1
# print(f"The number of {y} is: {c}")

#Finding common elements
# a=[]
# b=[]
# n=int(input("Enter no of elements:"))
# for i in range(n):
#     print(f"Enter element{i+1}:",end="")
#     a.append(input())
# print(a)
# for j in range(n):
#     print(f"Enter element{j+1}:",end="")
#     b.append(input())
# print(b)
# com_char=set(a)&set(b)
# print(com_char)

# insert different data types in list.
# emp=[]
# n=int(input("Enter number of employees:"))
# for i in range(n):
#     print("Enter id:", end='')
#     emp.append(int(input()))
#     print("Enter Name:", end='')
#     emp.append((input()))
#     print("Enter salary:", end='')
#     emp.append(float(input()))
# print("The list is:",emp)
# a=int(input("Enter employee id want to check:"))
# for a in emp:
#     print(f"id={emp[i]}, Name={emp[i+1]}, Salary={emp[i+2]:.2f}")
#     break

#Nested list in matrices.
# mat=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print("Display original matric:",mat)
# #Display rows
# for r in mat:
#     print(r)
# #Display cols
# for r in mat:
#     for c in r:
#         print(c,end=" ")
#     print()
# #Display col1, col2 and col3
# for c in mat[0]:
#         print(c,end=" ")
# print()
# for c in mat[1]:
#         print(c,end=" ")
# print()
# for c in mat[2]:
#         print(c,end=" ")
# print()

#Square elements of alist.
# list1=[]
# for i in range(0,12):
#     list1.append(i**2)
# print(list1)
# list1=list(range(0,12))
# sq=[i**2 for i in list1]
# print(sq)

#add each element of a to each element of b
a=[10,20,30]
b=[1,2,3,4]
list1=[]
for i in a:
    for j in b:
        list1.append(i+j)
print(list1)