import sqlite3
import pandas as pd
def extract_data(db_path, query):
    connect_db = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, connect_db)
    connect_db.close()
    return df

db_path = 'movies.sqlite'
query = "SELECT * FROM movies;"
movies_df = extract_data(db_path, query)
print(movies_df.head())

def transform_data(df):
    df = df.dropna()
