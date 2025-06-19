i_string=input("Enter any string: ")
vow=[chr for chr in i_string if chr.lower() in 'aeiou']
print("Vowels are:",'',set(vow))

# i_string=input("Enter any string: ")
# vow=[chr for chr in i_string if chr=='a' if chr=='e' if chr=='i' if chr=='o' if chr=='u']
# print("Vowels are:",'',vow)