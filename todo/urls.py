from django.urls import path
from .views import getRoutes, BooksAPI

urlpatterns = [
    path("", getRoutes, name="Routes"),
    path("books", BooksAPI.as_view(), name="Books"),
    # path("books/<int:id>", BooksAPI.as_view(), name="Books"),
    # path("savebooks", saveBooks, name="SaveBooks"),
]
