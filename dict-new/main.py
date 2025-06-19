# dict1={'name':'Kiratbir Singh',
#         'id':'13',
#         'Salary':'1Cr'
# }
# print("Name of emp:",dict1['name'])

# dict1={}
# n=int(input())
# for _ in range(n):
#     k=input()
#     k_value=int(input())
#     dict1[k]=k_value
# print(dict1)
# sum1=sum(dict1.values())
# print(sum1)

# player={}
# n=int(input())
# for _ in range(n):
#     pname=input()
#     runs=int(input())
#     player[pname]=(runs)
# print(player)
# name=input()
# print(player.get(name,"Player not found."))

# colors={'r':'Red','b':'Blue','y':'Yellow'}
# for k in colors:
#     print(k)
# for v in colors:
#     print(colors[v])
# for k,v in colors.items():
#     print(k,v)
# colors['o']="Orange"
# colors.pop('r')
# print(colors)

# str1=input()
# dict1={}
# for x in str1:
#     dict1[x]=dict1.get(x,0)+1
# print(dict1)
# for k,v in dict1.items():
#     print(k,v)

# p={}
# n=int(input())
# for _ in range(n):
#     k=int(input())
#     v=input()
#     p[k]=v
# print(p)
# c1=sorted(p.items(), key=lambda t:t[0])
# print(c1)
# c2=sorted(p.items(), key=lambda t:t[1])
# print(c2)

# list1=[]
# list2=[]
# n=int(input())
# for i in range(n):
#     a=input()
#     list1.append(a)
# for i in range(n):
#     b=input()
#     list2.append(b)
# z=zip(list1,list2)
# d=dict(z)
# print(d)