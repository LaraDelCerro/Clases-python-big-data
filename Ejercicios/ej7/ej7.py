# crear un programa en python que me permita hacer una lista de la compra, 
# Un menu con tres opciones
   # [1].Añadir un producto (nombre, cantidad)
   # [2].Mostrar Lista de la compra
   # [3]. Borrar lista
   # [x]. Salir 
   
# trabajamos con modulos separados. modulo principal y secundario

# el fichero se llamará lista_compra.txt

from lib.file_functions import anadir_producto, mostrar_lista, borrar_lista






def main():
    menu = """
##Lista de la compra##
[1] Añadir un producto(nombre, cantidad)
[2] Mostrar lista de la compra
[3] Borrar lista de la compra
[X] Salir
"""
    print(menu)
    option = input('Escoge una opción: ')
    if option == '1':
        print ('Añadir')
        nombre = input('¿Qué producto necesitas?: ').strip() #strip elimina todos los espacios por delante y por detrás
        cantidad = input('¿Cuántas unidades necesitas?: ').strip()
        mensaje= anadir_producto(nombre, cantidad)
        #print(mensaje)
    elif option == '2':
        mensaje = anadir_producto()
        #print(mensaje)
    elif option == '3':
        mensaje = borrar_lista()
        #print(mensaje)
    elif option =='x' or option == 'X':
        print('Hasta pronto')
        return
    else:
        print('Opción no válida')
    print(mensaje)
    main()


main()





   