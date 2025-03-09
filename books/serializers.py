from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['full_name', 'age']


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# serializers nima? u nima uchun kerak, nima ish bajaradi?
