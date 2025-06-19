# Display the string as tuple. But the output string must be reversed in the form of tuple.
str1=input("Enter the string: ")
list1=[]
for i in str1:
    list1.append(i)
print(tuple(list1[::-1]))