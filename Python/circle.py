# class circle:
    
#     PI=3.14
    
#     def __init__(self):
#         self.radius=0   #Instance Variable
        
#     def AcceptMethod(self):  #Instance Method
#         self.radius=int(input('Enter the radius'))
        
        
#     def Area_Of_circle(self):
#        res= circle.PI*self.radius*self.radius
#        print(res)
       
       
# def main():
#     ans=circle()
#     ans.AcceptMethod()
#     ans.Area_Of_circle()
    
# if __name__=="__main__":
#     main()
    
    
# =============================================================================


class lists:
    def __init__(self):
        self.list=[]
        self.max=0
        self.min=0
        self.addition=0
    
    def accept_method(self):
        self.list=[]
        number=int(input('enter the list size:'))
        
        for i in range(number):
            num=int(input())
            self.list.append(num)
        
        print(self.list)
        
    def maximum(self):
        self.max=0
        for i in self.list:
            if i>self.max:
                self.max=i
        print('Maximum num: ',self.max)
        
    def minimum(self):
        self.min=self.list[0]
        for i in self.list:
            if i<self.min:
                self.min=i
        print('Minimum num: ',self.min)
    
    def add(self):
        self.addition=0
        for i in self.list:
            self.addition+=i
        print('Addition Value: ',self.addition)
        
def main():
    result=lists()
    result.accept_method() 
    result.maximum()
    result.minimum()
    result.add()

main()
    
if __name__=='__main__':
    main()