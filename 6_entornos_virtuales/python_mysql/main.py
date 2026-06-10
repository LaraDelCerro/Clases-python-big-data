import mysql.connector
from mysql.connector import Error

#configurar nuestra conexión. 
DB_CONFIG = {
    'host' : 'localhost',
    'port' : 3306,
    'user': 'root',
    'password': 'larisis5087',
    'database': 'tinta_eterna'
}

#nos conectamos a mySQL
def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
        #con ** pasamos como param a la fcón los valores del diccionario
    except Error as e:
        print(f'Error: {e}')
        return None

#Obtener un listado con todos los libros
def get_all_books():
    try:
        #lo primero es conectarse a la B.D.
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)#abrir un fichero de query, diccionario para conservar las claves
        cursor.execute('select * from libros')
        return cursor.fetchall() #descomprimir los datos que recibimos
    except Error as e:
        print(f'Error: {e}')
        return []
    finally: #finally ocurre siempre
        conn.close() #cerrar la conexión al acabar

#libros = get_all_books()
#print(libros)


#petición de un libro por id
def get_book_by_id(id_libro):
    try:
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select * from libros where id=%s', (id_libro,))
        return cursor.fetchone() #fetchone pq es un elemento 
    except Error as e:
        print(f'Error: {e}')
        return None
    finally: #finally ocurre siempre
        conn.close() #cerrar la conexión

libro_1 = get_book_by_id(1)
print(libro_1)
