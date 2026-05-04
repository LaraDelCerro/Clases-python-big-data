#Tenemos una lista de diccionarios, productos. Esta es la forma más sencilla de representar una base de datos

productos = [
    {
        'id': 1,
        'titulo': 'Leche desnatada',
        'precio': 0.56,
        'cantidad': 3
    },
    {
        'id': 2,
        'titulo': 'seitán',
        'precio': 3.45,
        'cantidad': 3
    }
]

#pintar todos los productos de la listas
def pintar_productos(lista):
    for producto in lista:
        print('-'*10) 
        print(f'{producto['id']} Producto:{producto['titulo']} Precio: {producto['precio']} Cantidad: {producto["cantidad"]}')

pintar_productos(productos)


#Pedir por pantalla los datos de un producto, insertarlo en el listado de productos.

def insertar_productos(lista):
    titulo = input('Dime el producto que quieres insertar: ')
    precio = float(input('Dime el precio del producto: '))
    cantidad = int(input('Dime la cantidad de producto: '))

    producto_nuevo = {
        'id': len(lista)+1,
        'titulo': titulo,
        'precio': precio,
        'cantidad': cantidad
    }

    productos.append(producto_nuevo)
    pintar_productos(productos)

insertar_productos(productos)
