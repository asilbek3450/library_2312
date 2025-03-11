from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['full_name', 'age']

    def validate(self, attrs):

        ism_familiya = attrs['full_name']
        if ism_familiya:
            for i in ism_familiya:
                if i.isdigit():
                    raise ValidationError("Ism familiyada raqam bo'lishi mumkinmas")
        return attrs


# class AuthorSerializer(Serializer):
#     full_name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     country = serializers.CharField(max_length=50)
#
#     def create(self, validated_data):
#         return Author.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.full_name = validated_data.get('full_name', instance.full_name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.country = validated_data.get('country', instance.country)
#         instance.save()
#         return instance


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        pass
# price 0 dan katta bo'lishi kerak
# genre da raqam bo'lishi mumkinmas
# year da 2025 dan baland qo'yish mumkinmas



# serializers nima? u nima uchun kerak, nima ish bajaradi?
# validated_data = {  # post put patch qilinganda tekshiruvdan o'tib keladigan ma'lumotlar
#     "full_name": "Saidbek Saidakbarov",
#     "age": 90,
#     "country": "Britaniya"
# }
