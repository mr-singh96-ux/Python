#updating the element of list include addition, deletion or updation of elements of lists.

#write a nornmal list in specific range
list=list(range(0,5))
print(list)


list1=[10,5,5,8,8,4,3,9,9]
print(set(list1))

#now add any number
list.append(9)
print(list)

#change value of any place number
list[3]=5
print(list)

#update value of any place number
list[3:5]=10,13
print(list)

#delete any number from the list
del list[3]
print(list)

#remave any element from the list
list.remove(13)
print(list)

#reverse of the list
list.reverse()
print(list)

#reverse of the list
days=['Sunday','Monday','Tuesday','Wednesday','Thursday']
print('\nIn Reverse Order')
i=len(days)-1
while i>=0:
    print(days[i])
    i-=1

#Combining two lists  
print(list+days)

#deleting a complete list
del list
print(list)