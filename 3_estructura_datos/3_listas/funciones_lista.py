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

#nombres.remove('MARIO') #daría un error 
#nombres.remove('MARIO'.title()) #arreglaría el error anterior

#fcón que nos permita contar un elemento concreto en la lista
animales = ['león', 'perro', 'gato', 'jiraja', 'león', 'hipopótamo']

print(len(animales)) #6

#¿Cuántos "león" hay en la lista?
print(animales.count('león')) #2

#invertir una lista. reverse modifica el listado original

animales.reverse()
print(animales)

#ordenar la lista. Modifica la lista

numeros = [12, 34, 5, 6, 74, 34, 6,8, 1]
letras = ['a', 'F', 'D','i', 'b']

numeros.sort() #ordena de menor a mayor
numeros.sort(reverse=False)#ordena de mayor a menor

#ordenación de letras
print(letras.sort())
letras.sort(key=str.lower) #para que las trate todas como minúsculas y luego las ordene porque si no, ordenaría 1º las minúsculas y luego mayusc. 
print(letras)

# orden por longitud de caracteres de un string
nombres.sort(key=len, reverse=True)
print(nombres)


#pero sort tiene un problema, modifica la lista original. Para evitar esto Python ha creado un método parecido que tiene los mismos parámetros, SORTED()
nueva_lista = sorted(nombres, key= len, reverse=False)
print(nombres)
print(nueva_lista)


#Max y Min
print(max(numeros))#74
print(min(numeros))#1



