from django.db import models
from django.template.defaultfilters import slugify


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')
    image = models.ImageField(upload_to='image/catalog', height_field=None, width_field=None, max_length=100, verbose_name='изображение', null=True)
    category_name = models.ForeignKey("Category", on_delete=models.CASCADE)
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.description}'

    class Meta:
        verbose_name = 'продукт' # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты' # Настройка для наименования набора объектов


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов

class Blog(models.Model):
    """Модель записи в блоге"""
    title = models.CharField(max_length=50, verbose_name='Название')  # Заголовок
    slug = models.SlugField(max_length=50, verbose_name='Slug')  # Slug (человекопонятный URL)
    content = models.TextField(verbose_name='Содержимое')  # Текст записи
    image = models.ImageField(upload_to='image/blog', blank=True, null=True, verbose_name='Изображение')  # Превью
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # Дата создания (генерируется автоматически)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')  # Метка публикации статьи
    views_count = models.IntegerField(default=0)  # количество просмотров (по умолчанию 0)

    def __str__(self):
        """Строковое представление"""
        return f'{self.title} {self.created_at}'

    # def __init__(self, *args, **kwargs):
    #     """Переопределение метода __init__ для автоматического формирования слага"""
    #     super().__init__(*args, **kwargs)
    #     self.slug = slugify(self.title)
    #     save = self.save()

    # def get_absolute_url(self):
    #     # return reverse_lazy('blog:blog_detail', kwargs={'blog_slug': self.slug}) - если в контроллере слаг
    #     if self.is_published:
    #         return reverse_lazy('blog:blog')
    #     else:
    #         return reverse_lazy('blog:developing_posts')

    def save(self, *args, **kwargs):
        """Переопределение метода для автоматического формирования слага"""
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'