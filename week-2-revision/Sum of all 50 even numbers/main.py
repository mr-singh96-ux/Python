sum_total=0
i=1
for i in range(1,101):
    if i%2==0:
        print("The Given numbers are even",i)
        sum_total+=i
print("Sum of all even numbers upto 100: ",sum_total)