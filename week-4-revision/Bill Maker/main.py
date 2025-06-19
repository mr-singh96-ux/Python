a=int(input("Enter Units:"))
sum=0
if a<101:
    sum=a*0
    print("According To Policy By Panjab Government First 100units are Free.")
    print(f"The Total Bill is: Rs{sum}/-")
elif a<201:
    sum=(a-100)*2.5+100*1
    print(f"The Total Bill is: Rs{sum}/-")
elif a<301:
    sum=(a-200)*4+100*1+100*2.5
    print(f"The Total Bill is: Rs{sum}/-")
elif a>301:
    sum=(a-300)*6+100*1+100*2.5+100*4
    print(f"The Total Bill is: Rs{sum}/-")