from lib.carga import cargar_excel, cargar_csv, cargar_json, cargar_xml
from lib.auditoria import 

horarios = cargar_excel('datos', 'escenarios_horarios.xlsx')
#print(horarios)

artistas = cargar_csv('datos', 'artistas.csv')
#print(artistas)

ventas_entradas = cargar_json('datos', 'ventas_entradas.json')
#print(ventas_entradas)

patrocinadores = cargar_xml('datos', 'patrocinadores.xml')

print(patrocinadores)

#print(len(horarios))
#print(type(horarios))
