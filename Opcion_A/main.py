from lib.carga import cargar_excel, cargar_csv, cargar_json, cargar_xml, pintar_info_fichero
from lib.limpieza import  procesar_csv, procesar_excel, procesar_json,procesar_xml
from lib.exportacion import crear_csv, crear_excel
from lib.auditoria import mostrar_auditoria
import os


os.makedirs('datos_limpios', exist_ok=True) #crea la carpeta datos_limpios en caso de que no exista

## CARGA DE LOS FICHEROS ##

horarios = cargar_excel('datos', 'escenarios_horarios.xlsx')
artistas = cargar_csv('datos', 'artistas.csv')
ventas_entradas = cargar_json('datos', 'ventas_entradas.json')
patrocinadores = cargar_xml('datos', 'patrocinadores.xml')

## MOSTRAR INFO DE LOS FICHEROS ##

pintar_info_fichero(horarios, 'escenarios_horarios.xlsx', 5)
pintar_info_fichero(artistas, 'artistas.csv', 5)
pintar_info_fichero(ventas_entradas, 'ventas_entradas.json', 5)
pintar_info_fichero(patrocinadores, 'patrocinadores.xml', 5)

## LIMPIEZA DE LOS DATOS ##

horarios_limpios, auditoria_horarios = procesar_excel(horarios)
artistas_limpios, auditoria_artistas = procesar_csv(artistas)
ventas_entradas_limpios, auditoria_entradas = procesar_json(ventas_entradas)
patrocinadores_limpios, auditoria_patrocinadores = procesar_xml(patrocinadores)



##  CREACIÓN DE 4 CSV'S EN LA CARPETA DATOS LIMPIOS ##

crear_csv(horarios_limpios, 'horarios_limpio.csv', 'datos_limpios')
crear_csv(artistas_limpios, 'artistas_limpios.csv','datos_limpios')
crear_csv(ventas_entradas_limpios, 'venta_entradas_limpios.csv', 'datos_limpios')
crear_csv(patrocinadores_limpios, 'patrocinadores_limpio.csv', 'datos_limpios')


## CREACIÓN DE UN EXCEL CON UN FICHERO LIMPIO EN CADA HOJA ##

crear_excel(horarios_limpios, 'datos_limpios', 'datos.xlsx', 'horarios')
crear_excel(artistas_limpios, 'datos_limpios', 'datos.xlsx', 'artistas')
crear_excel(ventas_entradas_limpios, 'datos_limpios', 'datos.xlsx', 'venta_entradas')
crear_excel(patrocinadores, 'datos_limpios', 'datos.xlsx', 'patrocinadores')




## AUDITORÍA DE LOS FICHEROS ##

mostrar_auditoria('escenarios_horarios.xlsx', auditoria_horarios)
mostrar_auditoria('artistas.csv', auditoria_artistas)
mostrar_auditoria('ventas_entradas.json', auditoria_entradas)
mostrar_auditoria('patrocinadores.xml', auditoria_patrocinadores)









