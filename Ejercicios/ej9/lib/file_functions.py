from openpyxl import Workbook

def crear_excel(fichero, datos):
    wb = Workbook()#inicializar el libro de excel
    #seleccionamos la primera hoja
    hoja = wb.active
    hoja.title = 'Ventas'

    #extraer de un diccionario cq de mi lista las cabeceras
    cabeceras =list( datos[0].keys())
    cabeceras.append('total')
    #añado las cabeceras a mi hoja
    hoja.append(cabeceras)

    #recorrer la lista de datos para imprimir en cada fila un dato concreto
    for producto in datos:

        producto['total'] = producto['cantidad'] * producto['precio_unitario']
        lista_producto = [producto[clave] for clave in cabeceras]#para cada prducto crea una lista con toda su info
        hoja.append(lista_producto)#añadimos a la hoja de excel la lista de cada empleado


    wb.save(f'./{fichero}')#guardar 
    print('Fichero crado correctamente')
