from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category, Product


class Command(BaseCommand):
    def reset_auto_increment(self, table_name):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), 1, false);")

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        # Сброс автоинкремента для таблицы Category
        self.reset_auto_increment(Category._meta.db_table)
        # Сброс автоинкремента для таблицы Product
        self.reset_auto_increment(Product._meta.db_table)


        category_list = [
            {"category_name": "молоко", "description": "натуральное"},
            {"category_name": "колбаса", "description": "варёная"},
            {"category_name": "сыр", "description": "твердый сыр"},
            {"category_name": "овощи", "description": "замороженые"},
            {"category_name": "овощи", "description": "свежие"},
            {"category_name": "фрукты", "description": "свежие"},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)




        product_list = [
                    {
                        "product_name": "яблоко",
                        "description": "зеленое",
                        "img": "img/1676653795-yabloki-fon-zelenie-239.jpg",
                        "category_name": Category.objects.get(pk=6),
                        "purchase_price": 120
                    },
                    {
                        "product_name": "слива",
                        "description": "синяя",
                        "img": "img/cae3eda2ded864a53596503c623b8f2a.jpeg",
                        "category_name": Category.objects.get(pk=6),
                        "purchase_price": 300
                    },
                    {
                        "product_name": "картофель",
                        "description": "свежий урожай",
                        "img": "img/Kartofel.jpg",
                        "category_name": Category.objects.get(pk=5),
                        "purchase_price": 60
                    },
                    {
                        "product_name": "броколи",
                        "description": "заморожен",
                        "img": "img/dfcb8300c3a7e8e902e691c6c9554d09.jpeg",
                        "category_name": Category.objects.get(pk=4),
                        "purchase_price": 130
                    },

                ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
