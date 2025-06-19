a=input("Enter a String:")
count=sum(1 for char in a if char.isdigit())
print(f"Number of digits in {a} is:",count)