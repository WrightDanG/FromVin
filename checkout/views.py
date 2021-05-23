from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Handle the overall checkout view


def checkout(request):
    bag = request.session.get('bag', {})
    # Stop people accessing /checkout via url without items.
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_0SMREd7Vdweb1MGRi8S0EycR00JVzSAs5O',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
