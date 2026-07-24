import os

import mysql.connector
import pandas as pd
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()


def create_connection():
    """Create a connection to the Bacchus Winery database."""
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database="bacchus_winery",
        )

    except Error as error:
        print(f"Database connection failed: {error}")
        return None


def generate_work_hours_report():
    """Retrieve and display employee work-hour data."""
    connection = create_connection()

    if connection is None:
        return

    query = """
    SELECT
        EmployeeID,
        FirstName,
        LastName,
        Role,
        WorkHours
    FROM Employee
    ORDER BY WorkHours DESC;
    """

    try:
        dataframe = pd.read_sql(query, connection)

        print("\n========== Employee Work Hours Report ==========\n")
        print(dataframe.to_string(index=False))

        average_hours = dataframe["WorkHours"].mean()
        highest_hours = dataframe["WorkHours"].max()

        print(f"\nAverage work hours: {average_hours:.1f}")
        print(f"Highest recorded work hours: {highest_hours}")

    except Exception as error:
        print(f"Unable to generate work-hours report: {error}")

    finally:
        if connection.is_connected():
            connection.close()


if __name__ == "__main__":
    generate_work_hours_report()
