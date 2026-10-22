from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()
    publisher = models.CharField(max_length=255)
    # published_date = model.DataTimefield()
    # version = models.IntegerField()
    genre = models.CharField(max_length=3,
    choices=[("sci", "Science"),("sfi", "Science Fiction"), ("fan", "Fantasy "), ("nov", "Novel")]
    )
