#WAP to add numbers using lambda.
result=(lambda x,y: x+y)
print(result(3,5))

#WAP to square a list using map and lambda.
x=[1,2,3,4,5]
result=map(lambda a: a**2, x)
print(list(result))

#WAP to filter even numbers from a list.
x=[1,2,3,4,5,6]
result=filter(lambda a: a%2==0, x)
print(tuple(result))

#WAP to sort element list.
dict=[(1,"Apple"), (2,"Cherry"), (3,"Banana"), (4,"Angoori")]
sorted_data=sorted(dict, key=lambda x: x[1])
print(tuple(sorted_data))

#WAP to multiply all elements in a list.
from functools import reduce
x=[1,2,3,4,5,6]
result=reduce(lambda a,y: a*y, x)
print(result)