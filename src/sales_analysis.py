# Kyle Marlia-Conner
# Steve Stylin
# Ean Masoner
# Cuitlahuac Hernandez
# Mirajo Tesora
# Milestone # 1, 2, 3, 4


import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# MySQL connection configuration
config = {
    'user': 'root',
    'password': 'Bellevue2021',  # Replace with your password
    'host': 'localhost',
    'database': 'bacchus_winery'
}

# Connect to MySQL server
connection = mysql.connector.connect(**config)
query = """
SELECT w.WineType, SUM(s.QuantitySold) AS TotalQuantity, SUM(s.SaleAmount) AS TotalSales
FROM Sales s
JOIN Wine w ON s.WineID = w.WineID
GROUP BY w.WineType;
"""

# Fetch data
df = pd.read_sql(query, connection)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(df['WineType'], df['TotalSales'], color='skyblue')
plt.title('Sales Performance by Wine Type')
plt.xlabel('Wine Type')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_performance_report.png')
plt.show()

# Close the connection
connection.close()
