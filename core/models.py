from django.db import models


class People(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    description = models.TextField(
        verbose_name="Description", null=True, blank=True)
    image = models.ImageField(
        upload_to="images/people/", null=True, blank=True)


class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    description = models.TextField(
        verbose_name="Description", null=True, blank=True)
    image = models.ImageField(
        upload_to="images/publishers/", null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    description = models.TextField(
        verbose_name="Description", null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=400)
    authors = models.ManyToManyField(
        People, related_name="written_books", verbose_name="Authors")
    translators = models.ManyToManyField(
        People, related_name="translated_books", verbose_name="Translators", null=True, blank=True)
    publisher = models.ForeignKey(
        Publisher, related_name="books", verbose_name="Publisher")
    categories = models.ManyToManyField(
        Category, related_name="books", verbose_name="Categories")
    year = models.IntegerField(verbose_name="Year Published")
    isbn10 = models.CharField(verbose_name="ISBN10",
                              max_length=10, null=True, blank=True)
    isbn13 = models.CharField(verbose_name="ISBN13",
                              max_length=13, null=True, blank=True)
    num_pages = models.IntegerField(
        verbose_name="Number of Pages", null=True, blank=True)
    description = models.TextField(
        verbose_name="Description", null=True, blank=True)
    edition = models.IntegerField(
        verbose_name="Edition", null=True, blank=True)


class BookCopy(models.Model):
    book = models.ForeignKey(Book, related_name="copies",
                             verbose_name="Book Copies")
    serial = models.CharField(max_length=15)
