# books/tests.py
from django.test import TestCase
from src.library.models import Book


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title='Test Book',
            author='Test Author',
            publication_year=2022,
            isbn='1234567890123'
        )

    def test_title_field(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_author_field(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_publication_year_field(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('publication_year').verbose_name
        self.assertEqual(field_label, 'publication year')

    def test_isbn_field(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_str_representation(self):
        book = Book.objects.get(id=1)
        self.assertEqual(str(book), 'Test Book')
