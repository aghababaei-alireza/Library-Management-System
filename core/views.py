from django.shortcuts import render
from .models import Category, Book, Person, Publisher


def home(request):
    categories = Category.objects.all().order_by('name')[:10]
    books = Book.objects.all()[:10]

    num_categories = Category.objects.all().count()
    num_books = Book.objects.all().count()
    num_authors = Person.objects.all().count()
    num_publishers = Publisher.objects.all().count()

    context = {
        'stat': {
            'categories': num_categories,
            'books': num_books,
            'authors': num_authors,
            'publishers': num_publishers
        },
        'categories': categories,
        'books': books
    }
    return render(request, 'core/home.html', context)


def book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'core/book.html', context)
