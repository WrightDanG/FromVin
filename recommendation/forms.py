from django import forms
from django.forms import ModelForm


WINE_CHOICES = [
    ('0', 'I like my wine...'),
    ('1', 'Red: Soft, fruity and light'),
    ('2', 'Red: Well rounded, berry-flavoured and full'),
    ('3', 'Red: Deep, Earthy and Poweful'),
    ('4', 'White: Subtle, Light, Floral'),
    ('5', 'White: Fruity, Zesty with a punch'),
    ('6', 'White: Strong, Complex and Mineral-y')
]

# Possibly change cats to be more approachable - Light / smelly / sweet

CHEESE_CHOICES = [
    ('0', 'I like my cheese...'),
    ('1', 'Soft: Crumbly, Mellow, Light '),
    ('2', 'Soft: Gooey, Creamy, Sweet-notes'),
    ('3', 'Soft: Punchy, Rich and Strong'),
    ('4', 'Hard: Subtle and a little sweet'),
    ('5', 'Hard: Sharp, Flavoursome'),
    ('6', 'Hard: The Smellier the better')
]


class WineForm(forms.Form):
    wine_choice = forms.ChoiceField(choices=WINE_CHOICES)


class CheeseForm(forms.Form):
    cheese_choice = forms.ChoiceField(choices=CHEESE_CHOICES)
