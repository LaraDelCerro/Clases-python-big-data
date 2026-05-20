#Crear un excel con todos los datos del log, separados por item(fecha, IP, metodo, endpoint, status, resp_time)
#Quiero añadir una columna nueva llamada alerta, 'LENTO' si el tiempo de respuesta es <300 ms, OPTIMO en otro caso. 
from openpyxl import  Workbook
import os

#paso 1: leer el fichero y transformarlo en una lista de datos
#paso 2:crear fichero de excel desde una lista
#paso 3: transformar los datos

def extraer_log(texto):
    valor = texto.split('=')#devuelve un array de dos elementos, la clave y el valor
    return valor[1]




def leer_fichero (carpeta, nombre):
    ruta = f'./{carpeta}/{nombre}'
    mi_fichero = open(ruta, 'r', encoding='UTF-8') # ./ indica que estamos en la misma carpeta que el fichero. Encoding para codificar tildes, exlcamaciones...
    lista = []
    for linea in mi_fichero.readlines():
        #linea = linea.replace('\n', '')
        linea.strip()
        if not linea:
            continue
        partes = linea.split(' ')
        fecha_hora = f'{partes[0]} {partes[1]}'.replace('[', '').replace(']', '')
        ip = extraer_log(partes[2])
        metodo = extraer_log(partes[3])
        end_point= extraer_log(partes[4])
        status = int(extraer_log(partes[5]))
        resp_time =int( extraer_log(partes[6]).replace('ms', '').replace('\n', ''))
        lista.append([fecha_hora,ip,metodo,end_point,status,resp_time])
    mi_fichero.close()
    return lista
    

#datos = leer_fichero('data', 'access_log.txt')


def crear_fichero(carpeta, nombre, datos):
    excel = Workbook()
    hoja = excel.active
    hoja.title = 'Logs de server'
    cabeceras = ['fecha_hora', 'ip', 'metodo', 'end_point', 'status', 'tiempo_respuesta', 'alerta']
    hoja.append(cabeceras)
    for fila in datos:
        hoja.append(fila)
    excel.save(f'./{carpeta}/{nombre}')
    

def modificar_datos(lista, tiempo):
    for item in datos:
        if item[5] > tiempo:
            item.append('lento')
        else:
            item.append('optimo')
    return lista




    
datos = leer_fichero('data', 'access_log.txt')
datos = modificar_datos(datos, 300)
crear_excel('data', 'reporte_log.xlsx', datos)