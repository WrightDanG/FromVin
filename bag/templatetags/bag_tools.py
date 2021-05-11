from django import template

# Register as a template
register = template.Library()

# Decorate and declare a function for calculating the bag subtotal.


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
