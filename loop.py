i=1
n=13

while (i<=10):
    print(n,'*',i,'=',n*i)
    i=i+1
l1=[1,2,3,4,5,6,7]
x=0
while x < len(l1):
    l1[x]=l1[x]+100
    x=x+1
print(l1)     
print("for loop")
l1=[1,2,3,4,5,6,7]
for i in l1:
    print(i)
l1=[1,2,3,4,5,6,7]
l2=["python",'c','c++','java','html','ai','ml']
for i in l1:
    for j in l2:
        print(i,j)        