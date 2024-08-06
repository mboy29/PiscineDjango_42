from django.db import models
from django.utils import timezone

class Planets(models.Model):

    """
    Represent a planet in the database with detailed attributes.

    Attributes:
        name (str): The name of the planet.
        climate (str): The climate of the planet.
        diameter (int): The diameter of the planet.
        orbital_period (int): The orbital period of the planet.
        population (int): The population of the planet.
        surface_water (float): The surface water of the planet.
        terrain (str): The terrain of the planet.
        created (datetime): The date and time the record was created.
        updated (datetime): The date and time the record was last updated.

    Methods:
        __str__: Returns the name of the planet as its string representation.
    """

    name = models.CharField(max_length=64, unique=True)
    climate = models.CharField(max_length=255, blank=True, null=True)
    diameter = models.IntegerField(blank=True, null=True)
    orbital_period = models.IntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    rotation_period = models.IntegerField(blank=True, null=True)
    surface_water = models.FloatField(blank=True, null=True)
    terrain = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:

        """
        Meta class to define the metadata options for the model.

        Attributes:
            db_table (str): The name of the database table that will store the model's records.
            verbose_name_plural (str): The plural name of the model.
        """

        db_table = 'ex10_planets'
        verbose_name_plural = "Planets"

    def __str__(self):

        """
        Method to return the name of the planet as its string representation.

        Args: None

        Returns:
            str: The name of the planet
        """

        return self.name

class People(models.Model):

    """
    Represent a person in the the database with detailed attributes.

    Attributes:
        name (str): The name of the person.
        birth_year (str): The birth year of the person.
        gender (str): The gender of the person.
        eye_color (str): The eye color of the person.
        hair_color (str): The hair color of the person.
        height (int): The height of the person.
        mass (float): The mass of the person.
        homeworld (Planets): The homeworld of the person.
        created (datetime): The date and time the record was created.
        updated (datetime): The date and time the record was last updated.
    
    Methods:
        __str__: Returns the name of the person as its string representation.
    """

    name = models.CharField(max_length=64)
    birth_year = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=32, blank=True, null=True)
    eye_color = models.CharField(max_length=32, blank=True, null=True)
    hair_color = models.CharField(max_length=32, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    homeworld = models.ForeignKey(Planets, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:

        """
        Meta class to define the metadata options for the model.

        Attributes:
            db_table (str): The name of the database table that will store the model's records.
            verbose_name_plural (str): The plural name of the model.
        """

        db_table = 'ex10_people'
        verbose_name_plural = "People"

    def __str__(self):

        """
        Method to return the name of the person as its string representation.

        Args: None

        Returns:
            str: The name of the person
        """

        return self.name

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
        characters: A many-to-many relationship with the People model.

    Methods:
        __str__: Returns the title of the movie as its string representation.
        fetchall: Fetches all the movies from the database depending on the
            given parameters.
    """

    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64, unique=True, null=False)
    opening_crawl = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    characters = models.ManyToManyField(People, related_name='movies')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ex10_movies'
        verbose_name_plural = "Movies"
    
    @classmethod
    def fetchall(cls, **kwargs):
        
        """
        Fetches all the movies from the database where the release date is
        between the minimum and maximum release dates, the character's
        gender correspond to the given gender, the character's homeworld
        diameter is greater than or equal to the given diameter, and the
        results are ordered by the movie.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            QuerySet: A queryset of all the movies in the database.
        """
        
        try:
            min_date = kwargs.get('min_release_date', '')
            max_date = kwargs.get('max_release_date', '')
            diameter = kwargs.get('min_diameter', '')
            gender = kwargs.get('gender', '')

            data = cls.objects.filter(
                release_date__range=(min_date, max_date),
                characters__gender=gender,
                characters__homeworld__diameter__gte=diameter,
            ).values_list(
                'title', 'characters__name', 'characters__gender', 'characters__homeworld__name', 'characters__homeworld__diameter'
            ).order_by('title')
            return list(data)
        except Exception as e:
            raise Exception(e)

       

