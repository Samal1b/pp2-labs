import psycopg2


def make_connection():
    with psycopg2.connect(
        host="localhost",
        dbname="phonebook",
        user="samalb",
        password="postgres",
        port=5432
    ) as connection:
        return connection
