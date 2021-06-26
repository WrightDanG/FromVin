from django.shortcuts import render
from django.conf import settings

# Create your views here.


def index(request):
    """ Returns the index page for the guide. """
    context = {'image_url': settings.IMAGE_URL}
    return render(request, 'guide/index.html', context)
