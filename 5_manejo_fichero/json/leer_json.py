""""
import json

def leer_json(carpeta, nombre):
    try: #esto es extrapolable al resto de ficheros (csv, xml, ... )
        fichero = open(f"./{carpeta}/{nombre}", "r", encoding="UTF-8")
        datos = json.load(fichero)
        return datos
    except FileNotFoundError:
        print('Archivo o carpeta no encontrado')
    
    
lista_trabajadores = leer_json('data', 'trabajadores.json')

for trabajadores in lista_trabajadores:
    print(empleado['nombre'])

"""



import json

def leer_json(carpeta, nombre):
    try:
        fichero = open(f"./{carpeta}/{nombre}", "r", encoding="UTF-8")
        datos = json.load(fichero)
        return datos
    except FileNotFoundError:
        print('Archivo o carpeta no encontrado')
    
    
#lista_empleados = leer_json('data', 'empleados.json')

#for empleado in lista_empleados:
#    print(empleado['nombre'])
