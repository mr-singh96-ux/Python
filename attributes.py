class Car:
    def __init__(kirat, make, model, year):
        kirat.make = make
        kirat.model = model
        kirat.year = year
my_car = Car('Toyota', 'Corolla', 2020)

print(my_car.make)
print(my_car.model)
print(my_car.year)
