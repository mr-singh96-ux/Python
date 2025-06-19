list1=[1, 2, 3, 4, 5]
list2=[6, 7, 8, 9, 10]
def add(x, y):
    return x+y
n=map(add, list1 ,list2)
print("Original List 1:", list(list1))
print("Original List 2:", list(list2))
print("Added List:",list(n))
