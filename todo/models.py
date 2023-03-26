from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=250)
    author = models.ManyToManyField(Author, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
