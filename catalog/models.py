from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, verbose_name='изображение')
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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов