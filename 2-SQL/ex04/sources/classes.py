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
        table_name: The name of the table to operate on.
    
    Methods:
        __init__: Initializes the DatabaseManager class.
        __enter__: Enter the runtime context related to this object.
        __exit__: Exit the runtime context related to this object.
        database_connect: Establish a connection to the 
            PostgreSQL database and create a cursor.
        database_disconnect: Close the database connection
            and cursor.
        database_table_movies_create: Create the table if it does not exist.
        database_table_movies_insert: Insert a record into the table.
        database_table_movies_get: Retrieve all records from the table.
        database_table_movies_remove: Remove a record from the table by title.
    """

    def __init__(self, table_name='ex04_movies'):
        
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
        Attempt to create the table in the database. 
        If the table already exists, an error message will be raised.

        Args: None

        Returns: None

        Raises:
            Exception: If the table already exists.
            psycopg2.Error: If there is an error executing the SQL query.
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
            raise Exception(f"The table '{self.table_name}' already exists.")
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(e)

    def database_table_movies_insert(self, episode_nb, title, director, producer, release_date, opening_crawl=None):
        
        """
        Insert a single record into the table.

        Args:
            episode_nb (int): The episode number.
            title (str): The movie title.
            director (str): The movie director.
            producer (str): The movie producer(s).
            release_date (str): The release date in 'YYYY-MM-DD' format.
            opening_crawl (str, optional): The opening crawl text.

        Returns: None

        Raises:
            psycopg2.Error: If there is an error executing the SQL query.
        """
        
        insert_query = sql.SQL("""
        INSERT INTO {} (episode_nb, title, director, producer, release_date, opening_crawl) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """).format(sql.Identifier(self.table_name))

        try:
            self.cursor.execute(insert_query, (episode_nb, title, director, producer, release_date, opening_crawl))
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(e)

    def database_table_movie_delete(self, title):
        
        """
        Remove a record from the table by title.

        Args:
            title (str): The title of the movie to remove.

        Returns: None

        Raises:
            Exception: If an error occurs during the removal process.
        """
        
        delete_query = sql.SQL("DELETE FROM {} WHERE title = %s").format(sql.Identifier(self.table_name))

        try:
            self.cursor.execute(delete_query, (title,))
            if self.cursor.rowcount == 0:
                raise Exception(f"Movie with title '{title}' not found.")
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise Exception(e)


    def database_table_movies_get(self):
        
        """
        Retrieve all records from the table, ordered by the primary key (episode_number).

        Args: None

        Returns:
            list: A list of tuples containing the records from the table, ordered by episode_number.
        
        Raises:
            Exception: If an error occurs while executing the query or fetching the results.
        """
        select_query = sql.SQL("SELECT * FROM {} ORDER BY episode_nb").format(sql.Identifier(self.table_name))

        try:
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()
            return rows
        except psycopg2.Error as e:
            raise Exception(e)