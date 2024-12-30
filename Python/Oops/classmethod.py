class student:
    graduation='be'
    
    def graduation_in(cls):
        print('graduation',cls.graduation)
        
student.grad = classmethod(student.graduation_in)
student.grad()
print()
class student:
    graduation='be'
    @classmethod
    def graduation_in(cls):
        print('graduation',cls.graduation)
        

student.graduation_in()