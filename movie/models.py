from django.db import models
from datetime import datetime

gender_choice = [(0, "Male"), (1, 'Female')]

# Create your models here.


class Years(models.Model):
    year = models.IntegerField(unique=True)
    add_date = models.DateTimeField(auto_now=True)


class Movie_Category(models.Model):
    name = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now=True)


class Qualities(models.Model):
    title = models.CharField(max_length=20)
    add_date = models.DateTimeField(auto_now=True)


class Subtitle(models.Model):
    language = models.CharField(max_length=5)
    sub_file = models.CharField(max_length=50)


class Genres(models.Model):
    name = models.CharField(max_length=30)
    add_date = models.DateTimeField(auto_now=True)


class Actors(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(blank=True)
    gender = models.CharField(max_length=10, choices=gender_choice, default=0)
    place_of_birth = models.CharField(max_length=100, blank=True)
    biography = models.TextField(blank=True)
    profile_pic = models.ImageField('actors/%Y/%m/%d/', blank=True)
    tmdb_id = models.IntegerField(blank=True)
    imdb_id = models.CharField(max_length=10, blank=True)


class Trailers(models.Model):
    key = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    site = models.CharField(max_length=15)
    trailer_type = models.CharField(max_length=20)


class Collections(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length=250)
    poster = models.ImageField(upload_to='collections/%Y/%m/%d/', blank=True)
    backdrop = models.ImageField(upload_to='collections/%Y/%m/%d/', blank=True)


class Movies(models.Model):
    title = models.CharField(max_length=300)
    year = models.ForeignKey(Years, on_delete=models.SET_NULL, null=True)
    catagory = models.ForeignKey(
        Movie_Category, null=True, on_delete=models.SET_NULL)
    quality = models.ForeignKey(
        Qualities, null=True, on_delete=models.SET_NULL)
    subtitle = models.ForeignKey(
        Subtitle, null=True, on_delete=models.SET_NULL)
    tagline = models.CharField(max_length=600, blank=True)
    overview = models.TextField(blank=True)
    file_path = models.CharField(max_length=500)
    file_size = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    poster = models.ImageField(upload_to='movies/%Y/%m/%d/')
    backdrop = models.ImageField(upload_to='movies/%Y/%m/%d/', blank=True)
    img_1 = models.ImageField(upload_to='movies/%Y/%m/%d/', blank=True)
    img_2 = models.ImageField(upload_to='movies/%Y/%m/%d/', blank=True)
    img_3 = models.ImageField(upload_to='movies/%Y/%m/%d/', blank=True)
    img_4 = models.ImageField(upload_to='movies/%Y/%m/%d/', blank=True)
    tmdb_id = models.IntegerField(blank=True)
    imdb_id = models.CharField(max_length=10, blank=True)
    release_date = models.DateField(blank=True)
    views = models.IntegerField()
    is_pub = models.BooleanField(default=True)
    add_date = models.DateTimeField(default=datetime.now)
    # Those are many to many relation
    genres = models.ManyToManyField(Genres)
    collections = models.ManyToManyField(Collections)
    actors = models.ManyToManyField(Actors)
    trailers = models.ManyToManyField(Trailers)
