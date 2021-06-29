from django.urls import path
from . import views
from .webhooks import webhook

# State url paths needed for the checkout application
urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    # Webhooks - stripe related
    path('wh/', webhook, name='webhook'),
]
