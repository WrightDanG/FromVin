from products.models import Product
from django.contrib import messages
from django.shortcuts import (render, redirect, reverse, HttpResponse,
                              get_object_or_404)


def view_bag(request):
    """ A view for the shopping bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    # Get the product so that we can reference it in the message
    product = get_object_or_404(Product, pk=item_id)
    # Pass the amount of items and url for the user
    # to return to their previous place.
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # If there is no 'bag' in the session then go ahead and create one
    bag = request.session.get('bag', {})

    # Increment the quantity, or add the product
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    messages.success(request, f"Added {quantity}x '{product.name}' to Bag")
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    # Get the product so that we can reference it in the message
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f"Updated '{product.name}' in Bag")
    else:
        bag.pop(item_id)
        messages.success(request, f"Removed '{product.name}' from Bag")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    # Get the product so that we can reference it in the message
    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        # Pop will remove and not save the item
        bag.pop(item_id)

        request.session['bag'] = bag
        messages.success(request, f"Removed '{product.name}' from Bag")
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item '{product.name}': {e}")
        return HttpResponse(status=500)
