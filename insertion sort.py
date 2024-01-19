def insertion(x):
    no=len(x)
    for i in range(1,no):#key value has list's first value
        k=x[i]
        j=i-1
        while j>=0 and x[j]>k:
            x[j+1]=x[j]
            j=j-1
            x[j+1]=k
n=[5,98,115,823,46,3]
insertion(n)
print("sorted elemnt:",n)