from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AuthorViewSet



router = DefaultRouter()
router.register('',AuthorViewSet,basename='author')
app_name='author'


urlpatterns = [
    path('',include(router.urls))

]
