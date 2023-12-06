import psycopg2
from psycopg2 import sql

def connect_to_database():
    try:
        # Replace the following values with your database information
        db_params = {
            'host': 'localhost',
            'database': 'HEAT_local',
            'user': 'flask_user',
            'password': 'Aperion2023',
            'port': '5432'
        }

        # Establish a connection to the database
        connection = psycopg2.connect(**db_params)

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        print("Connected to the database!")

        # Example: Execute a simple query
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"PostgreSQL database version: {db_version[0]}")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    connect_to_database()
