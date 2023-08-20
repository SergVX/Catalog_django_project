from django.contrib import admin

from catalog.models import Product, Category, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'purchase_price', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('product_name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Админ-панель для работы с моделью Blog"""

    list_display = ['title', 'slug', 'content']  # Поля для отображения в админ-панели
    prepopulated_fields = {'slug': ('title',)}  # Поле для автоматического заполнения исходя из поля title