""""n=int(input("enter the value:"))
if n%2==0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")  """  """"
print("voting calculation")
n=int(input("enter your age:"))
if n>=18:
    print("eligible for vote")    
else:
    print("you are not eligible for vote")"""
print("if elif else documentation")
n=int(input("enter the days"))
if n==0:
    print("no fine")
elif n >= 1 and n <= 5:
    print("0.5 rupees fine",n*0.5)
elif n > 5 and n <= 10:
    print("1.0 rupees fine",n*1)
elif n > 10 and n <= 30:
    print("5 rupees fine",n*5)
else:
    print("membership cancel")
print(id(n))          

         