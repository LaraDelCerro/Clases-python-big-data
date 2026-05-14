#escribir esto en hyper para instalar la libreria pip install openpyxl
from openpyxl import load_workbook #workbook es un libro de excel

#cargar el fichero de excel en nuestro archivo
excel = load_workbook('./data/empleados.xlsx')
#seleccionar la hoja que quiero. Hoja activa
hoja = excel.active #la hoja en la que estoy
#recorrer filas y columnas de la hoja de excel
for fila in hoja.iter_rows(min_row=2, values_only=True): #empieza en la fila 2 pq la 1ª es la cabecera
    #print(fila) #cada fila es una tupla
    for value in fila:
        print(value)

