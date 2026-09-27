from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.index,name='home'),
    path('addtodo', views.addtodo,name='addtodo'),
]