import requests as rq
from colorama import init, Fore
##Consultar a la api del tiempo y devolvernos los datos del tiempo y temperatura de una ciudad cualquiera
init()#para usar colorama

def obtener_temperatura(ciudad):
    url = f'https://wttr.in/{ciudad}?format=j2'
    # la librería requests me permite hacer una petición a cq url
    # una API responde al siguiente patrón: 
    #       VERBO - URL
    #       GET/SELELCT - https://wttr.in/madrid 
    # POST/INSTERT ->CREAR
    #PUT/UPDATE -> ACTUALIZAR
    #DELETE/DELETE -> BORRAR
    respuestaApi = rq.get(url)
    #print(respuestaApi)
    #la respuesta de la API viene comprimida, la descomprimo con .json()
    data = respuestaApi.json()
    #print(data)
    temperatura = data['current_condition'][0]['temp_C']
    humedad = data['current_condition'][0]['humidity']
    descripcion = data['current_condition'][0]['weatherDesc'][0]['value']
    color = Fore.BLUE if float(temperatura)<25 else Fore.RED
    temperatura_color = color + str(temperatura)
    print(f'La tetemperatura de {ciudad.title()} es {temperatura_color}ºC {Fore.RESET}, la humedad es de un {humedad}% y el día en general es {descripcion}')


#pedir por pantalla una ciudad, pasarla a minúscula y ejecutar la fcón

ciudad = input('Dime una ciudad: ').lower()
obtener_temperatura(ciudad)