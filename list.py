a=['apple','ornge','mango']
print(a)
print(type(a))
print(a[2])
a[1]='kiwi'
print(a)
for x in a:
    print(x)
if 'apple' in a:
    print('true')
else:
    print("false")
print(len(a))        
a.append("banana")
print(a)
a.insert(1,"kiwi")
print(a)