from django.urls import path
from . import views

# Register URL paths for recommend application
urlpatterns = [
    path('', views.recommendation, name='recommendation'),
    path('choose/', views.choose, name='choose'),
]
