mapeo_generos = {
    'reggaetón': 'Reggaeton',
    'reggaeton': 'Reggaeton',
    'reguetón': 'Reggaeton',
    'electrónica': 'Electrónica',
    'electronica': 'Electrónica',
    'electrónic': 'Electrónica',
    'hiphop': 'Hip Hop',
    'hip hop': 'Hip Hop',
    'r & b': 'R&B',
    'r&b': 'R&B',
    'rnb': 'R&B',
    'flamenco': 'Flamenco',
    'flameko': 'Flamenco',
    'rokc' : 'Rock',
    'roc':'Rock',
    'cumbia': 'Cumbia',
    'kumbia' :'Cumbia',
    'jazz': 'Jazz',
    'jaz': 'Jazz',
    'salsa':'Salsa',
    'electro': 'Electro',
    'pop': 'Pop',
    'ppo' : 'Pop', 
    'techno': 'Tecno',
    'tekno': 'Tecno',
    'folk': 'Folk',
    'metall': 'Metal',
    'metal': 'Metal',
    'indie': 'Indie',
    'indy': 'Indie',
    'ska': 'Escape'
}

mapeo_paises = {
    'rep. dominicana' : 'República Dominicana',
    'rd': 'República Dominicana',
    'r. dominicana': 'República Dominicana',
    'republica dominicana': 'República Dominicana',
    'portugal': 'Portugal',
    'argentina': 'Argentina',
    'argetina': 'Argentina',
    'chile': 'Chile',
    'france': 'Francia',
    'francia': 'Francia',
    'peru': 'Perú',
    'perú': 'Perú',
    'cuba' : 'Cuba',
    'colombia': 'Colombia',
    'kolombia': 'Colombia',
    'espana': 'España',
    'españa': 'España',
    'uk': 'Reino Unido',
    'r. unido': 'Reino Unido',
    'reino unido': 'Reino Unido',
    'united kingdom':'Reino Unido',
    'us': 'Estados Unidos',
    'ee.uu.' : 'Estados Unidos',
    'estados unidos': 'Estados Unidos',
    'usa': 'Estados Unidos',
    'venezuela': 'Venezuela',
    'italia': 'Italia',
    'brasil' : 'Brasil',
    'brazil': 'Brasil',
    'mexico': 'Méjico',
    'méxico':'Méjico',
    'mejico': 'Méjico' 

    }
   
valores_unicos = set(r['escenario'].lower().strip() for r in datos)

mapeo_escenarios={}

mapeo_tipo_entrada = {}

mapeo_metodo_pago = {}

mapeo_categoria = {}


def limpiar_texto(texto): #elimina espacios al ppo, al final y en medio
    if not texto:
        return 'None'
    texto_limpio = texto.strip()
    texto_limpio = ' '.join(texto.split())
    return texto_limpio

def corregir_tildes(texto):
    correcciones_tildes = {
        "jose":       "José",      "maria":      "María",
        "garcia":     "García",    "gonzalez":   "González",
        "martinez":   "Martínez",  "lopez":      "López",
        "perez":      "Pérez",     "sanchez":    "Sánchez",
        "gomez":      "Gómez",     "fernandez":  "Fernández",
        "rodriguez":  "Rodríguez", "hernandez":  "Hernández",
        "ramirez":    "Ramírez",   "gutierrez":  "Gutiérrez",
        "electronica": "Electrónica"
    }
    palabras = texto.split()
    palabras_con_tildes =[]
    for palabra in palabras:
        clave = correcciones_tildes.get(palabra.lower())
        if clave:
            palabras_con_tildes.append(clave)
        else:
            palabras_con_tildes.append(palabra)
    lista_sin_tildes = ' '.join(palabras_con_tildes) #lo une con un espacio entre cada elemento de la lista
    return (lista_sin_tildes)



def normalizar_texto(texto): 
    if not texto:
        return 'None'
    texto_limpio = limpiar_texto(texto)
    texto_limpio = texto.title()
    texto_limpio = corregir_tildes(texto_limpio)
    return texto_limpio


