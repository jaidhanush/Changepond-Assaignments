#creating Class

class student:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        
    def Display(self): #instance Method
        print(f'{ self.firstname} { self.lastname}')
        
        
obj1=student('jai','dhanush')
print(obj1.firstname)
print(obj1.Display)
