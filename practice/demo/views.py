from django.shortcuts import render
from .models import Dish

# Create your views here.
def index(request):
    return render(request,'demo/index.html')


def Display(request):
    value=Dish.objects.all()
    return render(request,'demo/index.html',{'values':value})