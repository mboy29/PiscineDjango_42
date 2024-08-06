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
        insert: Inserts a new planet into the database.
    """

    name = models.CharField(max_length=64, unique=True)
    climate = models.CharField(max_length=255, blank=True, null=True)
    diameter = models.IntegerField(blank=True, null=True)
    orbital_period = models.IntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    rotation_period = models.IntegerField(blank=True, null=True)
    surface_water = models.FloatField(blank=True, null=True)
    terrain = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        """
        Meta class to define the metadata options for the model.

        Attributes:
            db_table (str): The name of the database table that will store the model's records.
            verbose_name_plural (str): The plural name of the model.
        """

        db_table = 'ex09_planets'
        verbose_name_plural = "Planets"

    def __str__(self):

        """
        Method to return the name of the planet as its string representation.

        Args: None

        Returns:
            str: The name of the planet
        """

        return self.name
    
    
    @classmethod
    def insert(cls, **kwargs):

        """
        Inserts a new planet into the database, or updates the existing record.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            tuple: A tuple containing the planet object and a boolean indicating 
                if the object was created.
        
        Raises:
            Exception: If an error occurs during the insertion.
        """

        try:
            if 'name' not in kwargs:
                raise ValueError("Name is required.")
            return cls.objects.update_or_create(
                name=kwargs['name'],
                defaults={
                    'climate': kwargs.get('climate'),
                    'diameter': kwargs.get('diameter'),
                    'orbital_period': kwargs.get('orbital_period'),
                    'population': kwargs.get('population'),
                    'rotation_period': kwargs.get('rotation_period'),
                    'surface_water': kwargs.get('surface_water'),
                    'terrain': kwargs.get('terrain')
                }
            )
        except Exception as e:
            raise ValueError(e)

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
        fetchall: Retrieves all people from the database.
        insert: Inserts a new person into the database.
    """

    name = models.CharField(max_length=64)
    birth_year = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=32, blank=True, null=True)
    eye_color = models.CharField(max_length=32, blank=True, null=True)
    hair_color = models.CharField(max_length=32, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    homeworld = models.ForeignKey(Planets, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        """
        Meta class to define the metadata options for the model.

        Attributes:
            db_table (str): The name of the database table that will store the model's records.
            verbose_name_plural (str): The plural name of the model.
        """

        db_table = 'ex09_people'
        verbose_name_plural = "People"

    def __str__(self):

        """
        Method to return the name of the person as its string representation.

        Args: None

        Returns:
            str: The name of the person
        """

        return self.name
    
    @classmethod
    def fetchall(cls):

        """
        Retrieves the characters' names, their homeworld, and the climate of
        their homeworld where the climate is windy or moderately windy, 
        sorted alphabetically by the homeworld's name.
        
        Args: None

        Returns:
            list: A list of tuples containing the character's name, homeworld,
                and climate. 
        
        Raises:
            Exception: If an error occurs during the insertion.
        """

        try:
            data = cls.objects.filter(
                homeworld__climate__contains='windy'
            ).values_list(
                'name', 'homeworld__name', 'homeworld__climate'
            ).order_by('name')
            return list(data)
        except Exception as e:
            raise Exception(e)

    @classmethod
    def insert(cls, **kwargs):

        """

        Inserts a new person into the database, or updates the existing record.

        Args:
            **kwargs: Arbitrary keyword arguments.
        
        Returns:
            tuple: A tuple containing the person object and a boolean indicating
                if the object was created.
        
        Raises:
            Exception: If an error occurs during the insertion.
        """

        try:
            if 'name' not in kwargs:
                raise ValueError("Name is required.")
            return cls.objects.update_or_create(
                name=kwargs['name'],
                defaults={
                    'birth_year': kwargs.get('birth_year'),
                    'gender': kwargs.get('gender'),
                    'eye_color': kwargs.get('eye_color'),
                    'hair_color': kwargs.get('hair_color'),
                    'height': kwargs.get('height'),
                    'mass': kwargs.get('mass'),
                    'homeworld': kwargs.get('homeworld')
                }
            )
        except Exception as e:
            raise ValueError(e)
