from django.db import models

# Create your models here.
class Chief(models.Model):
    full_name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'Name:{self.full_name} age:{self.age} Address:{self.address}'
    
class Dish(models.Model):
    name=models.CharField(max_length=20)
    rating=models.IntegerField()
    price=models.IntegerField()
    is_bestselling=models.BooleanField()
    Chief=models.ForeignKey("Chief",on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f'DishName:{self.name} Rating:{self.rating} Price:{self.price}'
    
    

   