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

def insertar_contacto(nombre,tfno,contactos):
    nuevo_contacto = {
        'nombre': nombre,
        'tfno' : tfno
    }
    contactos.append(nuevo_contacto)
    

def pintar_contactos(lista):
    for contacto in lista:
        print(f'Nombre: {contacto['nombre']}')
        print('- '*15)
        print(f'Teléfono: {contacto['tfno']}')
        print(' '*15)
        print('*'*15)



def borrar_ultimo_contacto(lista):
    lista = lista












def main():
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
    elif opcion == 'x' or opcion == 'X':
        print('Hasta pronto')
        return 
    else:
        print('Opción no válida')
    main()

main()

#pintar_contactos(contactos)
