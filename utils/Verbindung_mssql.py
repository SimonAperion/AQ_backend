import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

HOST = 'localhost\\SQLEXPRESS'
DB = 'Heat_local'
USER = 'flask_user'
PW = 'Aperion2023'
PORT = 1433

# Using the 'mssql+pyodbc' SQLAlchemy engine for SQL Server
#cstring = f"mssql+pyodbc://{USER}:{PW}@{HOST}:{PORT}/{DB}?driver=ODBC+Driver+17+for+SQL+Server"
# If using Windows authentication, you can use the trusted_connection parameter
cstring = f"mssql+pyodbc://{HOST}/{DB}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"

# Create the SQLAlchemy engine
engine = create_engine(cstring)

# Define a test table
metadata = MetaData()
test_table = Table('test_table', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(255)))

# Create the table in the database
metadata.create_all(engine)

# Insert a record into the table
with engine.connect() as connection:
    insert_query = test_table.insert().values(name='Test Record')
    connection.execute(insert_query)


# Retrieve records from the table
with engine.connect() as connection:
    select_query = test_table.select()
    result = connection.execute(select_query).fetchall()
    print(result)

# Display the retrieved records
for row in result:
    print(f"ID: {row['id']}, Name: {row['name']}")
