from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blogs/', views.all_blogs, name='all_blogs'),
     path('create-post/', views.create_post, name='create_post'),
     path('create-blog/', views.create_blogger, name='create_blogger'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
