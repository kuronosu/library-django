from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from books.forms import BookForm
from books.models import Book

# Create your views here.


class DetailBookView(DetailView):
    model = Book
    template_name = 'books/detail.html'


class ListBookView(ListView):
    model = Book
    queryset = Book.objects.all().order_by('-pk')
    paginate_by = 20
    template_name = 'books/list.html'
    context_object_name = 'books'


class CreateBookView(CreateView):
    model = Book
    template_name = 'books/create.html'
    form_class = BookForm


class DeleteBookView(DeleteView):
    model = Book
    template_name = 'books/delete.html'
    success_url = reverse_lazy('books:book_list')


class UpdateBookView(UpdateView):
    model = Book
    template_name = 'books/update.html'
    form_class = BookForm
    success_url = reverse_lazy('books:book_list')
