import psycopg2
from django.conf import settings
from psycopg2 import sql, errors

class DatabaseManager:
    
    """
    Database manager class responsible for connecting
    to the PostgreSQL database, table creation, and
    disconnection.

    Attributes:
        conn: A psycopg2 connection object.
        cursor: A psycopg2 cursor object.
    
    Methods:
        __init__: Initializes the DatabaseManager class.
        __enter__: Enter the runtime context related to this object.
        __exit__: Exit the runtime context related to this object.
        database_connect: Establish a connection to the 
            PostgreSQL database and create a cursor.
        database_disconnect: Close the database connection
            and cursor.
        database_table_movies_create: Create the ex00_movies
            table if it does not exist.
    """

    def __init__(self, table_name='ex00_movies'):
        
        """
        Initializes the DatabaseManager class, setting up the 
        connection and cursor attributes and the table name.

        Args:
            table_name (str): The name of the table to operate on.

        Returns: None
        """
        
        self.conn = None
        self.cursor = None
        self.table_name = table_name

    def __enter__(self):
        
        """
        Enter the runtime context related to this object.
        
        Args: None

        Returns: self
        """
        
        self.database_connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        """
        Exit the runtime context related to this object.
        
        Args:
            exc_type: The exception type.
            exc_val: The exception value.
            exc_tb: The exception traceback.
        
        Returns: None
        """
        
        self.database_disconnect()

    def database_connect(self):
        
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

    def database_disconnect(self):
        
        """
        Close the database connection and cursor if they are open.

        Args: None

        Returns: None
        """
        
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def database_table_movies_create(self):
        
        """
        Attempt to create the 'ex00_movies' table in the database.
        If the table already exists, an error message will be raised.
        The table has the following fields:
            - episode_nb: SERIAL, PRIMARY KEY
            - title: VARCHAR(64), UNIQUE, NOT NULL
            - opening_crawl: TEXT, nullable
            - director: VARCHAR(32), NOT NULL
            - producer: VARCHAR(128), NOT NULL
            - release_date: DATE, NOT NULL

        Args: None

        Returns: None

        Raises:
            psycopg2.errors.DuplicateTable: If the table already exists.
            psycopg2.Error: If there is another error executing 
                the SQL query.
        """
        
        create_table_query = sql.SQL("""
        CREATE TABLE {} (
            episode_nb SERIAL PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        )
        """).format(sql.Identifier(self.table_name))
        try:
            self.cursor.execute(create_table_query)
            self.conn.commit()
        except errors.DuplicateTable:
            self.conn.rollback()
            raise Exception("The table 'ex00_movies' already exists.")
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(f"An error occurred: {e}")
