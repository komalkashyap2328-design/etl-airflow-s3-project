import pandas as pd

# S3 file URL
url = "https://etl-project-komal-123.s3.ap-south-1.amazonaws.com/etl_project/cleaned_data.csv"

# Read data from S3
df = pd.read_csv(url)

# Show first 5 rows
print("DATA LOADED SUCCESSFULLY 🔥")
print(df.head().to_string())