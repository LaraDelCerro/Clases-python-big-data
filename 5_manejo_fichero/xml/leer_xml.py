#hay que instalar la extensión xml format
import xml.etree.ElementTree as et

#cómo leer un archivo en bruto
def leer_xml(carpeta, nombre):
    fichero = et.parse(f'./{carpeta}/{nombre}')
    nodo_raiz = fichero.getroot() #me devuelve el nodo ppal. 

    lista_empleados = []

    for emp in nodo_raiz.findall('empleado'): #findall para poder recorrerlo como un array
        #extraer la información del empleado e insertarla en diccionario empleado
        empleado = {}
        #print(emp.get('id')) #extraemos el atribudo 'id'
        #print(emp.find('nombre').text) #así accedemos a cada campo, nombre en este caso
        empleado = {
            'id' : emp.get('id'),
            'nombre': emp.find('nombre').text,
            'apellidos': emp.find('apellidos').text,
            'correo': emp.find('correo').text,
            'departamento': emp.find('departamento').text,

        }
        lista_empleados.append(empleado)
    return lista_empleados

empleados = leer_xml('data', 'empleados.xml')
print(empleados)

