from django.views.generic.edit import CreateView
from django.shortcuts import render

from products.models import Product, Category

from.forms import WineForm, CheeseForm


# Create your views here.


def recommendation(request):
    """ Returns the recommendation page. """
    context = {}
    context['wineform'] = WineForm()
    context['cheeseform'] = CheeseForm()

    # if 'wine_choice' in request.GET:
    #     wineValue = request.GET['wine_choice']
    #     print(wineValue)
    # elif 'cheese_choice' in request.GET:
    #     cheeseValue = request.GET['cheese_choice']
    #     print(cheeseValue)
    return render(request, 'recommendation/recommendation.html', context)

# Potentially add back to main method?


def choose(request):

    if 'wine_choice' in request.GET:
        wineValue = request.GET['wine_choice']
        print(wineValue)
    elif 'cheese_choice' in request.GET:
        cheeseValue = request.GET['cheese_choice']
        print(cheeseValue)
    return render(request, 'recommendation/recommendation.html')
