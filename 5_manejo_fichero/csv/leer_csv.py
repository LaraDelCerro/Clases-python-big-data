import csv


def mostrar_datos(ruta, nombre):
    fichero = open(f'{ruta}/{nombre}', 'r', encoding='UTF-8')
    #crear un elemento lector que me va a permitir leer csv
    lector = csv.reader(fichero)
    #si el archivo tiene cabeceras me salto la primera fila, con la fcón next
    next(lector)
    for fila in lector:
        print('-'*20)
        print(f'{fila[0]}: {fila[1]} {fila[2]} - Departamento: {fila[4]}')
    else:
        print('-'*20)
    fichero.close()


mostrar_datos('data', 'empleados.csv')

## crear un funcion que extraiga del csv un lista de empleado
## [ {id:1, nombre: juanan, apellidos: perez, departamento: desarrollo, correo: jj@gmail.com}, {id:1, nombre: juanan, apellidos: perez, departamento: desarrollo, correo: jj@gmail.com} ]

def cargar_datos(ruta, nombre): #crea una lista de diccionarios, un diccionario por cada empleado
    lista_empleados = []
    fichero = open(f'{ruta}/{nombre}', 'r', encoding='UTF-8')
    lector = csv.reader(fichero)
    next(lector) #quito las cabeceras
    for fila in lector:
        empleado = {
            'id': int((fila[0])),
            'nombre' : fila[1],
            'apellidos' : fila[2],
            'correo': fila[3],
            'departamento': fila[4]

        }
        lista_empleados.append(empleado)
    fichero.close()
    return lista_empleados

print(cargar_datos('data', 'empleados.csv'))





def cargar_datos2(ruta, nombre):
    fichero = open(f'{ruta}/{nombre}', 'r', encoding='UTF-8')
    lector = csv.DictReader(fichero) #la fcón DictReader mete todos los registros en un diccionario, identifica tb las cabeceras
    lista_empleados = list(lector)#transformo en lista el cjto de diccionarios que tengo en la vble lector. 
    print(lista_empleados)
    fichero.close()
    
