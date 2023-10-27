from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    description = models.TextField(
        verbose_name="Description", null=True, blank=True)
    image = models.ImageField(
        upload_to="images/people/", null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "People"


class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    description = models.TextField(
        verbose_name="Description", null=True, blank=True)
    image = models.ImageField(
        upload_to="images/publishers/", null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    description = models.TextField(
        verbose_name="Description", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def num_books(self):
        return self.books.count()

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField(max_length=400)
    authors = models.ManyToManyField(
        Person, related_name="written_books", verbose_name="Authors")
    translators = models.ManyToManyField(
        Person, related_name="translated_books", verbose_name="Translators", blank=True)
    publisher = models.ForeignKey(
        Publisher, related_name="books", verbose_name="Publisher", on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category, related_name="books", verbose_name="Categories")
    year = models.IntegerField(verbose_name="Year Published")
    isbn10 = models.CharField(verbose_name="ISBN10",
                              max_length=10, null=True, blank=True, unique=True)
    isbn13 = models.CharField(verbose_name="ISBN13",
                              max_length=13, null=True, blank=True, unique=True)
    num_pages = models.IntegerField(
        verbose_name="Number of Pages", null=True, blank=True)
    description = models.TextField(
        verbose_name="Description", null=True, blank=True)
    edition = models.IntegerField(
        verbose_name="Edition", null=True, blank=True)
    image = models.ImageField(
        upload_to="images/books/", null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def authors_names(self):
        return ', '.join(a.full_name for a in self.authors.all())


class BookCopy(models.Model):
    book = models.ForeignKey(Book, related_name="copies",
                             verbose_name="Book", on_delete=models.CASCADE)
    serial = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.book.title}-[{self.serial}]"

    class Meta:
        verbose_name_plural = "BookCopies"


class Reserve(models.Model):
    book_copy = models.ForeignKey(
        BookCopy, related_name="reseved", verbose_name="Book Copy", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="reserved", verbose_name="User", on_delete=models.CASCADE)
    reserve_time = models.DateField(
        auto_now=True, verbose_name="Time Reserved")

    def __str__(self):
        return f"{self.user} -> {self.book_copy}"


class Checkout(models.Model):
    book_copy = models.ForeignKey(
        BookCopy, related_name="checked_out", verbose_name="Book Copy", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="checked_out", verbose_name="User", on_delete=models.CASCADE)
    start_date = models.DateField(
        verbose_name="Start Date", auto_now_add=True)
    expected_return_date = models.DateField(
        verbose_name="Expected Return Date")
    num_extended = models.IntegerField(
        verbose_name="Number of Extending Return Date", default=0)
    return_date = models.DateField(
        verbose_name="Return Date", null=True, blank=True)
    is_returned = models.BooleanField(
        verbose_name="Is Returned", default=False)

    def __str__(self):
        return f"[{self.start_date}] - {self.user} -> {self.book_copy}"
