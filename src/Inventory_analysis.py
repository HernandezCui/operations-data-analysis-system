import mysql.connector
import pandas as pd
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()


def create_connection():
    """Create a connection to the Bacchus Winery database."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database="bacchus_winery",
        )
        return connection

    except Error as error:
        print(f"Database connection failed: {error}")
        return None


def generate_inventory_report():
    """Retrieve and display the current inventory report."""

    connection = create_connection()

    if connection is None:
        return

    query = """
    SELECT
        ItemName,
        Quantity,
        ItemType
    FROM Inventory;
    """

    try:
        df = pd.read_sql(query, connection)

        print("\n========== Inventory Status Report ==========\n")
        print(df)

    except Error as error:
        print(f"Unable to generate report: {error}")

    finally:
        connection.close()


if __name__ == "__main__":
    generate_inventory_report()