# array=[(1, 2, 3, 4, 5),
#         (3, 4, 5, 6, 7),
#         (1, 2, 3, 4, 5)]
# print(array)
# print(array[0])
# print(array[2])
# print(array[0][2])
# print(array[2][3])

array=[[1, 2, 3, 4, 5, 6], 
        [1, 2, 3, 4, 5, 7], 
        [1, 2, 3, 4, 5, 8], 
        [1, 2, 3, 4, 5, 9], 
        [1, 2, 3, 4, 5, 10], 
        [1, 2, 3, 4, 5, 11]]
array[3]=[3, 4, 5, 6, 7]
print(array,"\n")
array.insert(5,[2, 4, 6, 8, 10, 12])
print(array,"\n")
del array[4][3]
print(array,"\n")
array[4][3]=56
print(array)