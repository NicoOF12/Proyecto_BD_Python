# main.py

import mysql.connector
from mysql.connector import Error

# Configuración de la base de datos MySQL
mysql_config = {
    'host': '',  # Dirección IP del servidor MySQL
    'port': 3300,             # Puerto de conexión a MySQL
    'user': 'root',           # Usuario de la base de datos
    'password': '',       # Contraseña del usuario
    'database': 'db_hospitales'  # Nombre de la base de datos a usar
}

def get_connection():
    """
    Establece una conexión con la base de datos MySQL usando la configuración definida en mysql_config.

    Returns:
        mysql.connector.connection.MySQLConnection | None: 
        Retorna un objeto de conexión a la base de datos si la conexión es exitosa,
        de lo contrario, retorna None e imprime el error en la consola.
    """
    try:
        connection = mysql.connector.connect(**mysql_config)
        return connection
    except Error as e:
        print(f"Error durante la conexión: {e}")
        return None

