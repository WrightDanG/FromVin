from django.urls import path
from . import views

# Register url path for the main home screen
urlpatterns = [
    path('', views.index, name='guide'),
]
