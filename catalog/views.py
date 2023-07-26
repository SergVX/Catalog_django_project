from django.shortcuts import render

from catalog.models import Product
from catalog.utils import save_contact_data


def home(request):
    templates = 'catalog/home.html'
    products_list = Product.objects.all()
    context = {'object_list': products_list,
               'title': 'Главная страница'
    }
    return render(request, templates, context)


def contacts(request):
    templates = 'catalog/contacts.html'
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')

        save_contact_data(name, phone, message)

    return render(request, templates)


def card_product(request):
    templates = 'catalog/card_product.html'
    return render(request, templates)