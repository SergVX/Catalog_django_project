from django.shortcuts import render

from catalog.utils import save_contact_data


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    templates = 'catalog/contacts.html'
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')

        save_contact_data(name, phone, message)

    return render(request, templates)
