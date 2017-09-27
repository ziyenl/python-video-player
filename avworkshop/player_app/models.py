from django.db import models

# Movie object
class Movie(models.Model):
    imdb_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image_url = models.URLField()

    @classmethod
    def create(cls, imdb_id, title, image_url):

        instance = cls(
            imdb_id=imdb_id,
            title=title, 
            image_url=image_url)

        return instance

class MovieDetails(models.Model):
    imdb_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    plot_outline = models.CharField(max_length=200)
    rating = models.FloatField()
     
    image_url = models.URLField()
    trailer_url = models.URLField()
     
    @classmethod
    def create(
        cls, 
        imdb_id, 
        title, 
        year,
        plot_outline,
        rating,
        image_url,
        trailer_url):

        instance = cls(
            imdb_id=imdb_id, 
            title=title, 
            year=year,
            plot_outline=plot_outline,
            rating=rating,
            image_url=image_url,
            trailer_url=trailer_url)

        return instance