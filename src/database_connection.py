import mysql.connector

# Establishing the connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Bellevue2021'
)

cursor = connection.cursor()

# Creating the database
cursor.execute("CREATE DATABASE bacchus_winery;")
cursor.execute("USE bacchus_winery;")

# SQL schema for table creation
sql_schema = [
    "DROP TABLE IF EXISTS Sales;",
    "DROP TABLE IF EXISTS Distributor;",
    "DROP TABLE IF EXISTS Inventory;",
    "DROP TABLE IF EXISTS Supplier;",
    "DROP TABLE IF EXISTS Wine;",
    "DROP TABLE IF EXISTS GrapeVariety;",
    "DROP TABLE IF EXISTS Department;",
    "DROP TABLE IF EXISTS Employee;",
    """
    CREATE TABLE Employee (
        EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(100) NOT NULL,
        LastName VARCHAR(100) NOT NULL,
        Role ENUM('Finance', 'Marketing', 'Production', 'Distribution', 'Owner') NOT NULL,
        DepartmentID INT,
        WorkHours INT
    );
    """,
    """
    CREATE TABLE Department (
        DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
        DepartmentName VARCHAR(100) NOT NULL,
        HeadEmployeeID INT
    );
    """,
    """
    CREATE TABLE GrapeVariety (
        GrapeVarietyID INT PRIMARY KEY AUTO_INCREMENT,
        VarietyName VARCHAR(100) NOT NULL
    );
    """,
    """
    CREATE TABLE Wine (
        WineID INT PRIMARY KEY AUTO_INCREMENT,
        WineType ENUM('Merlot', 'Cabernet', 'Chablis', 'Chardonnay') NOT NULL,
        GrapeVarietyID INT
    );
    """,
    """
    CREATE TABLE Supplier (
        SupplierID INT PRIMARY KEY AUTO_INCREMENT,
        SupplierName VARCHAR(100) NOT NULL,
        DeliveryPerformance DECIMAL(5, 2)
    );
    """,
    """
    CREATE TABLE Inventory (
        InventoryID INT PRIMARY KEY AUTO_INCREMENT,
        ItemType ENUM('Raw Material', 'Finished Product') NOT NULL,
        ItemName VARCHAR(100) NOT NULL,
        Quantity INT NOT NULL,
        ResponsibleEmployeeID INT,
        WineID INT
    );
    """,
    """
    CREATE TABLE Distributor (
        DistributorID INT PRIMARY KEY AUTO_INCREMENT,
        DistributorName VARCHAR(100) NOT NULL,
        ContactInformation TEXT,
        EmployeeID INT
    );
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
    );
    """
]

# Executing the schema
for query in sql_schema:
    cursor.execute(query)

# Inserting data into tables
cursor.execute("INSERT INTO Department (DepartmentName, HeadEmployeeID) VALUES ('Finance', 1);")
cursor.execute("INSERT INTO Department (DepartmentName, HeadEmployeeID) VALUES ('Marketing', 2);")
cursor.execute("INSERT INTO Department (DepartmentName, HeadEmployeeID) VALUES ('Production', 3);")
cursor.execute("INSERT INTO Department (DepartmentName, HeadEmployeeID) VALUES ('Distribution', 4);")

cursor.execute("INSERT INTO Employee (FirstName, LastName, Role, DepartmentID, WorkHours) VALUES ('Janet', 'Collins', 'Finance', 1, 40);")
cursor.execute("INSERT INTO Employee (FirstName, LastName, Role, DepartmentID, WorkHours) VALUES ('Roz', 'Murphy', 'Marketing', 2, 60);")
cursor.execute("INSERT INTO Employee (FirstName, LastName, Role, DepartmentID, WorkHours) VALUES ('Bob', 'Ulrich', 'Marketing', 2, 60);")
cursor.execute("INSERT INTO Employee (FirstName, LastName, Role, DepartmentID, WorkHours) VALUES ('Henry', 'Doyle', 'Production', 3, 46);")
cursor.execute("INSERT INTO Employee (FirstName, LastName, Role, DepartmentID, WorkHours) VALUES ('Maria', 'Costanza', 'Distribution', 4, 56);")

