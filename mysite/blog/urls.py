from django.urls import path
from .import views

months={'1':views.jan,
        '2':views.feb,
        '3':views.mar,
        '4':views.apr,
        '5':views.may,
        '6':views.june,
        '7':views.july,
        '8':views.aug,
        '9':views.sep,
        '10':views.oct,
        '11':views.nov,
        '12':views.dec
        }

urlpatterns = [
    *[path(keys,view) for keys,view in months.items()]
]
