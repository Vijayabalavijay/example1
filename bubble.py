def bubble(x):
    c=len(x)
    for i in range(c):
        for j in range(0,c-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
n=[1,3,2,7,5,4,89,3,23,87]
bubble(n)    
print("sorted element:",n)