from django.views.generic.edit import CreateView
from django.shortcuts import render

from products.models import Product, Category

from.forms import WineForm, CheeseForm


# Create your views here.


def recommendation(request):
    """ Returns the recommendation page. """

    #products = Product.objects.all()
    #categories = None

    #products = products.filter(category=2)
    #categories = Category.objects.filter(name__in="red_wine")

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
        products = Product.objects.all()
        products = products.filter(category=wineValue)
    #categories = None

    elif 'cheese_choice' in request.GET:
        cheeseValue = request.GET['cheese_choice']
        print(cheeseValue)
        products = Product.objects.all()
        products = products.filter(category=cheeseValue)
    #categories = None

    context = {'products': products}
    context['wineform'] = WineForm()
    context['cheeseform'] = CheeseForm()
    return render(request, 'recommendation/recommendation.html', context)
