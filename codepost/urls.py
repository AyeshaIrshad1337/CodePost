from django.contrib import admin
from django.urls import path, include
from .import views 
urlpatterns = [
   
    path('', views.codehome, name='codehome'),
    path('<str:slug>',views.codepost, name='codepost')
    
] 