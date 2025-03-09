from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


BOOK_LANGUAGES = {
    'en': 'English',
    'ru': 'Russian',
    'uz': 'Uzbek',
}


# Foreign Key -
# avtorlar - Saidbek, Jon Jons, Nurulloh

# kitoblar - Python, Harry Potter, Django

# Foreign key -> ManyToOne
# ManyToOne, OneToMany, ManyToMany

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=50)
    pages = models.IntegerField()
    language = models.CharField(max_length=50, choices=BOOK_LANGUAGES)
    cover_image = models.URLField()

    def __str__(self):
        return f'{self.title} | Muallifi: {self.author}'