def limpiar_valor_numerico(valor, tipo):
    try:
        valor_txt = str(valor).strip().replace('€', '').replace('.', '').replace(',', '.')
        if tipo == 'int':
            return int(valor_txt)
        elif tipo == 'float':
            return round(float(valor_txt), 2)
    except ValueError:
        return None
        
def normalizar_fecha(fecha_texto):
    print(f'fecha texto', fecha_texto)
    meses = {
    "enero":1, "febrero":2, "marzo":3, "abril":4,
    "mayo":5, "junio":6, "julio":7, "agosto":8,
    "septiembre":9, "octubre":10, "noviembre":11, "diciembre":12,
    "jan":1, "feb":2, "mar":3, "apr":4, "may":5, "jun":6,
    "jul":7, "aug":8, "sep":9, "oct":10, "nov":11, "dec":12
    }
    if fecha_texto.find('/') and ( len(fecha_texto.split(' / ')[0]) == 1 or len(fecha_texto.split('/')[0]) == 2):
        print('0')
        fecha_partes = fecha_texto.split('/')
        dia = fecha_partes[0]
        mes =  str((fecha_partes[1])).zfill(2)
        anio = fecha_partes[2]
        #return fecha_texto
    
    
    elif '-' in fecha_texto and  len(fecha_texto.split('-')[0]) == 4:
        fecha_trozos = fecha_texto.split('-')
        fecha_trozos.reverse()
        dia = fecha_trozos[0]
        mes = fecha_trozos [1]
        anio = fecha_trozos[2]
        #fecha = '/'.join(fecha_trozos)
        #return fecha
        print('if 1')
    
        # return '/'.join(fecha_texto.split('-').reverse())
    elif ' de ' in fecha_texto:
        fecha_partes = fecha_texto.split(' de ')
        dia=fecha_partes[0]
        mes_letra =fecha_partes[1] #julio
        mes = str(meses[mes_letra]).zfill(2)
        anio=fecha_partes[2]
        #print(f'{dia}/{mes}/{anio}')
        print('if 2')
        
    elif fecha_texto.find(',') and fecha_texto.split(' ')[0].isalpha():
        #mes = fecha_texto.split(' ')[0]
        fecha_partes = fecha_texto.replace(' ', ',').split(',')
        print(fecha_partes)
        dia = fecha_partes[1]
        mes_letra = fecha_partes[0]
        mes = meses[mes_letra]
        anio = fecha_partes[3]
        #print(f'{dia}/{mes}/{anio}')
        print('if 3')

    elif '-' in fecha_texto and ( len(fecha_texto.split('-')[0]) == 1 or len(fecha_texto.split('-')[0]) == 2):
        fecha_partes = fecha_texto.replace('-', '/').split('/')
        dia = fecha_partes[0]
        mes = fecha_partes[1]
        anio = fecha_partes[2]
        #print(f'{dia}/{mes}/{anio}')
        print('if 4')
    
    elif '/' in fecha_texto and len(fecha_texto.split('/')[2]) == 2 and len(fecha_texto.split('/')[1]) == 1:
        fecha_partes = fecha_texto.split('/')
        dia = fecha_partes[0]
        mes =  str((fecha_partes[1])).zfill(2)
        anio = fecha_partes[2]
        print('if 5')


    elif '-' in fecha_texto and fecha_texto.split('-')[1].isalpha():
        fecha_partes = fecha_texto.split('-')
        dia = fecha_partes[0]
        mes_letra = fecha_partes[1]
        mes = meses[mes_letra]
        anio = fecha_partes[2]
        print('if 6')

    else:
        print ('Fecha inválida')

    return (f"{dia}/{mes}/{anio}")
    #return (f"{dia:02d}/{mes:02d}/{anio}")
     
def normalizar_categoria(texto,mapeo_generos):
    categoria_limpia = limpiar_texto(texto)
    for clave, valor in mapeo_generos.items():
        if texto == clave:
            categoria_limpia = valor
    if categoria_limpia == limpiar_texto(texto):
        print ('Valor no reconocido')
    return categoria_limpia

def detectar_fuera_de_rango(valor, minimo, maximo):
    if valor < 0: 
        valor_abs == abs(valor)
    if minimo<= valor_abs <=maximo:
        return True
    else:
        return 'Valor fuera de rango'



