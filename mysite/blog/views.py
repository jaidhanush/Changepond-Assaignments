from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jan(request):
    return HttpResponse('Today Is january')
def feb(request):
    return HttpResponse('Today Is Febrary')
def mar(request):
    return HttpResponse('Today Is March')
def apr(request):
    return HttpResponse('Today Is April')
def may(request):
    return HttpResponse('Today Is May')
def june(request):
    return HttpResponse('Today Is June')
def july(request):
    return HttpResponse('Today Is July')
def aug(request):
    return HttpResponse('Today Is Augest')
def sep(request):
    return HttpResponse('Today Is September')
def oct(request):
    return HttpResponse('Today Is October')
def nov(request):
    return HttpResponse('Today Is November ')
def dec(request):
    return HttpResponse('Today Is December')
