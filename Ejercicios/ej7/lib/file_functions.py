    
def anadir_producto(nombre, cantidad):
    try:
        if nombre != "" and cantidad != "" and int(cantidad) > 0 :
            fichero = open('./data/lista_compra.txt', 'a', encoding='UTF-8')
            fichero.write(f'{nombre} => cantidad: {cantidad}\n')
            fichero.close()
            return 'Producto añadido correctamente'
        else:
            return 'No se pueden introducir valor vacios o cero'
    except ValueError: #por si metemos en cantidad algo que no es un número
            return 'El valor introducido en cantidad tiene que ser un numero'



def mostrar_lista():
    fichero = open('./data/lista_compra.txt', 'r', encoding='UTF-8')#bandera r porque es solo lectura
    lineas = fichero.readlines()#me devuelve una lista de líneas
    if len(lineas) == 0:
         return 'No hay productos en el carrito'
    for linea in lineas:
        print('-' * 20)
        linea = linea.replace('\n', '')#después de cada línea hay un espacio, aquí lo quitamos
        linea = linea.replace(' =>', ':\n  ')#reemplazamos la flecha por un salto de línea y espacios
        print(linea)
    else:
        print('-'* 20) #cuando acaba el bucle imprime esto debajo del último elemento
    fichero.close()


def borrar_lista():
    fichero = open('./data/lista_compra.txt', 'w', encoding='UTF-8') #la bandera w sobreescribe el fichero en blanco
    fichero.close()
    return 'La lista de la compra está vacía'

     
