from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    # Fetch the profile for the user
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Populate user's profile
        form = UserProfileForm(request.POST, instance=profile)
        # Save
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    # Get all orders attached to the profile
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        # Tell the template that the user came from profile, not checkout.
        'from_profile': True,
    }

    return render(request, template, context)
