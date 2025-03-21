# main.py
import mysql.connector
from mysql.connector import Error

mysql_config = {
    'host': '192.168.80.21',
    'port': 3300,
    'user': 'root',
    'password': '1234',
    'database': 'db_hospitales'
}

def get_connection():
    try:
        connection = mysql.connector.connect(**mysql_config)
        return connection
    except Error as e:
        print(f"Error during connection: {e}")
        return None
