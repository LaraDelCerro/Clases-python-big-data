from db.config import get_connection
from mysql.connector import Error
#Visualizar datos de forma fácil con pandas
import pandas as pd
from colorama import init, Fore, Style
from tabulate import tabulate

#inicializar colorama
init(autoreset=True)

def get_compra():
    try:
        #crear la conexión
        conn = get_connection()
        #abrimos el fichero sql para hacer la consulta sql
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select * from productos')
        return cursor.fetchall()
    except Error as e:
        print(f'Error {e}')
    finally:
        conn.close()

def aplicar_color(prioridad):
    prioridad = prioridad.lower()
    if prioridad == 'alta':
        return f'{Fore.RED}{prioridad}{Style.RESET_ALL}' #pinta de rojo solo la prioridad
    elif prioridad == 'media':
        return f'{Fore.YELLOW}{prioridad}{Style.RESET_ALL}'
    elif prioridad == 'baja':
        return f'{Fore.GREEN}{prioridad}{Style.RESET_ALL}'
    return prioridad

def pintar_compra(lista):
    if not lista or len(lista) == 0:
        print('No necesitamos nada. Lista vacía.')
    df = pd.DataFrame(lista) 

    #voy a aplicar solo a la columna prioridad el color según el text almacenado
    if 'prioridad' in df.columns:
        df['prioridad'] = df['prioridad'].apply(aplicar_color) #la fcón apply aplica la fcón aplicar_color a cada elemento de df
    # añadir directamente a mi df una columna nueva
    df['precio_total'] = df['precio'] * df['cantidad'] * 1.21 #precio total con IVA

    print('-' * 30)
    print('# Lista Productos #')
    print(tabulate(df,headers='keys', showindex=False)) #tabulamos para que queden centrados los datos, ponemos cabeceras, quitamos la posición del df que genera pandas
    print('-' * 30)


def eliminar_articulo(id): #consulta a base de datos
    try:
        # lo primero obtener la conexión
        conn = get_connection()
        #abrir sql file para hacer la consulta
        cursor = conn.cursor() #no hay que poner diccionario porque no queremos devolver nada
        cursor.execute('delete from productos where id =%s', (id,))
        conn.commit() #para las consultas que no son select
        if cursor.rowcount > 0: #alguna fila ha sido afectada por la consulta
            return f'El producto con id {id} ha sido eliminado'
        return 'No se ha podido eliminar el producto, id no encontrado'


    except Error as e:
        print(f'Error {e}')
    finally:
        conn.close()


def insertar_articulo(producto_tupla):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('insert into productos (nombre, precio, cantidad, prioridad) values (%s, %s, %s, %s)', producto_tupla)
        conn.commit()
        return 'Producto insertado correctamente'

    except Error as es:
        print(f'Error {e}')
    finally:
        conn.close()


def filtrar_prioridad(prioridad):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)  
        cursor.execute('select * from productos where prioridad =%s order by precio desc', (prioridad,))
        return cursor.fetchall()
    except Error as e:
        print(f'Error: {e}')
    finally:
        conn.close()