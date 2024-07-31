from django.db import models

# Create your models here.

class Movies(models.Model):
    
    """
    Represents a movie in the database with detailed attributes.

    Fields:
        episode_nb: An integer field that is the primary key of the model. 
            Represents the episode number of the movie.
        title: A string field with a maximum length of 64 characters that
            must be unique. Represents the movie's title.
        opening_crawl: A text field that can be empty or null, used for
            additional information like the opening crawl of the movie.
        director: A string field with a maximum length of 32 characters.
            Represents the movie's director.
        producer: A string field with a maximum length of 128 characters.
            Represents the movie's producer.
        release_date: A date field that cannot be null, representing the
            movie's release date.

    Methods:
        __str__: Returns the title of the movie as its string representation.

    Meta Options:
        db_table: The name of the database table that will store the model's records.
    """

    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64, unique=True, null=False)
    opening_crawl = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ex01_movies'
