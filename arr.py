bike=['duke','honda','yamaha']
print(bike)
no=[0,1,2,3,4,5,6,7,8,9]
print(type(bike))
print(tuple(bike))
for i in bike:
    print(i)
y=bike.count("duke")
print(y)
a=no.index(8)
print(a)
bike.insert(1,tvs)
print(bike)
no.extend(bike)
print(no)
print(bike[2])
print(len(bike))
bike.append("xl")
bike.pop(2)
x=bike.copy()
print(x)
print(bike)



