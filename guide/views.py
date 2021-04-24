from django.shortcuts import render

# Create your views here.


def index(request):
    """ Returns the index page for the guide. """
    return render(request, 'guide/index.html')
