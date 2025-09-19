from django.db import models
from musician.models import Musician

# Create your models here.

class Album(models.Model):
    
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_name= models.CharField(max_length=100)
    release_date = models.DateField()


    Rating_choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = models.IntegerField(choices=Rating_choices)

    def __str__(self):
        return f"{self.album_name} {self.musician}"