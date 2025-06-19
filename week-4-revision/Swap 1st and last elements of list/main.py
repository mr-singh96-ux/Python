list=list(range(0,5))
print(f"The list before swapping{list}")
list[0],list[-1]=list[-1],list[0]
print(f"The list after swapping{list}")