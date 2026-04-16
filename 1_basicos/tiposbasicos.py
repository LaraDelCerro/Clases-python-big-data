nombre_alumno = "Lara del Cerro"
print (nombre_alumno)
print(type(nombre_alumno)) #imprime el tipo de vble 
print("____________")
nombre_alumno = 21
print(nombre_alumno)
print(type(nombre_alumno))

#Tipos básicos en Python

#1. Numéricos

edad= 34
precio = 1299.35

#2. Booleano

estado = True
activo = False

#3. Cadena de caracteres - string

nombre = "Irene"
apellidos = 'Martínez'
mensaje = 'El niño dijo: "¿Qué pasa?"'
print(mensaje)

nombre_completo =  nombre + " " + apellidos + ": " + str(edad)
print (nombre_completo)

nombre_completo2 = f'{nombre} {apellidos}: {edad}' #otra manera más ágil para concatenar strings
print(nombre_completo2)

texto_largo = """
Selecciona una opción:
[1] Sopa
[2] Puré de calabaza
[3] Gazpacho 

"""

opcion = input(texto_largo)
print ( f'La opción es {opcion}' )
