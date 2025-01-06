from django.db import models
from Chief.models import chief 

class dish(models.Model):
    dishname= models.CharField(max_length=50)
    rating = models.IntegerField()

    chief= models.ForeignKey(chief, on_delete=models.CASCADE)
    
def __str__(self):
    return self.dishname
