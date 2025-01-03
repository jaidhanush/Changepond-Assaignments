from django.shortcuts import render
from .models import UserProfile
from .forms import Profileform
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

class ProfileCreateView(CreateView):
    model=UserProfile
    template_name="imageapp/imgprofile.html"
    fields="__all__"
    success_url="/image"

class ProfileViewList(ListView):
    model=UserProfile
    context_object_name='profiles'
    template_name="imageapp/"
   
