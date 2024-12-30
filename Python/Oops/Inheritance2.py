
class person:
    def __init__(self,idCard,name):
        self.idCard=idCard
        self.name=name
        
        
    def DisplayInfo(self):
        print(f'Name: {self.name} Id Card: {self.idCard}')
        
    
#child class
class employee(person):
    def __init__(self, idCard, name,salary):
        super().__init__(idCard,name)
        self.salary=salary
        
        
obj1=person(123,'kaadhar')
obj1.DisplayInfo()


E1=employee(124,'jaidhanush',54345)
E1.DisplayInfo()
print(E1.salary)