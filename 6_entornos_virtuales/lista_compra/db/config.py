#Este fichero serivirá para crear la conexión a B.D.
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os 

load_dotenv() #cargamos el fichero .env para introducir los datos en el diccionario de abajo

## crear el diccionario de conexión a base de datos. 
DB_CONFIG = {
    'host': os.getenv("MYSQL_LOCALHOST"),
    'port':int(os.getenv("MYSQL_PORT")),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE")
}

def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Error: {e}")
        return None



    
