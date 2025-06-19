# my_list1=[1,2,3,4,5]
# my_list2=[6,7,8,9,10]

# def add(x,y):
#     return x+y

# my_list3=map(add,my_list1,my_list2)
# print(list(my_list3))

my_t=(1,2,3,4,5)
my_t1=(6,7,8,9,10)

def multiply(x,y):
    return x*y

result=map(multiply, my_t, my_t1)
print(set(result))