from django.urls import path
from catalog.views import ContactsListView, ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('<slug:pk>/product', ProductDetailView.as_view(), name='card_product'),
]