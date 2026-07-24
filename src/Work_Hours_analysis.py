# Kyle Marlia-Conner
# Steve Stylin
# Ean Masoner
# Cuitlahuac Hernandez
# Mirajo Tesora
# Milestone # 1, 2, 3, 4


import mysql.connector
import pandas as pd


# MySQL connection configuration
config = {
    'user': 'root',
    'password': 'Bellevue2021',  
    'host': 'localhost',
    'database': 'bacchus_winery'
}

# Connect to MySQL server
connection = mysql.connector.connect(**config)
query = """
SELECT FirstName, LastName, WorkHours
FROM Employee;
"""

# Fetch data
df = pd.read_sql(query, connection)

# Display the report
print("Employee Work Hours Report")
print(df)

# Close the connection
connection.close()
