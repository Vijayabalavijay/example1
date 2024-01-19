def merge_sort(x):
    if len(x)<=1:
        return x
    m=len(x)//2
    left=x[:m]
    right=x[m:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)
def merge(l,r):
    rs=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            rs.append(l[i])
            i+=1
        else:
            rs.append(r[j])
            j+=1
    rs.extend(l[i:])
    rs.extend(r[j:])
    return rs
n=[24,67,5,9,12,45,89]
x=merge_sort(n)
print("sorted element:",x)