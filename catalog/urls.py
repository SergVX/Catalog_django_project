from django.urls import path
from catalog.views import ContactsListView, ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('<slug:pk>/product', ProductDetailView.as_view(), name='card_product'),
    # path('blog/', BlogList.as_view(), name='blog'),  # http://127.0.0.1:8000/blog/  Список статей блога
    # path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_post'),  # http://127.0.0.1:8000/blog/<slug>
    # path('create_post/', BlogCreatePost.as_view(), name='create_post'),  # http://127.0.0.1:8000/create_post/
    # path('update_post/<slug:slug>/', BlogUpdatePost.as_view(), name='update_post'), # http://127.0.0.1:8000/update_post/
    # path('delete_post/<slug:slug>/', BlogDeletePost.as_view(), name='delete_post')  # http://127.0.0.1:8000/delete_post/
]