nombres = ['Juan', 'Mario', 'Pablo', 'Paula', 'Miriam']

#agregar un único elemento por el final
nombres.append('Joaquín')
print('append', nombres)

#agregar varios elementos a la vez en una lista por el final
nombres.extend(['Miguel Ángel', 'Reniel'])
print('extend', nombres)

#agregar un método en cualquier posición
nombres.insert(1, 'Luis')
print ('insert', nombres) # Juan Luis Mario

#borrar un elemento de la lista
#método pop() 
ultimo_elemento = nombres.pop() #guarda el último elemento
print(nombres)
print(ultimo_elemento)

elemento_tres = nombres.pop(3) #elimina el 3er elemento de la listas

#eliminar elementos de la lista por contenido
nombres.remove('Mario') #si el elemento no está en la lista da error
print(nombres)