animales = ['perro', 'gato', 'periquito', 'tortuga', 'conejo']

animales2 = animales 
 
animales[1]='nilo'

print(animales2) #si modifico la lista original, modifico la copia. En las listas se hace paso por referencia, ambas listas quedan "unidas por un hilo"

#para no hacer un paso por referencia tenemos que generar una copia de la lista original:

#método 1: copy()
animales3= animales.copy()
animales[1] = 'nilo'
print(animales)
print (animales2)#igual que animales porque la hemos creado por referencia
print (animales3)#no se le aplican los cambios sobre la lista animales porque es una copia


#método 2: índices [:]

frutas = ['manzana', 'platano', 'pera', 'sandia']

frutas2= frutas #un paso por referencia. Si modifico frutas también modifico frutas2

#romper la referencia
frutas3 = frutas[:] #genera una copia de la lista
frutas[2 = 'naranjas']

print(frutas)
print(frutas2)
print(frutas3)

