"""
tres acciones para realizar un fichero
open
    r(read) -> leer ficher, extraer datos pero no modificarlos
    w(write) -> sobreescribirlo, es decir lo que tenga se borra y se sutituye por lo que escribo
    a (append) -> añadir, es decir añado algo a lo que ya hay en el fichero

El ciclo de vida de un fichero constra de tres partes:
abrir fichero - realizar las acciones correspondientes (W-R-A) - cerrar el fichero
"""

#Paso 1: dónde está el fichero. Ruta
mi_fichero = open('./texto.txt', 'r', encoding='UTF-8') # ./ indica que estamos en la misma carpeta que el fichero. Encoding para codificar tildes, exlcamaciones...

frases = []

#read() me sirve para leer todo el fichero de golpe, pero no lo puedo manejar
#print(mi_fichero.read())

#readlines() me sirve para crear una lista por cada párrafo del texto
#print(mi_fichero.readlines()) #separa los elementos del array por un \n, que representa el salto del línea
#vamos a coger línea a línea, limpiamos el texto y lo metemos en una lista de frases

for linea in mi_fichero.readlines():
    linea = linea.replace('\n', '')#quitamos el \n
    frases.append(linea)
else:
    print(frases)

# Muy importante cerrar el fichero al terminar

mi_fichero.close()

    
