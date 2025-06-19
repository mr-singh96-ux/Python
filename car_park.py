# Write a python program to calculate the parking charges of a vehicle. Enter the type of vehicle as a 
# character (like c for car, b for bus, etc.) and read the hours and minutes when the vehicle enters the 
# parking lot. When the vehicle is leaving, it enters its leaving time. Calculate the difference between
# the two timings to calculate the number of hours and minutes for which the vehicle was parked. Calculate 
# the charges based on the following rules and display the result on the screen, otherwise If the vehicle 
# type entered by the user is not one of the expected options (c for car, b for bus and s for
# scooter/motor cycle),then the program output  will be Invalid vehicle choice.
a=input("Enter Vehicle type: ")
time=int(input("Enter Time: "))
a_char=0
if a=='c':
    if time<3:
        a_char=10
    elif time>3:
        a_char=20
    print(a_char)
elif a=='b' or a=='t':
    if time<3:
        a_char=20
    elif time>3:
        a_char=30
    print(a_char)
else:
    if time<3:
        a_char=5
    elif time>3:
        a_char=10
    print(a_char)