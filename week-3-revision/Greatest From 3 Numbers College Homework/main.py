# Reena and Teena are twin sisters. They got admission in BTech. Computer science and Engineering in 
# Chitkara University. Their teacher taught then about the coding concepts and gave them an assignment
# to write a program to find the greatest among three numbers. Help both sisters to find the greatest 
# among three numbers.

def g():
    a=int(input("Enter Any Number:"))
    b=int(input("Enter Any Number:"))
    c=int(input("Enter Any Number:"))
    if b<a>c:
        print(f"a is greater i.e. a={a}")
    elif a<b>c:
        print(f"b is greater i.e. b={b}")
    else:
        print(f"c is greater i.e. c={c}")
g()