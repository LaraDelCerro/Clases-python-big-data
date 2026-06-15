import pandas as pd

#cómo cargar un fichero json
df_json = pd.read_json('./data/empleados.json')
#pintar el data frame
#print(df_json)
#convertirlo en una lista de diccionarios
#print(df_json.to_dict('records')) #records son los registros




#Cómo cargar un fichero xml
df_xml = pd.read_xml('./data/empleados.xml')
#print(df_xml)
#convertirlo en una lista de diccionarios
#print(df_xml.to_dict('records'))

#Cómo cargar un fichero csv
df_csv = pd.read_csv('./data/empleados.csv')
#print(df_csv)



#Cómo cargar un fichero excel
df_excel = pd.read_excel('./data/empleados.xlsx', sheet_name='Empleados')
print(df_excel)


#Cómo cargar un fichero txt
df_txt = pd.read_csv('./data/notas_python.txt')
print(df_txt)