cursor.execute("INSERT INTO GrapeVariety (VarietyName) VALUES ('Merlot');")
cursor.execute("INSERT INTO GrapeVariety (VarietyName) VALUES ('Cabernet');")
cursor.execute("INSERT INTO GrapeVariety (VarietyName) VALUES ('Chablis');")
cursor.execute("INSERT INTO GrapeVariety (VarietyName) VALUES ('Chardonnay');")

cursor.execute("INSERT INTO Wine (WineType, GrapeVarietyID) VALUES ('Merlot', 1);")
cursor.execute("INSERT INTO Wine (WineType, GrapeVarietyID) VALUES ('Cabernet', 2);")
cursor.execute("INSERT INTO Wine (WineType, GrapeVarietyID) VALUES ('Chablis', 3);")
cursor.execute("INSERT INTO Wine (WineType, GrapeVarietyID) VALUES ('Chardonnay', 4);")

cursor.execute("INSERT INTO Supplier (SupplierName, DeliveryPerformance) VALUES ('BottlesNCorks', 95.00);")
cursor.execute("INSERT INTO Supplier (SupplierName, DeliveryPerformance) VALUES ('Pack4You', 90.00);")
cursor.execute("INSERT INTO Supplier (SupplierName, DeliveryPerformance) VALUES ('NotHiesenburg', 85.00);")

cursor.execute("INSERT INTO Inventory (ItemType, ItemName, Quantity, ResponsibleEmployeeID, WineID) VALUES ('Raw Material', 'Bottles', 1000, 1, NULL);")
cursor.execute("INSERT INTO Inventory (ItemType, ItemName, Quantity, ResponsibleEmployeeID, WineID) VALUES ('Raw Material', 'Corks', 2000, 1, NULL);")
cursor.execute("INSERT INTO Inventory (ItemType, ItemName, Quantity, ResponsibleEmployeeID, WineID) VALUES ('Finished Product', 'Merlot', 500, NULL, 1);")
cursor.execute("INSERT INTO Inventory (ItemType, ItemName, Quantity, ResponsibleEmployeeID, WineID) VALUES ('Finished Product', 'Cabernet', 300, NULL, 2);")

cursor.execute("INSERT INTO Distributor (DistributorName, ContactInformation, EmployeeID) VALUES ('TwoGlassesDown', '(555)420-6969', 4);")
cursor.execute("INSERT INTO Distributor (DistributorName, ContactInformation, EmployeeID) VALUES ('TwelveFingers', '(555)326-3825', 4);")

cursor.execute("INSERT INTO Sales (WineID, DistributorID, SaleDate, QuantitySold, SaleAmount, EmployeeID) VALUES (1, 1, '2023-01-01', 100, 1000.00, 4);")
cursor.execute("INSERT INTO Sales (WineID, DistributorID, SaleDate, QuantitySold, SaleAmount, EmployeeID) VALUES (2, 2, '2023-01-02', 150, 1500.00, 4);")
cursor.execute("INSERT INTO Sales (WineID, DistributorID, SaleDate, QuantitySold, SaleAmount, EmployeeID) VALUES (2, 2, '2023-02-03', 150, 1500.00, 4);")
cursor.execute("INSERT INTO Sales (WineID, DistributorID, SaleDate, QuantitySold, SaleAmount, EmployeeID) VALUES (2, 2, '2023-02-03', 150, 1500.00, 4);")
cursor.execute("INSERT INTO Sales (WineID, DistributorID, SaleDate, QuantitySold, SaleAmount, EmployeeID) VALUES (4, 2, '2023-02-03', 150, 1500.00, 4);")
# Committing the changes
connection.commit()

# Closing the connection
cursor.close()
connection.close()

print("Database successfully created.")
