# import functools

# num=[1, 2, 3, 4, 5, 6]
# result=functools.reduce(lambda x,y:x+y, num)
# print(result)

import functools

num=int(input())
li = []
for i in range(0,num):
    inp = int(input())
    li.append(inp)
print(li)
#result=functools.reduce(lambda x,y:x+y, num)
#print(result)