from django.db import models

# Create your models here.
class Movie(models.Model):
    genres = (
        ('ACTION', 'ACTION'),
        ('THRILLER', 'THRILLER'),
        ('ROMANCE', 'ROMANCE'),
        ('COMIC', 'COMIC'),
        ('CLASSIC', 'CLASSIC'),
        ('DRAMA', 'DRAMA'),
    )


    movie_name = models.CharField( max_length=50)
    movie_desc = models.TextField(max_length=1300, null=True)
    movie_small_desc = models.CharField(max_length=200, null=True)
    movie_img = models.ImageField(upload_to='media/')
    movie_genre = models.TextField(choices=genres, null=True)
    movie_year = models.DateField(null=True)
    movie_writers = models.CharField(max_length=30, null=True)
    movie_director = models.CharField(max_length=30, null=True)
    movie_runtime = models.CharField(max_length=10, null=True)


    def __str__(self):
        return self.movie_name