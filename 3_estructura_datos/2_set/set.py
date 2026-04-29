#Un set es un cjto ordenado de elementos ÚNICOS. Se utiliza para eliminar elementos duplicados de un cjto. 

#esto es una lista, no un set
lista = [1,1,1,2,2,2,2,2,3,3,3,4,4,5,5,5,5,5,5,3,6,7,5,9]
mi_set = set(lista) #transformo la lista en set
print('lista original', lista)
print('------------------------------------')
print ('conjunto final', mi_set)
print('lista no duplicados', list(mi_set)) #transformo el cjnto de nuevo en lista

#en un cjto de elementos o set el orden es aleatorio, esto complica un poco el manejo  por posición. No se puede recorrer

frutas = {'Manzana', 'Naranja', 'Pera', 'Plátano', 'Pera', 'Manzana'} 

print(frutas) #el orden es aleatorio, cada vez que lo ejecutas la posición cambia, pero elimina los duplicados

#agregar elementos
frutas.add('Melón') #no puede añadirse más de un elemento a la vez
frutas.add('Pera') #al añadir un elemento que ya existe, no da error pero no lo añade

#borrar elementos de un set 
frutas.remove('Melón') # si el elemento no está en el set dará un error
frutas.discard('Sandía') #si Sandía existe la borra. Si no, no pasa nada. 

#vaciar y eliminar un set
frutas.clear() #lo vacía, se ve set() por pantalla
del(frutas)#eliminarlo 


lista_frutas = tuple(frutas) #lo transforma en una tupla
print (lista_frutas)

print('----------------')
lista_frutas = list(frutas) #lo transforma en lista
print(lista_frutas[0])
