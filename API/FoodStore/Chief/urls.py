from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ChiefViewSet



router = DefaultRouter()
router.register('',ChiefViewSet,basename='chief')
app_name='chief'


urlpatterns = [
    path('',include(router.urls))

]
