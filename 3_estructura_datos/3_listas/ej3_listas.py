lista_productos = [('laptop', 1200), ('raton', 39), ('ram', 200), ('teclado', 10)]

print(lista_productos[1][1]) # 39
print(lista_productos[3][0]) #teclado

lista_ordenada = sorted(lista_productos) #ordena por orden alfabético decreciente del primer elemento de la tupla

#para acceder a otro elemento de la tupla que no sea el 1º es necesario la fcón lambda
lista_ordenada = sorted (lista_productos, key=lambda producto: producto[1]) # ordena el precio de menor a mayor
print(lista_ordenada)

lista_ordenada = sorted (lista_productos, key=lambda producto: producto[1], reverse=True) # ordena el precio de mayor a menor
print(lista_ordenada)


# ordena a los alumnos por altura del más alto al más bajo
alumnos = [('Carlos', 34, 180), ('Lucia', 24, 165), ('Raul', 18, 190), ('Berta', 24, 172)]

lista_ordenada = sorted(alumnos, key= lambda alumno: alumno[2], reverse=True)
print (lista_ordenada)