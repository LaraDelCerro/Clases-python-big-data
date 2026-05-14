import xml.etree.ElementTree as et


lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]

def crear_xml(carpeta, nombre, datos):
    #paso 1: crear el nodo raíz
    nodo_raiz = et.Element('empleados')#crea <empleados></empleados>
    #paso 2: voy a recorrer los datos para extraer la información
    for empleado in datos: #empleado es un diccionario
        #por cada empleado creamos un nodo_hijo dentro de nodo_raiz
        nodo_empleado = et.SubElement(nodo_raiz, 'empleado', id=str(empleado['id'])) #crea <empleado id='1'></empleado>
        for key, value in empleado.items(): #items extrae la clave y los valores
            if key != 'id':
                subelemento = et.SubElement(nodo_empleado, key) #crea nombre, apellidos, correo, departamento para cada empleado, las claves del diccionario
                subelemento.text = str(value) #crea los nombres, apellidos... concretos para cada empleado, los valores del diccionario
    # paso 3: ya tengo todo el contenido dentro del nodo_raiz
    xml = et.ElementTree(nodo_raiz)#para que le ponga la estructura de árbol
    xml.write(f"./{carpeta}/{nombre}", encoding='UTF-8', xml_declaration=True) #xml_declaration=True le pone las cabeceras        





crear_xml('data', 'trabajadores.xml', lista_empleados)

#si en el archivo trabajadores.xml que hemos creado le damos botón dcho dar formato al documento y queda más bonito