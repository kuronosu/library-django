
from django.urls import path

from .views import (CreateBookView, DeleteBookView, DetailBookView,
                    ListBookView, UpdateBookView)

app_name = 'books'

urlpatterns = [
    path('', ListBookView.as_view(), name='book_list'),
    path('create/', CreateBookView.as_view(), name='book_create'),
    path('<int:pk>/', DetailBookView.as_view(), name='book_detail'),
    path('<int:pk>/update/', UpdateBookView.as_view(), name='book_update'),
    path('<int:pk>/delete/', DeleteBookView.as_view(), name='book_delete'),
]
