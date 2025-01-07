from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import BookViewSet

router=DefaultRouter()
router.register('',BookViewSet,basename='Books')
app_name='book'


urlpatterns = [
    path('',include(router.urls))
]
