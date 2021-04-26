from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view in which to display all products. """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
