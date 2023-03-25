from django.urls import path
from .views import getRoutes, getBooks, saveBooks

urlpatterns = [
    path("", getRoutes, name="Routes"),
    path("books", getBooks, name="Books"),
    path("savebooks", saveBooks, name="SaveBooks"),
]
