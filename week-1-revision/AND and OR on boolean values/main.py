def bool_input(input_str: str) -> bool:
    return input_str.strip().lower() == 'true'

    
a = bool_input(input("Enter the first boolean value (True or False): "))
b = bool_input(input("Enter the second boolean value (True or False): "))
print(f"a={a}")
print(f"b={b}")
print(f"a & b = {a & b}")
print(f"a | b = {a | b}")

