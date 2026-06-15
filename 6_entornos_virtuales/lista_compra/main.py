
#nos traemos cada una de las fcones que me permitan conectarme con los datos. 
from controllers.consultas__controller import get_compra, pintar_compra, eliminar_articulo, insertar_articulo, filtrar_prioridad

def init():
    menu = """##### Lista de compra #####
    [1]. Añadir artículo
    [2]. Eliminar artículo
    [3]. Ver la lista de la compra
    [4]. Filtrar lista de productos por prioridad
    [x]. Salir
    """
    print(menu)
    option = input('Dime qué opción eliges: ')
    if option == '1':
        try:
            nombre = input('Introduce el nombre del producto: ')
            precio = float(input('Introduce el precio del producto: '))
            cantidad = int(input('Introduce la cantidad: '))
            prioridad = input('Introduce la prioridad (alta, media, baja): ').lower()
            if prioridad not in ('alta','media','baja'): #if prioridad != 'alta' and prioridad !='media' and prioridad !='baja':
                raise Exception ('La prioridad debe ser baja, media o alta')

            #creamos una tupla con todos los valores para insertarlos en la B.D.
            registro = (nombre, precio, cantidad, prioridad)
            result = insertar_articulo(registro)
            print(result)
        except ValueError: #controlar que precio y cantidad sean números para aplicarles float e int respectivamente
            print('Precio y cantidad tienen que ser números')
            print(' ')
        except Exception as e:
            print(f'Error: {e}')
            print(' ')
    elif option == '2':
        id = input('Dame el id del artículo a eliminar: ')
        result = eliminar_articulo(int(id))
        print(result)
    elif option == '3':
        result = get_compra()
        pintar_compra(result)
    elif option == '4':
        try:
            prioridad = input('Por qué valor de prioridad quieres filtrar (alta, media, baja): ').lower()
            if prioridad not in ('alta','media','baja'): 
                    raise Exception ('La prioridad debe ser baja, media o alta')
            result = filtrar_prioridad(prioridad)
            if result and len(result) > 0:
                pintar_compra(result)
            else:
                print('No hay resultados en esta búsqueda')
        except Exception as e:
            print(f'Error: {e}')
            print(' ')
    elif option.lower() == 'x':
        print('Hasta pronto.')
        return False # me saca del menú
    else:
        print('No es una opción válida. ')
    init()





if __name__=='__main__':
    init()