from django.contrib import admin
from .models import Book,Author

# Register your models here.
class Bookadmin(admin.ModelAdmin):
    list_display=('title','rating')
    list_filter=('rating',)
    
admin.site.register(Book,Bookadmin)
admin.site.register(Author)