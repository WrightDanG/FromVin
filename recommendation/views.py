from django.views.generic.edit import CreateView
from django.shortcuts import render

from.forms import WineForm, CheeseForm


# Create your views here.


def recommendation(request):
    """ Returns the recommendation page. """
    context = {}
    context['wineform'] = WineForm()
    context['cheeseform'] = CheeseForm()
    return render(request, 'recommendation/recommendation.html', context)
