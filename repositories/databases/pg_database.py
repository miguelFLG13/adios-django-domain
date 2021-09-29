import os
import psycopg2

from domain.repositories.database import Database


class PgDatabase(Database):

    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=os.getenv('DATABASE_NAME'),
            host=os.getenv('DATABASE_HOST'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD')
        )
        self.cursor =  self.connection.cursor()
