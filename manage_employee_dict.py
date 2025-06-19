# Manage the employees' database. The salary is credited in the form of rupees. 
# Write Python code to manage the data efficiently in the dictionary w.r.t empname and empsal by converting the 
# salary to dollars. Output must be in the form of a dictionary.
emp_dict={}
key=int(input("Enter number of Keys:"))
for i in range(key):
    empname=input("Enter name of Employee:")
    empsal=float(input("Enter salary of Employee:"))
    emp_dict[empname]=(empsal)
print(emp_dict)
for empname in emp_dict:
    emp_dict[empname]/=84.070
print(emp_dict)