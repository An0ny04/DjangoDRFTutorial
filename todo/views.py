from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Books
from rest_framework.views import APIView
from .serializers import BookSerializer

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    return Response({"data": "data"})


# @api_view(["GET"])
# def getBooks(request):
#     books = Books.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)


# @api_view(["POST"])
# def saveBooks(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


class BooksAPI(APIView):
    def get(self, request):
        books = Books.objects.filter(is_deleted=False)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        book_id = request.data.get("id")
        Book = Books.objects.get(id=book_id)
        Book.is_deleted = True
        Book.save()
        return Response({"message": "Deleted"})
