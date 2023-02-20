from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Book(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    image = models.ImageField(verbose_name='Image',
                              upload_to='images/', null=True, blank=True)
    synopsis = models.TextField(verbose_name='Synopsis')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('books:book_detail', kwargs={'pk': self.pk})
