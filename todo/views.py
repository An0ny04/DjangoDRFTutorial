from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BookSerializer

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    return Response({"data": "data"})


@api_view(["GET"])
def getBooks(request):
    books = Books.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def saveBooks(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
