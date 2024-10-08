from django.db import models, transaction, IntegrityError

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
        db_table = 'ex05_movies'
        verbose_name_plural = "Movies"
        
    @classmethod
    def fetchall(cls):

        """
        Retrieves all movies from the database.

        Returns:
            list: A list of tuples, each containing the details of a movie.

        Raises:
            Exception: If an error occurs during the retrieval
        """

        try:
            movies = cls.objects.all()
            return [(movie.episode_nb, movie.title, movie.opening_crawl, movie.director, movie.producer, movie.release_date) for movie in movies]
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
    
    @classmethod
    def insert(cls, episode_nb, title, director, producer, release_date, opening_crawl=None):
        
        """
        Inserts a new movie into the database.

        Args:
            episode_nb (int): The episode number of the movie.
            title (str): The title of the movie.
            director (str): The director of the movie.
            producer (str): The producer of the movie.
            release_date (date): The release date of the movie.
            opening_crawl (str): The opening crawl text of the movie (optional).

        Returns:
            str: A message indicating the success or failure of the operation.
       
        Raises:
            IntegrityError: If the insertion violates a unique constraint.
            Exception: If an error occurs during the insertion
       """
        
        try:
            with transaction.atomic():
                cls.objects.create(
                    episode_nb=episode_nb,
                    title=title,
                    opening_crawl=opening_crawl,
                    director=director,
                    producer=producer,
                    release_date=release_date
                )
            return f"Inserted episode {episode_nb} - Title: '{title}'"
        except Exception as e:
            raise Exception(e)
            

    @classmethod
    def remove(cls, title):
        
        """
        Removes a movie from the database by its title.

        Args:
            title (str): The title of the movie to be removed.

        Returns:
            str: A message indicating the success or failure of the operation.

        Raises:
            Exception: If an error occurs during deletion.
        """
        
        try:
            movie = cls.objects.get(title=title)
            movie.delete()
            return f"Movie '{title}' removed successfully."
        except Exception as e:
            raise Exception(e)