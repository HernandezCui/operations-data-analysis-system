import pandas as pd
from mysql.connector import Error

from src.database.db import create_connection


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
        inventory_data = pd.read_sql(query, connection)

        print("\n========== Inventory Status Report ==========\n")
        print(inventory_data.to_string(index=False))

    except Error as error:
        print(f"Unable to generate inventory report: {error}")

    finally:
        if connection.is_connected():
            connection.close()


if __name__ == "__main__":
    generate_inventory_report()