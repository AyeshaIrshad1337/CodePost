from django.contrib import admin
from django.urls import path, include
from home import views 

urlpatterns = [
    path('', views.index,name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search',views.search,name='search'),
    path('login_signup', views.login_signup, name='login_signup'),
    path('signup', views.handleSignup, name='signup'),
 #   path('signup',views.handleSignup, name='handleSignup'),
   path('login', views.handleLogin, name='login'),
   # path('logout',views.handleLogout, name='handlelogout')
    
] 
# iam gonna set views.main here with the main html file in views.py
