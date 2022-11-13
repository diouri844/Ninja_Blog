from django.urls import path
from . import views
# add home router path handler : 
urlpatterns = [
    path('', views.Blog_home,name='blog-home'),
    path('About/',views.Blog_about, name='about-blog'),
    path('Login/',views.Blog_login,name='login-blog'),
    path('Register/',views.Blog_register, name='register-blog'),
]
