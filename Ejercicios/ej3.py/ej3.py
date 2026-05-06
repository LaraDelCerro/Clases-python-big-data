## Construir un programa que dé por pantalla tres opciones
#      - 1 añadir un contacto a lista
#      - 2 leer todos los contactos de la lista
#      - 3 salir

# Si no pulso salir no me debe sacar de la aplicacion dandome opcion a elegir nuevamente cada vez que se termine mi eleccion anterior.

# lista_contactos sera un lista de diccionarios donde cada elemento tendrá los siguentes datos. Nombre, telefono, email

# Añadir un contacto deberá pedir esos datos y comprobar que nombre no es vacio, que telefono esta formado por digitos,y que el email estan bien escrito, al menos tiene que tener @. Si esto ocurre añadimos el contacto si no lanzamos un error y volvemos al menu principal 

# Leer contacto mostrara todos los contactos por pantalla


#Vamos a importar las funciones que necesitamos desde el fichero functions

#opción 1: Importar todo el fichero functions
import lib.functions as fn # importamos y le ponemos un alias (fn) para que sea más sencillo llamarlo
#La pega de esta opción es que importa todo el fichero, que puede ser muy pesado, la usamos cuando vamos a utilizar todas las fcones que haya en el fichero

#opción2: Importar solo las fcones que necesitamos
from lib.functions import insertar_contacto, validar_contacto, pintar_contactos


agenda = []

def main():
    menu=""" ### DIRECTORIO DE CONTACTOS ###
[1] Añadir un contacto a la lista de contactos
[2] Leer todos los contactos de la lista
[X] Salir
############################
"""
    print(menu)
    option = input('Escoge qué opción quieres: ')
    if option == '1':
        nombre = input('Introduce tu nombre: ')
        email = input('Introduce tu email: ')
        telefono = input('Introduce tu telefono: ')
        print(' '*15)
        #fn.insertar_contacto(nombre, email, telefono, agenda)  importación tipo 1
        es_valido = validar_contacto(nombre, email, telefono)
        if es_valido:
            insertar_contacto(nombre, email, telefono, agenda)
        else:
            print('Los datos introducidos no son correctos, prueba otra vez')
            print(' '*15)
    elif option == '2':
        pintar_contactos(agenda)
    elif option == 'x' or option == 'X':
        print ('hasta pronto')
        return
    else:
        print ('opción no válida')
    print(' '*15)
    main()

main()
