a=input("Enter String:")
vow="aeiou"
count_vow=0
for i in a:
    if i in vow:
        count_vow += 1
print("There are:",count_vow,"vowels.")