from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(Reserve)
admin.site.register(Checkout)
