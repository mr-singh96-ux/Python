# dict={
#     "brand":"ford",
#     "model":"Mustang",
#     "year":1964,
#     "color":["red", "yellow", "green"]
# }
# print(dict)

# dict["color"].remove("red")
# print(dict)

# del dict["color"]
# print(dict)

# dict.pop("model")
# print(dict)

# dict["age"]="60"
# print(dict)

# dict["age"]="68"
# print(dict)

# dict["price"]=dict.pop("age")
# dict["price"]="2500000"
# print(dict)

# dict["age"]="60"
# dict.pop("price")
# print(dict)

# Dictionary methods
# emp={'name':'Kirat Bir Singh','ID':'13','Salary':"250000"}
# print(emp['name'])
# print(emp['ID'])
# print(emp['Salary'])

# sum in dictionary
# n_dict={}
# n=int(input("Enter number of elements in dict:"))
# for _ in range(n):
#     key=input("enter keys:")
#     d_value=int(input("Enter value:"))
#     n_dict[key]=(d_value)
# print(n_dict)
# n_sum=sum(n_dict.values())
# print(n_sum)

#creating a new dictionary.
# n_dict={}
# n=int(input("Enter number of elements:"))
# for _ in range(n):
#      key=input()
#      k_value=int(input())
#      n_dict.update({key:k_value})
# print(n_dict)

# display player name of a dictionary
# player={}
# n=int(input("Enter number of elements:"))
# for i in range(n):
#     key=input()
#     runs=int(input())
#     player[key]=(runs)
# print(player)
# print("Players in match are:")
# for pname in player.keys():
#     print(end='')
#     print(pname)
# p=input()
# if p in player:
#     print(f"{p} has scored {player[p]} runs.")
# else:
#     print("Player not found.")

#dictionary using loop
# dict1={'a':"Red",'b':"Green",'c':"Yellow"}
# for k,v in dict1.items():
#     print(f"key={k}, value={v}")

#number of occurence using dict
# str1=input()
# dict1={}
# for x in str1:
#     dict1[x]=dict1.get(x,0)+1
# for k,v in dict1.items():
#     print(f"{k} occures {v} times")

# converting list into dictionary
# con=['Khalistan','India','Pakistan','China','Afghanistan']
# cit=['Amritrsar','New Delhi','Lahore','Tibet','Kabul']
# z=zip(con, cit)
# print(dict(z))