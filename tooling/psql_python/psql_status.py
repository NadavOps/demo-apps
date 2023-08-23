import os
import psycopg2

host = os.environ.get("HOST")
port = os.environ.get("PORT")
user = os.environ.get("USER")
password = os.environ.get("PASS")

try:
    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password
        # dbname=dbname
    )

    print("Connected to the database!")
    connection.close()

except Exception as e:
    print(f"Error: {e}")
