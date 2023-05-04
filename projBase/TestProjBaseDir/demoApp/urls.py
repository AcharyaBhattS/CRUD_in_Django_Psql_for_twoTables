from django.contrib import admin
from django.urls import path
from demoApp import views

urlpatterns = [
    path('', views.home, name="home"),
]
