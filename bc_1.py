name='vijay'
age=20
cgpa=7.93
student=True
print(type(name))
print(type(age))
print(type(cgpa))
print(type(student))
age=float(age)
cgpa=int(cgpa)
student=str(student)
print(type(age))
print(type(cgpa))
print(type(student))
#age=bool(age)
#print(age)
print(f'my name is {name} and my age is {age} and college cgpa is {cgpa} and belive me a single -{student}')

#implicit
x=2
y=2.0
print(x/y)