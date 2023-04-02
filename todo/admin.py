from django.contrib import admin
from .models.author import Author
from .models.books import Books

# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
