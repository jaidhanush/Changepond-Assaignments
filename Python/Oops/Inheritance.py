
class person:
    def __init__(self,idCard,name):
        self.idCard=idCard
        self.name=name
        
        
    def DisplayInfo(self):
        print(f'Name: {self.name} Id Card: {self.idCard}')
        
   #Chils cls     
class employee(person):
    def show(self):
        print('inside show')
        
obj1=employee(123,'jaiDhanush')
obj1.DisplayInfo()
obj1.show()