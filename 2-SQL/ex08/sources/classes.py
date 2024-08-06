import psycopg2
from psycopg2 import sql, errors

from django.conf import settings

class DatabaseManager:
    
    """
    A class to manage operations on the ex08_planets and
    ex08_people tables in the PostgreSQL database.

    Attributes:
        conn: A psycopg2 connection object to the database.
        cursor: A psycopg2 cursor object for executing SQL commands.
        planet_table_name: The name of the table for planet data (ex08_planets).
        people_table_name: The name of the table for people data (ex08_people).
    
    Methods:
        __init__: Initialize the DatabaseManager with a database connection.
        __enter__: Enter the runtime context related to this object.
        __exit__: Exit the runtime context related to this object.
        connect: Establish a connection to the PostgreSQL database.
        disconnect: Close the database connection and cursor.
        planet_init: Initialize the ex08_planets table in the database.
        planet_insert: Insert a new planet record into the ex08_planets table.
        people_init: Initialize the ex08_people table in the database.
        people_insert: Insert a new person record into the ex08_people table.
        people_get: Retrieve characters' names, their homeworld, 
            and the climate of their homeworld.
    """

    def __init__(self):
       
        """
        Initialize the DatabaseManager with a database connection.

        Args:
            conn: A psycopg2 connection object to the database.
        """
        
        self.conn = None
        self.cursor = None
        self.planet_table_name = 'ex08_planets'
        self.people_table_name = 'ex08_people'


    def __enter__(self):
        
        """
        Enter the runtime context related to this object.

        Establishes a connection to the database and returns the DatabaseManager instance.

        Args: None
        
        Returns: None
        """
        
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        """
        Exit the runtime context related to this object.

        Closes the database connection.

        Args:
            exc_type: The exception type.
            exc_val: The exception value.
            exc_tb: The exception traceback.
        
        Returns: None
        """
        
        self.disconnect()

    def connect(self):
        
        """
        Establish a connection to the PostgreSQL database using
        settings from Django's settings module and create a cursor.

        Args: None

        Returns: None

        Raises:
            psycopg2.OperationalError: If the connection to the 
                database cannot be established.
        """
        
        db_settings = settings.DATABASES['default']
        self.conn = psycopg2.connect(
            dbname=db_settings['NAME'],
            user=db_settings['USER'],
            password=db_settings['PASSWORD'],
            host=db_settings['HOST'],
            port=db_settings['PORT'],
        )
        self.cursor = self.conn.cursor()

    def disconnect(self):
        
        """
        Close the database connection and cursor if they are open.
        
        Args: None

        Returns: Non
        """
        
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def planets_init(self):
        """
        Initialize the ex08_planets table in the database.

        Creates the table if it does not already exist.

        Returns: None

        Raises:
            Exception: If there is an error executing the SQL query.
        """
        create_table_query = sql.SQL("""
        CREATE TABLE {} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(64) UNIQUE NOT NULL,
            climate VARCHAR,
            diameter INTEGER,
            orbital_period INTEGER,
            population BIGINT,
            rotation_period INTEGER,
            surface_water REAL,
            terrain VARCHAR(128)
        )
        """).format(sql.Identifier(self.planet_table_name))

        try:
            self.cursor.execute(create_table_query)
            self.conn.commit()
        except errors.DuplicateTable:
            self.conn.rollback()
            raise Exception(f"The table '{self.planet_table_name}' already exists.")
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(e)

    def planets_insert(self, file_path):
       
        """
        Load data into the ex08_planets table using the COPY command.

        Args:
            file_path (str): Path to the CSV file.
        
        Returns:
            None
        
        Raises:
            Exception: If an error occurs while copying data.
        """
        
        try:
            columns = ('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain')
            with open(file_path, 'r', encoding='utf-8') as f:
                self.cursor.copy_from(f, 'ex08_planets', columns=columns, null='NULL', sep='\t')
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(e)

    def people_init(self):
        
        """
        Initialize the ex08_people table in the database.

        Creates the table if it does not already exist. The `homeworld` field 
        is defined as a foreign key that references the `name` field in the 
        ex08_planets table.

        Returns: None

        Raises:
            Exception: If there is an error executing the SQL query.
        """
        
        create_table_query = sql.SQL("""
        CREATE TABLE {} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(64) UNIQUE NOT NULL,
            birth_year VARCHAR(32),
            gender VARCHAR(32),
            eye_color VARCHAR(32),
            hair_color VARCHAR(32),
            height INTEGER,
            mass REAL,
            homeworld VARCHAR(64),
            FOREIGN KEY (homeworld) REFERENCES {} (name)
        )
        """).format(
            sql.Identifier(self.people_table_name),
            sql.Identifier(self.planet_table_name)
        )

        try:
            self.cursor.execute(create_table_query)
            self.conn.commit()
        except errors.DuplicateTable:
            self.conn.rollback()
            raise Exception(f"The table '{self.people_table_name}' already exists.")
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(e)

    def people_insert(self, file_path):
        
        """
        Load data into the ex08_people table using the COPY command.

        Args:
            file_path (str): Path to the CSV file.
        
        Returns:
            None
        
        Raises:
            Exception: If an error occurs while copying data.
        """
        
        try:
            columns = ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld')
            with open(file_path, 'r', encoding='utf-8') as f:
                self.cursor.copy_from(f, 'ex08_people', columns=columns, null='NULL', sep='\t')
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(e)
    
    def people_get(self):
        """
        Retrieve characters' names, their homeworld, and the climate of their homeworld
        where the climate is windy or moderately windy, sorted alphabetically by the character's name.

        Returns:
            list: A list of tuples containing the character names, homeworlds, and climates.

        Raises:
            Exception: If an error occurs while executing the query or fetching the results.
        """
        
        select_query = sql.SQL("""
            SELECT 
                {people_table}.name, 
                {people_table}.homeworld,
                {planets_table}.climate
            FROM 
                {people_table}
            JOIN 
                {planets_table}
            ON 
                {people_table}.homeworld = {planets_table}.name
                WHERE
                    {planets_table}.climate
                    LIKE '%windy%'
            ORDER BY 
                {people_table}.name;
        """).format(
            people_table=sql.Identifier(self.people_table_name),
            planets_table=sql.Identifier(self.planet_table_name)
        )

        try:
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()
            return rows
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(e)

