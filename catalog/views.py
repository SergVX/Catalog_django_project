from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Category, Blog
from catalog.utils import save_contact_data, send_email_100


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

class BlogList(ListView):
    """Класс-контроллер для страницы со списком постов блога"""
    model = Blog  # Модель с которой он работает
    extra_context = {'title': 'Блог'}  # Заголовок страницы

    def get_queryset(self):
        """Отбор постов у которых is_published=True для отображения на странице"""

        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    """Класс-контроллер для детального отображения информации о посте"""

    model = Blog  # модель, с которой он работает

    def get_object(self, queryset=None):
        """Переопределение метода get_object для увеличения количества просмотров"""

        object = super().get_object()
        object.views_count += 1  # увеличение количества просмотров

        # Проверка, есть ли 100 просмотров у поста
        if object.views_count == 100:
            send_email_100(object.title)  # Отправка сообщения на почту 'aleksandr1990veselov@yandex.ru'(не работает)

        object.save()  # сохранение в базе данных

        return object


class BlogCreatePost(CreateView):
    """Класс-контроллер для отображения страницы с формой создание поста"""

    model = Blog  # Модель с которой он работает
    fields = ('title', 'content', 'image', 'is_published')  # Поля для построения формы
    success_url = '/blog/'  # URL адрес, на который происходит перенаправление после успешного создания записи в блоге


class BlogUpdatePost(UpdateView):
    """Класс-контроллер для отображения формы изменение записи"""
    model = Blog  # Модель, с которой он работает
    fields = ('title', 'content', 'image', 'is_published')  # поля для отображения в форме

    def get_success_url(self, *args, **kwargs):
        """Переопределение метода get_success_url для формирования правильного URL на который происходит
        перенаправление после успешного изменения записи блога"""

        slug = self.kwargs['slug']  # slug статьи
        url = reverse_lazy('catalog:blog_post', args=[slug])  # формирование URL

        return url


class BlogDeletePost(DeleteView):
    """Класс-контроллер для уделения записи в блоге"""
    model = Blog  # Модель, с которой он работает
    success_url = '/blog/'  # URL адрес, на который происходит перенаправление после успешного удаления записи в блоге