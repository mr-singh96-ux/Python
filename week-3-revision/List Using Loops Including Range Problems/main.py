#range in list is used to show or type a sequence of intergers by giving them initial as well as endind point.
#It can be written as range(start,stop,size).
#Size is used to get interval that after how many integers we leave and get other output.

#List with consecutive integer values
# list=range(10)
# for i in list:
#     print(i,',',end="")
# print()

# list1=range(4,10,1)
# for i in list1:
#     print(i,',',end="")
# print()

# #list with odd integer values.
# list2=range(5,10,2)
# for i in list2:
#     print(i,',',end="")
# print()


#display list elements using while and for loop
#while loop
print("Using While Loop")
list=[10,20,30,40,50]
i=0
while i<len(list):
    print(list[i])
    i=i+1
    
#Using for Loop
print("Using for loop")
for i in list:
    print(i)