from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommendation, name='recommendation'),
    path('choose/', views.choose, name='choose'),
]
