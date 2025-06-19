def calculate_pizza_cost():
    base=100
    s_value=10
    m_value=15
    l_value=20
    i=0
    T=20
    print("Small=+10 Medium=+15 Large=+20")
    a=input("Choose Your Size in for of Small=S, Medium=M and Large=L: ")
    b=int(input("Choose Number toppings:"))
    if a=="S":
        i=base+s_value
        print(f"Small={i}")
    elif a=="M":
        i=base+m_value
        print(f"Medium={i}")
    elif a=="L":
        i=base+l_value
        print(f"Large={i}")
    result=i+T*b
    print(f"Total cost of pizza including {b} toppings {i}+{T*b} is:{result}")
    print("Thank You for Ordering From PizzaHut!")
calculate_pizza_cost()


# def calculate_pizza_cost(size,toppings):
#     base_prices={"Small":10, "Medium":15, "Large":20}
#     topping_cost=2
#     total_cost=base_prices[size]+(toppings*topping_cost)
#     return total_cost
# size=input("Enter Size: ")
# toppings=int(input("Enter number of toppings: "))
# total_cost=calculate_pizza_cost(size,toppings)

# print(size)
# print(toppings)
# print(f"{total_cost}")
# print("Thank You for odering fropm PizzaHut!")