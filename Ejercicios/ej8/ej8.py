import csv

def cargar_fichero(carpeta, nombre):
    fichero = open(f'./{carpeta}/{nombre}', 'r', encoding='UTF-8')
    lector = csv.DictReader(fichero) #tengo la info tipo csv pero no python no es capaz de leerlo.
    lista = list(lector)
    fichero.close()
    return lista #devuelve una lista de diccionarios, todos los campos son tipo str. 
    #print (lista) #aquí veo cómo lo devuelve
   


def mostrar_bbdd(juegos, stock):
    for game in juegos:
        if game['en_stock'] == str(stock): #string porque el parámetro que meto es un nº pero los que tengo en juegos son tipo string
            print('='*50)
            print(f'{game['titulo']} - {game['genero']} => precio: {game['precio']} - {game['lanzamiento']}')


def crear_fichero(carpeta, nombre, datos):
    fichero = open(f'./{carpeta}/{nombre}', 'w', encoding='UTF-8')
    cabeceras = []
    for key in datos[0].keys():
        cabeceras.append(key)
    mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras)
    #escribir el documento físico y guardarlo localmente
    mi_csv.writeheader()
    mi_csv.writerows(datos)
    fichero.close()


def aplicar_descuento(datos, descuento):
    for game in datos:
        resultado =str( round(float(game['precio']) * (1-descuento/100),2))
        game['precio_descuento'] = resultado
    return datos


def valor_maximo(datos):
    juego_precio_maximo = {}
    maximo = 0
    for game in datos:
        if float(game['precio']) > maximo:
            maximo = float(game['precio'])
            juego_precio_maximo = game
    print (juego_precio_maximo)


def calcular_precio_max_min(datos, tipo):
    valor_busqueda = float(datos[0]['precio'])
    juego_buscado = datos[0]
    for game in datos:
            if float(game['precio']) > valor_busqueda and tipo == 'max':
                valor_busqueda = float(game['precio'])
            elif float(game['precio']) < valor_busqueda and tipo == 'min':
                valor_busqueda = float(game['precio'])
                juego_buscado = game
    if tipo != 'max' and tipo != 'min':
        print('El tipo no es apto')
    else:
        print(f' El juego de precio {tipo} es {juego_buscado}')





juegos = cargar_fichero('data', 'game.csv')
#mostrar_bbdd(juegos, 1) #si meto 1 da los que están es stock. Si meto 0 da los que no.
#crear_fichero('data', 'juego.csv', juegos)#esto me crearía otro archivo llamado juego.csv idéntico a game.csv
#vamos a usar la fcón crear_fichero para crear los ficheros que queramos, juego rebajados por ejemplo

juegos_20 = aplicar_descuento(juegos, 20)
crear_fichero('data', 'rebajas.csv', juegos_20)
valor_maximo(juegos)
calcular_precio_max_min(juegos, 'max')