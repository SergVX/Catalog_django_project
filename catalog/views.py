
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product, Category
from catalog.utils import save_contact_data


# def home(request):
#     templates = 'catalog/home.html'
#     products_list = Product.objects.all()
#     context = {'object_list': products_list,
#                'title': 'Главная страница'}
#     return render(request, templates, context)

class ProductListView(ListView):
    """Класс-контроллер для страницы со списком продуктов"""
    model = Product  # Модель с которой он работает
    template_name = 'catalog/home.html'
    extra_context = {'title': 'Список товаров'}  # Заголовок страницы


# def contacts(request):
#     templates = 'catalog/contacts.html'
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name}({phone}): {message}')
#
#         save_contact_data(name, phone, message)
#
#     return render(request, templates)

class ContactsListView(TemplateView):
    """Класс-контроллер страницы с контактами"""
    template_name = 'catalog/contacts.html'  # Шаблон для отображения
    extra_context = {'title': 'Наши контакты'}  # Заголовок страницы

# def card_product(request):
#     templates = 'catalog/card_product.html'
#     return render(request, templates)

class ProductDetailView(DetailView):
    model = Product  # Модель с которой он работает
    template_name = 'catalog/card_product.html'
    extra_context = {'title': 'Карточка товара'}  # Заголовок страницы
    # slug_url_kwarg = 'product_slug'