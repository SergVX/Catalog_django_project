from django.urls import path
from catalog.views import home, contacts, card_product

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('card_product/', card_product, name='card_product'),
]