from lib.carga import cargar_excel, cargar_csv, cargar_json, cargar_xml, pintar_info_fichero
from lib.limpieza import limpiar_texto, normalizar_texto, procesar_csv, procesar_excel, procesar_json,procesar_xml, limpiar_valor_numerico

horarios = cargar_excel('datos', 'escenarios_horarios.xlsx')
#print(horarios)

artistas = cargar_csv('datos', 'artistas.csv')
#print(artistas)

ventas_entradas = cargar_json('datos', 'ventas_entradas.json')
#print(ventas_entradas)

patrocinadores = cargar_xml('datos', 'patrocinadores.xml')

#print(patrocinadores)

#print(len(horarios))
#print(type(horarios))


#print(normalizar_texto('  Juan garcia                lopez   '))



#cabeceras =list(horarios[0].keys())
#print(cabeceras)

#pintar_info_fichero(horarios, 'escenarios_horarios.xlsx', 5)
#pintar_info_fichero(artistas, 'artistas.csv', 5)
#pintar_info_fichero(ventas_entradas, 'ventas_entradas.json', 5)
#pintar_info_fichero(patrocinadores, 'patrocinadores.xml', 5)

artistas_limpio = procesar_csv(artistas)
#print(artistas_limpio)

#horarios_limpio = procesar_excel(horarios)
#print(horarios_limpio)

#ventas_entradas_limpio = procesar_json(ventas_entradas)
#print(ventas_entradas_limpio)

#patrocinadores_limpio = procesar_xml(patrocinadores)
#print(patrocinadores_limpio)


