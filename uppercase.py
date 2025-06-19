a=input("Enter a String:")
count=sum(1 for char in a if char.isupper())
print(f"Number of uppercase characters in {a} is:",count)