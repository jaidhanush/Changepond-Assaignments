from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Book


# Create your views here.

def index(request):
    book=Book.objects.all()
    return render(request,'author/index.html',{
        'book_collection':book
    })

def bookdetails(request,id):
    books=get_object_or_404(Book,pk=id)
    context={'book_title':books.title,'book_rating':books.rating}
    
    return render(request,'author/details.html',context=context)
    # try:
    #     book=Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    