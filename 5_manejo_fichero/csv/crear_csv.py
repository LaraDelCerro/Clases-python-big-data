lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]

import csv
""""
def crear_csv(lista, nombre, carpeta):
    cabeceras = []
    fichero = open(f'./{carpeta}/{nombre}', 'a', encoding='UTF-8', newline='')
    #saber las cabeceras
    for key in lista[0].keys(): #quiero sacar las cabeceras de cq registro del diccionario, me daría igual ponero 0 que otro nº
        cabeceras.append(key)
    #volcar los datos de la lista en un objeto csv
    mi_csv= csv.DictWriter(fichero, fieldnames=cabeceras) #crea los registros del csv en fcón de las cabeceras
    #imprimir cabeceras en la primera línea
    mi_csv.writeheader()
    #escribir cada fila en el csv
    mi_csv.writerows(lista_empleados)
    #cerramos el fichero
    fichero.close()
"""
    
def crear_csv(lista, nombre, carpeta):
    fichero = open(f"./{carpeta}/{nombre}", 'a', encoding='UTF-8')
    # saber las cabeceras.
    cabeceras = []
    for key in lista[0].keys():
        cabeceras.append(key)
    #volcar los datos de la lista en un objeto csv
    mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras) 
    #imprimir cabeceras en la primera linea
    mi_csv.writeheader()
    # Escribir cada fila en el csv
    mi_csv.writerows(lista_empleados)
    # cerramos el fichero
    fichero.close()
        
crear_csv(lista_empleados, 'trabajadores.csv', 'data')








    


crear_csv(lista_empleados, 'trabajadores.csv', 'data')    