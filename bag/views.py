from django.shortcuts import render, redirect


def view_bag(request):
    """ A view for the shopping bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    # Pass the amount of items and url for the user to return to their previous place.
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
    return redirect(redirect_url)
