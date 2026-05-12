import os #librería de python para acceder al sistema operativo

def crear_archivo(carpeta, nombre, extension):
    ##en os hay una funcion que me permite crear directorios.
    os.makedirs(carpeta, exist_ok=True) # con el 2º parámetro solo crea la carpeta si no existe.
    fichero = open(f"./{carpeta}/{nombre}.{extension}", "w", encoding="UTF-8")
    fichero.write('algo')
    fichero.close()
    
    
crear_archivo('data', 'prueba', 'txt') #crea una carpeta data y dentro de ella el archivo prueba.txt