def auditar(item,item_limpio):
    diccionario = {}
    for clave in item.keys():
        diccionario[clave]= item[clave] != item_limpio[clave]
    return diccionario
    
def contar_cambios(lista):
    diccionario_cambios = dict.fromkeys(lista[0], 0)
    for item in lista:
        for clave in item.keys():
            if item[clave]:
                if diccionario_cambios[clave]:
                    diccionario_cambios[clave] = diccionario_cambios[clave] + 1
                else:
                    diccionario_cambios[clave] = 1
    print(diccionario_cambios)

def procesar_csv(lista):
    lista_limpia = []
    lista_auditoria = []
    for item in lista: 
        item_limpio = {
           'id_artista': normalizar_texto(item['id_artista']),
            'nombre' : normalizar_texto(item['nombre']),
            'genero_musical': normalizar_categoria(item['genero_musical'], mapeo_generos),
             'pais':normalizar_categoria(item['pais'], mapeo_paises),
             'cache_eur': limpiar_valor_numerico(['cache_eur'],'float'),
             'email_manager':normalizar_texto(item['email_manager']),
             'telefono': item['telefono']
       }
        auditoria = auditar(item, item_limpio)
        lista_auditoria.append(auditoria)
        lista_limpia.append(item_limpio)
        #contar_cambios(lista_auditoria)
    #print(f'Número de textos corregidos: {cambios_textos}')

    valores_unicos= set(r['pais'].lower().strip() for r in lista)
    print(valores_unicos)
    return lista_limpia, lista_auditoria

       
           
def procesar_excel(lista):
    lista_auditoria = []
    lista_limpia = []
    for item in lista:
       item_limpio = {
            'fecha': normalizar_fecha(item['fecha']),
            'escenario' : normalizar_categoria(item['escenario'], mapeo_escenarios),
            'artista': normalizar_texto(item['artista']),
             'hora_inicio':(item['hora_inicio']),
             'hora_fin':item['hora_fin'],
             'soundcheck':normalizar_texto(item['soundcheck']),
             'notas': normalizar_texto(item['notas'])
       }
       auditoria = auditar(item, item_limpio)
       lista_auditoria.append(auditoria)
       lista_limpia.append(item_limpio)
    contar_cambios(lista_auditoria)
    return lista_limpia


def procesar_json(lista):
    lista_limpia = []
    lista_auditoria = []
    for item in lista:
       item_limpio = {
            'id_venta': normalizar_texto(item['id_venta']),
            'nombre_comprador' : normalizar_texto(item['nombre_comprador']),
            'email': normalizar_texto(item['email']),
            'dni':normalizar_texto(item['dni']),
            'tipo_entrada':normalizar_categoria(item['tipo_entrada'], mapeo_tipo_entrada),
            'precio':limpiar_valor_numerico(item['precio'],'float'),
            'fecha_compra': normalizar_fecha(item['fecha_compra']),
            'metodo_pago': normalizar_categoria(item['metodo_pago'], mapeo_metodo_pago)
       }
       auditoria = auditar(item, item_limpio)
       lista_auditoria.append(auditoria)
       lista_limpia.append(item_limpio)
    contar_cambios(lista_auditoria)
    return lista_limpia


def procesar_xml(lista):
    lista_limpia = []
    lista_auditoria = []
    for item in lista:
       item_limpio = {
            'nombre_empresa': normalizar_texto(item['nombre_empresa']),
            'contacto' : normalizar_texto(item['contacto']),
            'email': normalizar_texto(item['email']),
            'importe_patrocinio':(item['importe_patrocinio']),
            'categoria':normalizar_categoria(item['categoria'], mapeo_categoria),
            'fecha_inicio':normalizar_fecha(item['fecha_inicio']),
            'fecha_fin': normalizar_fecha(item['fecha_fin'])
       }
       auditoria = auditar(item, item_limpio)
       lista_auditoria.append(auditoria)
       lista_limpia.append(item_limpio)
    contar_cambios(lista_auditoria)
    return lista_limpia








    
