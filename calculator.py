import math
n1=int(input("enter the no:"))
n2=int(input("enter the no:"))
choice=int(input(("enter your choice:")))
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")
print("5.square")
print("6.square root")
print("7.cube")
print("8.cube root:")
print("9.any power above square and cube:")
print("10.any root above of square and cube:")
print("11.sin value of given number:")
print("12.cos value of given number:")
print("********************")
if choice==1:
    print("addition:")
    s=n1+n2
    print("sum",s)
elif choice==2:
    print("subraction:")
    d=n1-n2
    print("difference",d)
elif choice==3:
    print("multiplication:")
    m=n1*n2
    print("multiplication",m)
elif choice==4:
    if n2==0:
        print("syntax error")
        print("denominator is non zero only")
    else:
        div=n1/n2
        print("division",div)
elif choice==5:
    print("square")
    s=n1**2
    print("square of given number:",s)
elif choice==6:
    print("square root:")
    sr=math.sqrt(n1)
    print("square root of given no:",sr)
elif choice==7:
    print("cube:")
    c=n1**3
    print("cube of given number:",c)
elif choice==8:
    print("cube root:")
    cr=n1**(1/3) 
    print("cube root of given number",cr) 
elif choice==9:
    print("any power:")
    ap=n1**n2
    print("any power of given details:",ap)
elif choice==10:
    print("any root:")
    ar=n1**(1/n2)
    print("any root above square and cube:",ar) 
elif choice==11:
    print("sin value of given number:")
    si=math.sin(n1)
    print("sin value of given number:",si)  
elif choice==12:
    print("cos value of given number:")
    co=math.cos(n1)
    print("cos value of given number:",co)                               
else:
    print("exit")
                           
    


    