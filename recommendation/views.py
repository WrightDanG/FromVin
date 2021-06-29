from django.shortcuts import render
from random import sample

from products.models import Product

from.forms import WineForm, CheeseForm


def recommendation(request):
    """ Returns the recommendation page. """
    # Add wine and cheese selections to context
    context = {}
    context['wineform'] = WineForm()
    context['cheeseform'] = CheeseForm()

    return render(request, 'recommendation/recommendation.html', context)


# Return filtered products for display on recommend page.
def choose(request):

    if 'wine_choice' in request.GET:
        wineValue = request.GET['wine_choice']
        print(wineValue)
        queryset = Product.objects.all()
        filtered = queryset.filter(tastingprofile=wineValue)
        if filtered:
            products = sample(list(filtered), 3)
        else:
            products = {}

    elif 'cheese_choice' in request.GET:
        cheeseValue = request.GET['cheese_choice']
        print(cheeseValue)
        queryset = Product.objects.all()
        filtered = queryset.filter(tastingprofile=cheeseValue)
        if filtered:
            products = sample(list(filtered), 3)
        else:
            products = {}

    context = {'products': products}
    context['wineform'] = WineForm()
    context['cheeseform'] = CheeseForm()
    return render(request, 'recommendation/recommendation.html', context)
