list=list(range(0,5))
print(f"The list before swapping{list}")
n=int(input("Enter the position of first element: "))
i=int(input("Enter the position of second element: "))
list[n],list[-i]=list[-i],list[n]
print(f"The list after swapping{list}")