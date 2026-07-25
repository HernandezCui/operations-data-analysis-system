import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


load_dotenv()


def create_connection(database: str = "operations_analytics"):
    """Create and return a MySQL database connection."""

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=database,
        )

        if connection.is_connected():
            return connection

    except Error as error:
        print(f"Database connection failed: {error}")
        return None