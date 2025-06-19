<<<<<<< HEAD
a=[]
n=int(input())
for i in range(n):
	e=int(input())
	a.append(e)
b=[]
even_count=0
even_sum=0
for j in a:
	if j%2==0:
		even_sum+=j
		even_count+=1
		sum=even_sum/even_count
		print(sum)
=======
# # list1=[1,2,3,4,5]
# # print(len(list1))

# lst1=[]
# n=int(input())
# for i in range(n):
#     x=int(input())
#     lst1.append(x)
# print(lst1)
# lst2=filter(lambda a: a%2==0, lst1)
# print(list(lst2))

# def is_ana(a,b):
#     if len(a)!=len(b):
#         return False
#     char_count={}
#     for char in a:
#         char_count[char]=char_count.get(char,0)+1
#     for char in b:
#         if char not in char_count or char_count[char]==0:
#             return False
#         char_count[char]-=1
#     return True
# print(is_ana("listen","silent"))

a=input()
b=input()
def an(a,b):
    return sorted(a)==sorted(b)
print(an(a,b))
>>>>>>> 0ef2b74cbe6874749af737175f980a6947059c9a
