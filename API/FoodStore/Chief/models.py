from django.db import models

# Create your models here.
class chief(models.Model):
    fullname=models.CharField(max_length=20)
    age=models.IntegerField()