class user:
    def __init__(self,name):
        print("call me constructor")
        self.name=name
    def pt(self):
        print("name",self.name)
c=user("vijay")
c.pt() 
print(c.__dict__)       
c1=user("vijaya bala")
c1.pt()      
print(c1.__dict__)
print(user.__dict__)