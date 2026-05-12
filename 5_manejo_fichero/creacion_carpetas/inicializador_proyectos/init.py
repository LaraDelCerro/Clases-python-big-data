
import os

def init():
    try:
        #paso 1: crear la carpeta del proyecto
        os.makedirs('proyecto', exist_ok=True)
        #paso 2: crear fichero main.py vacío en la raíz
        fichero = open('./proyecto/main.py', 'w', encoding= 'UTF-8')
        fichero.close()
        #paso 3: crear la carpeta lib para la gestión de módulos
        os.makedirs('./proyecto/lib', exist_ok=True)
        #paso 4: crear la carpeta data para la gestión de datos o ficheros de datos
        os.makedirs('./proyecto/data', exist_ok=True)
        print('### PROYECTO CREADO CORRECTAMENTE ###')
    except:
        print('### HA HABIDO UN PROBLEMA, NO SE HA CREADO EL PROYECTO ###')


init()






