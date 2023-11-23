from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        """ Получение информации о конкретной книге """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ Обновление информации о книге """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ Удаление книги"""
        return self.destroy(request, *args, **kwargs)


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        """ Получение списка всех книг """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Создание новой книги """
        return self.create(request, *args, **kwargs)