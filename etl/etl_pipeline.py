import pandas as pd
import psycopg2

# Read cleaned data
df = pd.read_csv("https://etl-project-komal-123.s3.ap-south-1.amazonaws.com/etl_project/cleaned_data.csv")
print("ROWS:", len(df))

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()

# Insert data row by row
from psycopg2.extras import execute_values

data = df.values.tolist()

query = """
INSERT INTO sales (
    InvoiceNo, StockCode, Description, Quantity,
    InvoiceDate, UnitPrice, CustomerID, Country, TotalPrice
) VALUES %s
"""

execute_values(cur, query, data)
conn.commit()


cur.close()
conn.close()

print("Data loaded into PostgreSQL successfully!")