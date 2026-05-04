#Un diccionario es un cjto de datos donde se pierde el factor porsición, los vamos a referenciar por claver. Teniendo un cjto clave:valor

alumno = {
    'nombre':'Juan Antonio', 
    'edad':44, 
    'tlf':677788899
}

print(alumno)

print(alumno['nombre']) #Juan Antonio. Obtenemos el valor poniendo su clave asociada

print(alumno.get('edad'))#44 Otra forma de acceder a los datos del diccionario

#Modificar valores
alumno['tlf'] = 64456783
print(alumno)

#Crear claves nuevas
alumno['direccion'] = 'Calle Melancolía'
print(alumno)

#Eliminar claves
alumno.pop('direccion')
print(alumno)

#diccionario complejo
producto = {
    'titulo': 'Portatil HP',
    'precio': 1200,
    'caracteristicas':{
        'ram':16,
        'procesador': 'AMD RYZEN 7',
        'disco': [256, 512]
    },
    'pantalla': ['1920', '1980']
}

#Si quiero acceder a la resolución de pantalla horizontal, 1920
print( producto['pantalla'][0])

#Si quiero acceder a la ram
print(producto['caracteristicas']['ram']) #16

#Quiero ver los discos
print(producto['caracteristicas']['disco'][0])
print(producto['caracteristicas']['disco'][1])
#También puedo verlo con un bucle:
for i in range(len(producto['caracteristicas']['disco'])):
    print(producto['caracteristicas']['disco'][i])



#Para extraer todos los elementos:
for valor in alumno.values():
    print(valor)

print('-'*10)

#Para extraer todas las claves:
for clave in alumno.keys():
    print(clave)

print('-'*10)

#Para extraer todas las claves con sus elementos:
for clave, valor in alumno.items():
    print(f'{clave}:{valor}')

print('-*10')
print(alumno.values()) #diccionario de valores
print(alumno.keys()) #diccionario de claves
print(alumno.items()) #diccionario de items


