def selection(x):
    no=len(x)
    for i in range(no-1):
        m=i
        for j in range(i+1,no):
            if x[m]>x[j]:
                m=j
        x[i],x[m]=x[m],x[i]
n=[67,34,2,6,7,5]
selection(n)
print("sorted element:",n)    