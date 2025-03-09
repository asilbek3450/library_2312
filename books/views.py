from django.shortcuts import render
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class BookAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)  # objectni json ko'rinishga o'tkazadi
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)  # json ko'rinishdan objectga o'tkazadi
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):

    # retrieve, put patch delete
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorAPIView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailAPIView(APIView):

    def get(self, request, pk):
        author = Author.objects.get(id=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = Author.objects.get(id=pk)
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = Author.objects.get(id=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
