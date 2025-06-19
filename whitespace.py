a=input("Enter a String:")
count=sum(1 for char in a if char.isspace())
print(f"Number of whitespace in {a} is:",count)