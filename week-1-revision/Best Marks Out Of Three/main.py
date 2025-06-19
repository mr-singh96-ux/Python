# str1=int(input("Enter number1:"))
# str2=int(input("Enter number2:"))
# str3=int(input("Enter number3:"))

# if str1<str2 and str1<str3:
#     print("The average of best marks is:",(str2+str3)/2)
# if str2<str1 and str2<str3:
#     print("The average of best marks is:",(str1+str3)/2)
# if str3<str2 and str3<str1:
#     print("The average of best marks is:",(str2+str1)/2) 

def b(str1,str2,str3):
    if str1<str2 and str1<str3:
        print("The average of best marks is:",(str2+str3)/2)
    if str2<str1 and str2<str3:
        print("The average of best marks is:",(str1+str3)/2)
    if str3<str2 and str3<str1:
        print("The average of best marks is:",(str2+str1)/2)
a1=int(input())
a2=int(input())
a3=int(input())
b(a1,a2,a3)
