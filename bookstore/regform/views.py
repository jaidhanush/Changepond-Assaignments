from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReviewForm

# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse('thank-you')
    
    else:
        form=ReviewForm()
    return render (request,'regform/regform.html',{
        'form':form
    })
    
    