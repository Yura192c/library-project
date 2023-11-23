from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text='Название книги')
    author = models.CharField(max_length=100,
                              help_text='Автор')
    publication_year = models.IntegerField(help_text="Год публикации")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character')

    def __str__(self):
        return self.title
