from django.shortcuts import render
from django.conf import settings

# Create your views here.


def index(request):
    """ Returns the index page for the guide. """
    context = {}
    return render(request, 'guide/index.html', context)
