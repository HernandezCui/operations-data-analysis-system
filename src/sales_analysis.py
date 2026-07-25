import os

import matplotlib.pyplot as plt
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


def generate_sales_report():
    """Generate and display the sales performance report."""

    connection = create_connection()

    if connection is None:
        return

    query = """
    SELECT
        w.WineType,
        SUM(s.QuantitySold) AS TotalQuantitySold,
        SUM(s.SaleAmount) AS TotalSales
    FROM Sales s
    JOIN Wine w
        ON s.WineID = w.WineID
    GROUP BY w.WineType
    ORDER BY TotalSales DESC;
    """

    try:
        dataframe = pd.read_sql(query, connection)

        print("\n========== Sales Performance Report ==========\n")
        print(dataframe.to_string(index=False))

        total_revenue = dataframe["TotalSales"].sum()
        best_seller = dataframe.iloc[0]["WineType"]

        print(f"\nTotal Revenue: ${total_revenue:,.2f}")
        print(f"Best Selling Wine: {best_seller}")

        plt.figure(figsize=(10, 6))
        plt.bar(dataframe["WineType"], dataframe["TotalSales"])

        plt.title("Sales Performance by Wine Type")
        plt.xlabel("Wine Type")
        plt.ylabel("Total Sales ($)")
        plt.xticks(rotation=45)

        plt.tight_layout()

        os.makedirs("../images", exist_ok=True)

        plt.savefig("../images/sales_performance_report.png")

        plt.show()

        print("\nChart saved to images/sales_performance_report.png")

    except Exception as error:
        print(f"Unable to generate sales report: {error}")

    finally:
        if connection.is_connected():
            connection.close()


if __name__ == "__main__":
    generate_sales_report()