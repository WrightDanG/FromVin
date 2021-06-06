from django.shortcuts import render

# Create your views here.

def recommendation(request):
    """ Returns the index page for the guide. """
    return render(request, 'recommendation/recommendation.html')
