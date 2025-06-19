g = input("Enter your gender: ").lower()
y = int(input("Enter year of service: "))
q = int(input("Enter your qualification (1 for Post-Graduate, 0 for Graduate): "))

salary_cal = lambda g, y, q: (
    15000 if g=='m' and y >= 10 and q==1 else
    10000 if g=='m' and y >= 10 and q==0 else
    10000 if g=='m' and y < 10 and q==1 else
    7000 if g=='m' and y < 10 and q==0 else
    12000 if g=='f' and y >= 10 and q==1 else
    9000 if g=='f' and y >= 10 and q==0 else
    10000 if g=='f' and y < 10 and q==1 else
    6000 if g=='f' and y < 10 and q==0 else
    "not valid"
)

salary=salary_cal(g, y, q)
print("Salary is:", salary)
