# You are working at a bank, and your team is tasked with developing a simple interest calculator for customers. 
# The bank offers two types of accounts: savings accounts and fixed deposit accounts. 
# Each type of account has a different interest rate, and customers need a program that 
# will calculate their interest based on their account type and the amount they have deposited.
# Input Format:
# An integer representing the principal amount.
# A string indicating the account type:
# o "savings": The interest rate is 4% per year.
# o "fixed_deposit": The interest rate is 6% per year.
# Output Format:
# The total interest amount earned after one year, rounded to 2 decimal places.
# The formula for calculating interest after one year for different account types:
# Savings Account (4% interest rate):
# Interest=Principal Amount×0.04
# Where 0.04 represents the 4% annual interest rate for savings accounts.
# Fixed Deposit Account (6% interest rate):
# Interest=Principal Amount×0.06
# Where 0.06 represents the 6% annual interest rate for fixed deposit accounts.
# a=input("Enter Account Type:")
# if a=="Savings":
#     def s():
#         p_value=int(input("Enter Principal Amount: "))
#         i_rate=0.04
#         interest=p_value*i_rate
#         print(f"The total amount after getting one year interest is:{interest:.2f}")

#     s()
# elif a=="FD":
#     def f():
#         p_value=int(input("Enter Principal Amount: "))
#         i_rate=0.06
#         interest=p_value*i_rate
#         print(f"The total amount after getting one year interest is:{interest:.2f}")
        
#     f()
# else:
#     print("Invalid Account Type")

# def b_int():
#     p_value=int(input("Enter Amount: "))
#     if a=="Savings":
#         rate=0.04
#     elif a=="FD":
#         rate=0.06
#     else:
#         print("Invaild account Type")
#         return
    
#     interest=p_value*rate
#     print(f"The total amount get after addition of interest:{rate} is {interest:.2f}")
# a=input("Enter Account Type: ")
# b_int()


# a=input("Enter Gender: ")
# if a=="M":
#     def s():
#         i_rate=int(input("Enter Increment: "))
#         p_value=int(input("Enter Gross Salary: "))
#         interest=(p_value*i_rate)/100
#         c=p_value+interest
#         print(f"The total salary after incriment is:{c:.2f}")

#     s()
# elif a=="F":
#     def f():
#         i_rate=int(input("Enter Increment: "))
#         p_value=int(input("Enter Gross Salary: "))
#         interest=(p_value*i_rate)/100
#         c=p_value+interest
#         print(f"The total salary after incriment is:{c:.2f}")
        
#     f()
# else:
#     print("Invalid Account Type")

a=float(input("Enter Time Taken: "))
if a<=3:
    def h():
        print("Workers are highly efficient.")
    h()
    
elif a>3 and a<=4:
    def i():
        print("Workers need to improve speed.")
    i()
    
elif a>4 and a<=5:
    def t():
        print("Workers required training.")
    t()

else:
    print("Invalid Data Input")