#In some foreign university, the central library has charged a fine for every book returned late after the due
#date mentioned on the book. For first 5 days after due date the fine is 50 paise per day, if days are in
#between 6-10 days then the fine is one rupee per day and if days are in between 11-30 days then the fine is 5
#rupees per day. If you return the book after 30 days your membership will be cancelled. Write a program to 
#accept the number of days the member is late to return the book and display the fine or the appropriate message.
st_name=input("Enter Name of The Student: ")
due_date=int(input("Enter the Due Date: "))
ret_book=int(input("Rturning on: "))
charge=(ret_book-due_date)
if ret_book<=due_date:
    print("No fine will be charged.")
elif ret_book in range(0,6):
    charges=charge*0.5
    print(f"The charges for late submission is {charges} paise.")
elif ret_book in range(6,11):
    charges=charge*1
    print(f"The charges for late submission is {charges} rupees.")
elif ret_book in range(11,31):
    charges=charge*5
    print(f"The charges for late submission is {charges} rupees.")
else:
    print("Your membership has been cancelled.")