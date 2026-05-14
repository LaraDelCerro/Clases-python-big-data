import csv

def extraer_ultimo_id(carpeta, nombre):
    fichero = open (f'./{carpeta}/{nombre}', 'r', encoding='UTF-8') #abrimos para leer
    datos = list(csv.DictReader(fichero))
    fichero.close()
    return int(datos[-1]['id']) + 1 






def pedir_datos():
    nombre = input ('Nombre: ')
    apellidos = input('Apellidos: ')
    correo = input('Correo: ')
    dpto = input('Departamento: ')
    return [nombre, apellidos, correo, dpto]





def actualizar_datos(carpeta, nombre):
    try:
        empleado_nuevo = pedir_datos() #empleado nuevo es una lista
        #añadir el siguiente id al nuevo empleado
        empleado_nuevo.insert(0, extraer_ultimo_id(carpeta, nombre)) #inserto el id en la posición 0 de la lista empleado_nuevo
        fichero = open(f'./{carpeta}/{nombre}', 'a', encoding='UTF-8', newline='') #newline = vacío para que no meta una línea en blanco entre una fila y la siguiente
        mi_csv=csv.writer(fichero) #con el método writer lo tratamos como un array de arrays. Con el método DictWriter lo trata como un array de diccionarios 
        mi_csv.writerow(empleado_nuevo) #añade una fila para empleado nuevo
        print('El archivo ha sido actualizado')
        fichero.close()

    except:
        print('No se ha podido actualizar el archivo')


actualizar_datos('data', 'empleados.csv')


