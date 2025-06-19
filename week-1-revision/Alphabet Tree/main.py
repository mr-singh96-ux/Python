a="CALIFORNIA"
for i in range(1,11,1):
    for j in range(i):
        print(a[j], end='')
    print()
a="CALIFORNIA"
for i in range(10,0,-1):
    for j in range(i-1):
        print(a[j], end='')
    print()