import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()


def create_server_connection():
    """Connect to the local MySQL server without selecting a database."""
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
    except Error as error:
        print(f"Unable to connect to MySQL: {error}")
        return None


def create_database(cursor):
    """Create the project database if it does not already exist."""
    cursor.execute("CREATE DATABASE IF NOT EXISTS operations_analytics")
    cursor.execute("USE operations_analytics")


def create_tables(cursor):
    """Create the database tables in the correct dependency order."""
    drop_statements = [
        "DROP TABLE IF EXISTS Sales",
        "DROP TABLE IF EXISTS Distributor",
        "DROP TABLE IF EXISTS Inventory",
        "DROP TABLE IF EXISTS Supplier",
        "DROP TABLE IF EXISTS Wine",
        "DROP TABLE IF EXISTS GrapeVariety",
        "DROP TABLE IF EXISTS Department",
        "DROP TABLE IF EXISTS Employee",
    ]

    for statement in drop_statements:
        cursor.execute(statement)

    table_statements = [
        """
        CREATE TABLE Employee (
            EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
            FirstName VARCHAR(100) NOT NULL,
            LastName VARCHAR(100) NOT NULL,
            Role ENUM(
                'Finance',
                'Marketing',
                'Production',
                'Distribution',
                'Owner'
            ) NOT NULL,
            DepartmentID INT,
            WorkHours INT NOT NULL
        )
        """,
        """
        CREATE TABLE Department (
            DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
            DepartmentName VARCHAR(100) NOT NULL,
            HeadEmployeeID INT
        )
        """,
        """
        CREATE TABLE GrapeVariety (
            GrapeVarietyID INT PRIMARY KEY AUTO_INCREMENT,
            VarietyName VARCHAR(100) NOT NULL
        )
        """,
        """
        CREATE TABLE Wine (
            WineID INT PRIMARY KEY AUTO_INCREMENT,
            WineType ENUM(
                'Merlot',
                'Cabernet',
                'Chablis',
                'Chardonnay'
            ) NOT NULL,
            GrapeVarietyID INT
        )
        """,
        """
        CREATE TABLE Supplier (
            SupplierID INT PRIMARY KEY AUTO_INCREMENT,
            SupplierName VARCHAR(100) NOT NULL,
            DeliveryPerformance DECIMAL(5, 2)
        )
        """,
        """
        CREATE TABLE Inventory (
            InventoryID INT PRIMARY KEY AUTO_INCREMENT,
            ItemType ENUM(
                'Raw Material',
                'Finished Product'
            ) NOT NULL,
            ItemName VARCHAR(100) NOT NULL,
            Quantity INT NOT NULL,
            ResponsibleEmployeeID INT,
            WineID INT
        )
        """,
        """
        CREATE TABLE Distributor (
            DistributorID INT PRIMARY KEY AUTO_INCREMENT,
            DistributorName VARCHAR(100) NOT NULL,
            ContactInformation TEXT,
            EmployeeID INT
        )
        """,
        """
        CREATE TABLE Sales (
            SalesID INT PRIMARY KEY AUTO_INCREMENT,
            WineID INT,
            DistributorID INT,
            SaleDate DATE NOT NULL,
            QuantitySold INT NOT NULL,
            SaleAmount DECIMAL(10, 2) NOT NULL,
            EmployeeID INT
        )
        """,
    ]

    for statement in table_statements:
        cursor.execute(statement)


def insert_sample_data(cursor):
    """Insert sample operational data into the database."""
    departments = [
        ("Finance", 1),
        ("Marketing", 2),
        ("Production", 3),
        ("Distribution", 4),
    ]

    cursor.executemany(
        """
        INSERT INTO Department (DepartmentName, HeadEmployeeID)
        VALUES (%s, %s)
        """,
        departments,
    )

    employees = [
        ("Janet", "Collins", "Finance", 1, 40),
        ("Roz", "Murphy", "Marketing", 2, 60),
        ("Bob", "Ulrich", "Marketing", 2, 60),
        ("Henry", "Doyle", "Production", 3, 46),
        ("Maria", "Costanza", "Distribution", 4, 56),
    ]

    cursor.executemany(
        """
        INSERT INTO Employee
        (FirstName, LastName, Role, DepartmentID, WorkHours)
        VALUES (%s, %s, %s, %s, %s)
        """,
        employees,
    )

    grape_varieties = [
        ("Merlot",),
        ("Cabernet",),
        ("Chablis",),
        ("Chardonnay",),
    ]

    cursor.executemany(
        """
        INSERT INTO GrapeVariety (VarietyName)
        VALUES (%s)
        """,
        grape_varieties,
    )

    wines = [
        ("Merlot", 1),
        ("Cabernet", 2),
        ("Chablis", 3),
        ("Chardonnay", 4),
    ]

    cursor.executemany(
        """
        INSERT INTO Wine (WineType, GrapeVarietyID)
        VALUES (%s, %s)
        """,
        wines,
    )

    suppliers = [
        ("BottlesNCorks", 95.00),
        ("Pack4You", 90.00),
        ("NotHiesenburg", 85.00),
    ]

    cursor.executemany(
        """
        INSERT INTO Supplier (SupplierName, DeliveryPerformance)
        VALUES (%s, %s)
        """,
        suppliers,
    )

    inventory = [
        ("Raw Material", "Bottles", 1000, 1, None),
        ("Raw Material", "Corks", 2000, 1, None),
        ("Finished Product", "Merlot", 500, None, 1),
        ("Finished Product", "Cabernet", 300, None, 2),
    ]

    cursor.executemany(
        """
        INSERT INTO Inventory
        (ItemType, ItemName, Quantity, ResponsibleEmployeeID, WineID)
        VALUES (%s, %s, %s, %s, %s)
        """,
        inventory,
    )

    distributors = [
        ("TwoGlassesDown", "(555) 420-6969", 4),
        ("TwelveFingers", "(555) 326-3825", 4),
    ]

    cursor.executemany(
        """
        INSERT INTO Distributor
        (DistributorName, ContactInformation, EmployeeID)
        VALUES (%s, %s, %s)
        """,
        distributors,
    )

    sales = [
        (1, 1, "2023-01-01", 100, 1000.00, 4),
        (2, 2, "2023-01-02", 150, 1500.00, 4),
        (2, 2, "2023-02-03", 150, 1500.00, 4),
        (4, 2, "2023-02-03", 150, 1500.00, 4),
    ]

    cursor.executemany(
        """
        INSERT INTO Sales
        (WineID, DistributorID, SaleDate, QuantitySold, SaleAmount, EmployeeID)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        sales,
    )


def initialize_database():
    """Create the database, build the schema, and insert sample data."""
    connection = create_server_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        create_database(cursor)
        create_tables(cursor)
        insert_sample_data(cursor)

        connection.commit()
        print("Database successfully created and populated.")
        return True

    except Error as error:
        connection.rollback()
        print(f"Database setup failed: {error}")
        return False

    finally:
        if cursor is not None:
            cursor.close()

        if connection.is_connected():
            connection.close()


if __name__ == "__main__":
    initialize_database()