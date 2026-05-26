from lib.carga import cargar_excel, cargar_csv, cargar_json, cargar_xml, pintar_info_fichero
from lib.limpieza import limpiar_texto, normalizar_texto, procesar_csv, procesar_excel, procesar_json,procesar_xml, limpiar_valor_numerico, normalizar_fecha, normalizar_categoria
from lib.exportacion import crear_csv, crear_excel
import os

os.makedirs('datos_limpios', exist_ok=True)

horarios = cargar_excel('datos', 'escenarios_horarios.xlsx')
artistas = cargar_csv('datos', 'artistas.csv')
ventas_entradas = cargar_json('datos', 'ventas_entradas.json')
patrocinadores = cargar_xml('datos', 'patrocinadores.xml')


horarios_limpios, auditoria_horarios = procesar_excel(horarios)
artistas_limpios, auditoria_artistas = procesar_csv(artistas)
ventas_entradas_limpios, auditoria_entradas = procesar_json(ventas_entradas)
patrocinadores_limpios, auditoria_patrocinadores = procesar_xml(patrocinadores)

print(auditoria_horarios)
print(auditoria_artistas)
print(auditoria_entradas)
print(auditoria_patrocinadores)



crear_csv(horarios_limpios, 'horarios_limpio.csv', 'datos_limpios')
crear_csv(artistas_limpios, 'artistas_limpios.csv','datos_limpios')
crear_csv(ventas_entradas_limpios, 'venta_entradas_limpios.csv', 'datos_limpios')
crear_csv(patrocinadores_limpios, 'patrocinadores_limpio.csv', 'datos_limpios')



crear_excel(horarios_limpios, 'datos_limpios', 'datos.xlsx', 'horarios')
crear_excel(artistas_limpios, 'datos_limpios', 'datos.xlsx', 'artistas')
crear_excel(ventas_entradas_limpios, 'datos_limpios', 'datos.xlsx', 'venta_entradas')
crear_excel(patrocinadores, 'datos_limpios', 'datos.xlsx', 'patrocinadores')


#print ('Auditoría horarios')













