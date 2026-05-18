from openpyxl import Workbook

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]


def crear_excel(carpeta, fichero, datos):
    #crear el libro de excel
    wb = Workbook()
    #seleccionamos la primera hoja
    hoja = wb.active
    hoja.title = 'Trabajadores'

    #extraer de un diccionario cq de mi lista las cabecerasd
    cabeceras =list( datos[0].keys())
    #añado las cabeceras a mi hoja
    hoja.append(cabeceras)

    #recorrer la lista de datos para imprimir en cada fila un dato concreto
    for empleado in datos:
        #para que esto funcione el empleado tiene que tener los datos en el mismo orden que la lista de cabeceras y estar convertido en lista
        #lista_empleado = list(empleado.values())
        lista_empleado = [empleado[clave] for clave in cabeceras]#para cada empleado crea una lista con toda su info
        #print(lista_empleado)
        hoja.append(lista_empleado)#añadimos a la hoja de excel la lista de cada empleado



    wb.save(f'./{carpeta}/{fichero}')#guardar 
   




crar_excel('data', 'trabajadores.xlsx', lista_empleados)