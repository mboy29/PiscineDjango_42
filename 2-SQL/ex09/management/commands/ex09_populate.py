import json, os
from django.conf import settings
from django.core.management.base import BaseCommand

from ex09.models import *
from .sources import *

class Command(BaseCommand):

    """
    Custom Django management command to populate the ex09_people and ex09_planets 
    tables in the PostgreSQL database with data.

    Attributes:
        help (str): A message displayed when running 'python3 manage.py help'.
    
    Methods:
        handle: Populates both the ex09_people and ex09_planets tables in the
            PostgreSQL database with data.
    """

    help = 'Populates both the ex09_people and ex09_planets tables in the PostgreSQL database with data.'

    def handle(self, *args, **kwargs):

        """
        Populates both the ex09_people and ex09_planets tables in the PostgreSQL
        database with data from the ex09_initial_data.json file.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """

        def handle_planets(data):

            """
            Specifically populates the ex09_planets table in the PostgreSQL 
            database.

            Args:
                data (list): A list of dictionaries containing the data for the
                    planets.
            
            Returns:
                dict: A dictionary containing the planet objects, with the primary
                    key as the key and the planet object as the value.
            
            Raises:
                Exception: If an error occurs during the population.
            """

            try:
                print(f"{INFO}[INFO] Populating planets...")
                print(f"----------------------------{NC}")
                planets = {}
                for entry in data:
                    fields = entry.get('fields', {})
                    planet, _ = Planets.insert(
                        name=fields.get('name'),
                        climate=fields.get('climate'),
                        diameter=fields.get('diameter'),
                        orbital_period=fields.get('orbital_period'),
                        population=fields.get('population'),
                        rotation_period=fields.get('rotation_period'),
                        surface_water=fields.get('surface_water'),
                        terrain=fields.get('terrain'),
                    )
                    print(f"- {SUCCESS}Successfully added planet: {planet.name}{NC}", end='                       \r')
                    planets[entry.get('pk')] = planet
                print(f"{SUCCESS}[SUCCESS] Planets handled successfully.\n{NC}")
                return planets
            except Exception as e:
                raise Exception(e)
        
        def handle_people(data, planet_data):
            
            """
            Specifically populates the ex09_people table in the PostgreSQL
            database.

            Args:
                data (list): A list of dictionaries containing the data for the
                    people.
                planet_data (dict): A dictionary containing the planet objects,
                    with the primary key as the key and the planet object as the
                    value.
            
            Returns: None

            Raises:
                Exception: If an error occurs during the population.
            """

            try:
                print(f"{INFO}[INFO] Populating people...")
                print(f"----------------------------{NC}")
                for person_entry in data:
                    person_fields = person_entry.get('fields', {})
                    homeworld_id = person_fields.get('homeworld')
                    homeworld = planet_data.get(homeworld_id) if homeworld_id else None
                    person, _ = People.insert(
                        name=person_fields.get('name'),
                        birth_year=person_fields.get('birth_year'),
                        gender=person_fields.get('gender'),
                        eye_color=person_fields.get('eye_color'),
                        hair_color=person_fields.get('hair_color'),
                        height=person_fields.get('height'),
                        mass=person_fields.get('mass'),
                        homeworld=homeworld,
                    )
                    print(f"- {SUCCESS}Successfully added person: {person.name}{NC}", end='                       \r')
                print(f"{SUCCESS}[SUCCESS] People handled successfully.\n{NC}")
            except Exception as e:
                raise Exception(e)

        

        try:
            file_path = os.path.join(settings.BASE_DIR, 'ex09/data/ex09_initial_data.json')
            data = data_read(file_path)

            planets_data = [entry for entry in data if entry.get('model') == 'ex09.planets']
            people_data = [entry for entry in data if entry.get('model') == 'ex09.people']
            
            handle_people(people_data, handle_planets(planets_data))

            print(f"{SUCCESS}[SUCCESS] All tables populated successfully.{NC}")

        except FileNotFoundError:
            raise FileNotFoundError(f'File {file_path} not found.')
        except Exception as e:
            print(f"{ERROR}[ERROR] {e}{NC}")
