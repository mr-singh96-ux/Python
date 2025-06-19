num1=[1, 2, 3, 4, 5]
def dnum(i):
        return i*2
num=map(dnum, num1)
print("Original List:", list(num1))
print("New List:", list(num))
