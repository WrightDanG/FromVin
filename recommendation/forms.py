from django import forms

# Was originally going to live in models.py
# But forms.py made more sense in context

# Identify broad types of wine

WINE_CHOICES = [
    ('0', 'I like my wine...'),
    ('1', 'Red: Soft, fruity and light'),
    ('2', 'Red: Well rounded, berry-flavoured and full'),
    ('3', 'Red: Deep, Earthy and Poweful'),
    ('4', 'White: Subtle, Light, Floral'),
    ('5', 'White: Fruity, Zesty with a punch'),
    ('6', 'White: Strong, Complex and Mineral-y')
]

# Identify broad types of cheese

CHEESE_CHOICES = [
    ('0', 'I like my cheese...'),
    ('7', 'Soft: Crumbly, Mellow, Light '),
    ('8', 'Soft: Gooey, Creamy, Sweet-notes'),
    ('9', 'Soft: Punchy, Rich and Strong'),
    ('10', 'Hard: Subtle and a little sweet'),
    ('11', 'Hard: Sharp, Flavoursome'),
    ('12', 'Hard: The Smellier the better')
]


class WineForm(forms.Form):
    wine_choice = forms.ChoiceField(choices=WINE_CHOICES)


class CheeseForm(forms.Form):
    cheese_choice = forms.ChoiceField(choices=CHEESE_CHOICES)
