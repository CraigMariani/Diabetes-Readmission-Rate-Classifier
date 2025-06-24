import pandas as pd
from sqlalchemy import create_engine

# Database connection settings
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_PORT = ''
DB_NAME = 'ClinicalTrials'



# TABLE_NAME = 'admission_source_lookup'
# TABLE_NAME = 'admission_type_lookup'
TABLE_NAME = 'discharge_disposition_lookup'




# CSV_FILE_PATH = 'admission_source_lookup.csv'
# CSV_FILE_PATH = 'admission_type_lookup.csv'
CSV_FILE_PATH = 'discharge_disposition_lookup.csv'

# Create a SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Read CSV into DataFrame
df = pd.read_csv(CSV_FILE_PATH)

# Insert into PostgreSQL table
df.to_sql(TABLE_NAME, engine, if_exists='append', index=False)

print(f"CSV data inserted successfully to {TABLE_NAME}.")
