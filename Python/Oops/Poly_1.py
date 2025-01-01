# Example: Polymorphism and inheritance (overriding)

class Transport:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def Display(self):
        print(f'{self.brand} and {self.model}')
        
class Car(Transport):
    Transport.brand=brand
    Transport.model=model
    
class Boat(Transport):
    pass
    

class Bike(Transport):
    pass