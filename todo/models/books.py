from django.db import models
from .author import Author


class Books(models.Model):
    name = models.CharField(max_length=250)
    author = models.ManyToManyField(Author, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
