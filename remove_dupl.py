test_dict={'Manjeet':[1], 'Akash':[1,8,9]}
# Combine all values from the dictionary into a single list
all_val=[]
for a in test_dict.values():
    all_val.extend(a)
# Find common values by checking if the value appears more than once in the list
com_val=set(b for b in all_val if all_val.count(b)>1)
# Remove common values from each list in the dictionary
for c in test_dict:
    test_dict[c]=[d for d in test_dict[c] if d not in com_val]
# Print the result
print(test_dict)