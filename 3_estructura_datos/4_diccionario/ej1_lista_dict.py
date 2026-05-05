# quiero un menu cli, 2 opciones insertar contacto y 
# opcion 2: pintar la lista contactos 
#	Juan Antonio : 9876543
#  ----------------------
#  Miguel Angel: 567899
#  ----------------------
#opción 3: borrar el último contacto de la agenda
#opción 4: borrar un contacto por nombre
# crear un lista de contactos vacia.
# contactos = []
# en la opcion 1 inserta contacto pedir los datos de contacto, nombre y telefono. E insertarlo en la lista.
# podremos insertar los contactos que queramos antes de salir

contactos = []

def limpiadora_datos(texto):
    texto = texto.lower() #paso todo a minúscula
    #paso 2: quitar tildes
    lista_vocales_tildes = ['á', 'é', 'í', 'ó', 'ú', 'ü']
    lista_vocales = ['a', 'e', 'i', 'o', 'u', 'u'] #ambas listas deben tener la misma longitud, por eso hay dos 'u'
    for i in range(len(lista_vocales_tildes)): #recorre la lista de tildes y si en el texto hay alguna, la sustituye por la correspondiente sin tilde
        texto = texto.replace(lista_vocales_tildes[i], lista_vocales[i])
    return texto



def insertar_contacto(nombre,tfno,contactos):
    nuevo_contacto = {
        'nombre': limpiadora_datos(nombre), #dejo el nombre en minúsculas y sin tildes para poder borrar luego por nombre. 
        'tfno' : tfno
    }
    contactos.append(nuevo_contacto)
    print(' '*15)
    print('## Contacto añadido correctamente ##')
    

def pintar_contactos(lista):
    for contacto in lista:
        print(' '*15)
        print(f'Nombre: {contacto['nombre']}')
        print('- '*15)
        print(f'Teléfono: {contacto['tfno']}')
        print(' '*15)
        print('*'*15)



def borrar_contacto(lista, nombre=""): #si no pasamos el param nombre, borra el último
    if nombre != "":
        for contacto in lista:
            if contacto['nombre'] == nombre: 
                lista.remove(contacto)
        print(' '*15)
        print(f'## Contacto con nombre {nombre} borrado correctamente ##')

        pass
    else:
        lista.pop() #borramos el último
        print(' '*15)
        print('## Último contacto borrado correctamente ##')







def main():
    print(' '*15)
    menu = """ BIENVENIDO AL MENÚ
    _____________________________________________
    ESCOGE UNA OPCIÓN:
    [1] INSERTAR CONTACTO
    [2] MOSTRAR CONTACTOS
    [3] BORRAR EL ÚLTIMO CONTACTO
    [4] BORRAR UN CONTACTO POR NOMBRE
    [X] SALIR
    """
    print(menu)
    opcion = input('¿Qué opción eliges?: ')
    if opcion == '1':
        nombre = input('Dime el nombre del nuevo contacto: ')
        tfno = input ('Dime el teléfono del nuevo contacto: ')
        insertar_contacto(nombre,tfno,contactos)
    elif opcion == '2':
        pintar_contactos(contactos)
    elif opcion == '3':
        borrar_contacto(contactos) #si no le paso nombre borro el último contacto
    elif opcion == '4':
        nombre = input('Dime el nombre a borrar: ')
        nombre = limpiadora_datos(nombre) #introduzco el nombre limpio para localizarlo luego en el diccionario
        borrar_contacto(contactos, nombre)
    elif opcion == 'x' or opcion == 'X':
        print('Hasta pronto')
        return 
    else:
        print('Opción no válida')
    main()

main()

#pintar_contactos(contactos)
