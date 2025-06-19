list1=[6,7,8,9,10]
list2=[1,2,3,4,5]
result1=set(list1)-set(list2)
result2=set(list2)-set(list1)
print("Elements in list1 but not in list2:",list(result1))
print("Elements in list2 but not in list1:",list(result2))