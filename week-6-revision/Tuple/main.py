# t=(1,2,3,4,5,6,7,8,9)
# print(t.count(2))
# print(t.index(3))

# #WAP to reverse a tuple
# t=(1,2,3,4,5,6)
# m=t[::-1]
# print(m)

#WAP to swap two tuple
# t=(1,2,3,4,5,6)
# m=(7,8,9,10,11,12)
# t,m=m,t
# print(t)
# print(m)

# #WAP to find duplicate in tuple
# t=(1,1,2,3,4,5,5,6,7,8,8,9,9)
# dup=set(x for x in t if t.count(x)>1)
# print("Duplicates: ", list(dup))

#WAP to add [1 4 7]
        #[2 5 8]
        #[3 6 9]

# List1=[[1,2,3],
#         [2,5,8],
#         [3,6,9]]
matrix=[]
row=int(input("Enter no. of rows"))
for i in range(row):
    row=input(f"Enter {i+1}:").split() #separated by space
    matrix.append([int(num) for num in row])
print("Matrix is:")
for row in matrix:
    print(row)
row1_index=0
row2_index=2
col1_index=0
col2_index=2
row_sum=sum(matrix[row1_index])+sum(matrix[row2_index])
col_sum=sum(matrix[col1_index])+sum(matrix[col2_index])
T_sum=row_sum+col_sum
print(T_sum)
