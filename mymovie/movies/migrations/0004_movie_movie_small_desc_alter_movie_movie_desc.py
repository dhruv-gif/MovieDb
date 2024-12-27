# Generated by Django 5.1.4 on 2024-12-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_movie_genre_movie_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_small_desc',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_desc',
            field=models.CharField(max_length=20),
        ),
    ]