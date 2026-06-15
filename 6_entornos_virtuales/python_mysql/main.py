import mysql.connector
from mysql.connector import Error
import pandas as pd

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
        #es una desestructuración del diccionario, pasa de 1 vble(el dicc) a 5 vbles
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

#libro_1 = get_book_by_id(1)
#print(libro_1)

# Una fcón que me permita obtener libros de un género determinado
def get_book_by_gender(genero):
    try:
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select * from libros where genero=%s', (genero,))
        return cursor.fetchall() #fetchall porque devolvemos muchos elementos 
    except Error as e:
        print(f'Error: {e}')
        return []
    finally: #finally ocurre siempre
        conn.close() #cerrar la conexión

#libros_genero = get_book_by_gender('realismo magico')
#df = pd.DataFrame(libros_genero)
#print(df)


'''
'''
## sacar un dataframe que muestre libros entre 10 y 20 euros
def get_book_by_price(precio_min, precio_max, tipo):
    if precio_min > precio_max:
        return 'El precio mínimo no puede ser mayor que el máximo'
    orden = 'desc' if tipo == 1 else 'asc'
    try:
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'select * from libros where precio between %s and %s order by precio {orden}', (precio_min,precio_max))
        #return cursor.fetchall() #fetchall porque devolvemos muchos elementos
        print(pd.DataFrame(cursor.fetchall()))
    except Error as e:
        print(f'Error: {e}')
        return []
    finally: #finally ocurre siempre
        conn.close() #cerrar la conexión

#libros_precio = get_book_by_price(10,20,2)

##df = pd.DataFrame(libros_precio)
##print(df)

'''
'''
def get_books_by_price(price_min, price_max, tipo):
    if price_min > price_max:
        return 'El precio minimo no puede ser mayor que el maximo'
    orden = "DESC" if tipo == 1 else "ASC"
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'SELECT * FROM libros WHERE precio BETWEEN %s AND %s ORDER BY precio {orden}', (price_min, price_max))
        return cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()
        
'''
libros_precio_10_20 = get_books_by_price(40, 10, 2)
if type(libros_precio_10_20) is str:
    print(libros_precio_10_20)
elif len(libros_precio_10_20) == 0:
    print('No hay libros en eso precios')
else:
    df = pd.DataFrame(libros_precio_10_20)
    print(df)

'''

## Devolver un dataframe con el título, número de páginas y año de publicación de los libros que estén publicados desde 2000 en adelante y que tengan 300 o más páginas
def get_books_by_year_page(anyo, pag):
    try:
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select titulo, anyo_publicacion, paginas from libros where anyo_publicacion >= %s and paginas >= %s order by anyo_publicacion', (anyo,pag))
        return cursor.fetchall() #fetchone pq es un elemento 
    except Error as e:
        print(f'Error: {e}')
        return []
    finally: #finally ocurre siempre
        conn.close() #cerrar la conexión

#libros= get_books_by_year_page(2000,300)
#df = pd.DataFrame(libros)
#print(df)

## Top 5 libros más vendidos por número de compras. Sacar el título y el género
def get_top_compras(top):
    try:
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
                    select l.titulo, l.genero, count(c.id) as ventas 
                    from libros l 
                    inner join compras c on c.libro_id = l.id 
                    group by c.libro_id 
                    order by ventas desc, l.id desc 
                    limit %s''', (top,))
        return cursor.fetchall() #fetchone pq es un elemento 
    except Error as e:
        print(f'Error: {e}')
        return []
    finally: #finally ocurre siempre
        conn.close() #cerrar la conexión

#libros= get_top_compras(5)
#df = pd.DataFrame(libros)
#print(df)

## Borrado de una compra
def delete_compra_by_id(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()#no pongo diccionario pq no devuelvo un objeto diccionario
        cursor.execute('delete from compras where id = %s', (id,))
        conn.commit() #commit es el botón de aply del mySQL. Todas las consultas que no sean select terminan con commit
        ## opcional
        return 'La compra se ha borrado correctamente' if cursor.rowcount > 0 else 'No se ha podido borrar la compra. Inténtalo de nuevo'
    except Error as e:
        print(f'Error: {e}')
        return False #si hay un error no quiero retornar nada pq no busco nada
    finally:
        conn.close()

#result = delete_compra_by_id(15)
#print(result)



## Inserción de un libro en la tabla libros
def insert_book(book):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute ("""insert 
                       into libros(
                       titulo, 
                       anyo_publicacion, 
                       isbn, 
                       genero, 
                       idioma, 
                       paginas, 
                       precio, 
                       editorial_id) 
                       values
                       (%s, %s, %s,%s,%s,%s,%s,%s)""",(
                           book['titulo'],
                           book['anyo_publicacion'],
                           book['isbn'],
                           book['genero'],
                           book['idioma'],
                           book['paginas'],
                           book['precio'],
                           book['editorial_id']
                            )
                        )
        conn.commit()
        #para sacar el libro que acabo de insertar necesito el id para consultar por get_by_id
        last_id= cursor.lastrowid #te da el último id
        result = get_book_by_id(last_id)
        return result

    except Error as e:
        print(f'Error: {e}')
        return None
    finally:
        conn.close() 

new_book = {
    'titulo': 'Los renglones torcidos de dios',
    'anyo_publicacion': 1990,
    'isbn': "978-8426354648",
    'genero': 'Drama',
    'idioma': 'Español',
    'paginas': 125,
    'precio': 10,
    'editorial_id': 2
}

result = insert_book(new_book)
print(result)


## Actualizar los campos de un libro
def update_book(book):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('UPDATE libros SET titulo=%s, anyo_publicacion=%s, isbn=%s, genero=%s, idioma=%s, paginas=%s, precio=%s, editorial_id=%s WHERE id=%s', (
            book['titulo'],
            book['anyo_publicacion'],
            book['isbn'],
            book['genero'],
            book['idioma'],
            book['paginas'],
            book['precio'],
            book['editorial_id'],
            book['id'],
        ))
        conn.commit()
        result = get_book_by_id(book['id'])
        return result
    except Error as e:
        print(f'Error: {e}')
        return None
    finally:
        conn.close()
        

book_update = {
    'id': 41,
    'titulo': 'Los renglones torcidos de dios',
    'anyo_publicacion': 1985,
    'isbn': "978-8426344647",
    'genero': 'Drama',
    'idioma': 'Español',
    'paginas': 250,
    'precio': 15,
    'editorial_id': 1
}

result = update_book(book_update)
print(result)