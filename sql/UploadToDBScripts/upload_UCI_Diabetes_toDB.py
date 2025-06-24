import pandas as pd
from sqlalchemy import create_engine

# Database connection settings
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_PORT = ''
DB_NAME = 'ClinicalTrials'
TABLE_NAME = 'uci_diabetes_readmissions'
CSV_FILE_PATH = 'diabetic_data.csv'

# Create a SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Read CSV into DataFrame
df = pd.read_csv(CSV_FILE_PATH)

# Insert into PostgreSQL table
df.to_sql(TABLE_NAME, engine, if_exists='append', index=False)

print(f"CSV data inserted successfully to {TABLE_NAME}.")
