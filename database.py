import sqlite3
from sqlite3 import Error

table_name = input('введите название таблицы: ')


# Constant
PATH = 'testdb.db'


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(PATH)
        print('Try to connect to db')
    except Error as e:
        print('Can`t connected. Error:', e)
    else:
        print("Success")

    return connection

def query_create_table(connection):
    cursor = connection.cursor()
    query_create = '''
        CREATE TABLE table_name (
        id INTEGER NOT NULL PRIMARY KEY,
        email TEXT NOT NULL UNIQUE,
        date DATETIME,
        salary REAL NOT NULL); '''

    cursor.execute(query_create)
    connection.commit()
    print('Table was created')
    cursor.close()

conn = create_connection()
query_create_table(conn)