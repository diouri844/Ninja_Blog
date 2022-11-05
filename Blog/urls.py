from django.urls import path
from . import views
# add home router path handler : 
urlpatterns = [
    path('', views.Blog_home,name='blog-home'),
]
