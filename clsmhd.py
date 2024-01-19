class student:
    name="vijaya bala"
    age=20
    def _printall():
        print("name:",student.name)
        print("age:",student.age)
student._printall()
print(student.__dict__)
print(getattr(student,"_printall")) 
getattr(student,"_printall")()
print(student.__dict__['_printall']())       
        