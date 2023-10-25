from django.shortcuts import render
from .models import Category


def home(request):
    categories = [Category(name='Fantasy', description='Fantasy encompasses a huge part of the book world. It’s one of the most popular book genres out there—a personal favorite of mine to read and write.'),
                  Category(
                      name='Adventure', description='Writing a novel in the adventure category will require a trip, journey, or quest of some kind as the overall plot.'),
                  Category(
                      name='Contemporary', description='This book genre is among the most popular, though most writers aren’t sure of what this category even is.'),
                  Category(
                      name='Mystery', description='We’ve all heard of the mystery book genres. It’s an extremely popular genre, and for a good reason.'),
                  Category(
                      name='Horror', description='Horror novels are characterized by the fact that the main plot revolves around something scary and terrifying.'),
                  Category(name='Romance', description='Romance authors have one specific goal when it comes to their books: to make you fall in love with the characters just as much as the characters fall in love with each other.')]
    context = {
        'categories': categories
    }
    return render(request, 'core/home.html', context)
