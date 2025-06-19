tuple1=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
a=input("Check element: ")
for i in tuple1:
    if a in i:
        print(True)
        break
else:
    print(False)