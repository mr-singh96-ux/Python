a=input("Enter a String:")
count=sum(1 for char in a if char.islower())
print(f"Number of lowercase characters in {a} is:",count)

count=sum(1 for char in a if char.isupper())
print(f"Number of uppercase characters in {a} is:",count)

count=sum(1 for char in a if char.isdigit())
print(f"Number of digits in {a} is:",count)

count=sum(1 for char in a if char.isspace())
print(f"Number of whitespace in {a} is:",count)