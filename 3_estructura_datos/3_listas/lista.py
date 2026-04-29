#Una lista es un cjto de elementos, casi siempre del mismo tipo, ordenado por posición

lista_nombres = ['Miguel Ángel', 'Pablo', 'Lara', 'Paula']
lista = ['Juan', 44, True] #es posible pero no es muy habitual, tendría más sentido una tupla

#Longitud - cantidad de elementos
print(len(lista_nombres)) #4

#imprimir un valor de la lista
print(lista_nombres[2])#Lara

#añadir elementos a la lista por el final
nombre_nuevo = 'Reniel'
lista_nombres.append(nombre_nuevo) #no permite añadir más de uno
print(lista_nombres)

#recorren la lista - varios métodos

for i in range(len(lista_nombres)):
    print(lista_nombres[i])

print('-----------------------')


for nombre in lista_nombres:
    print(nombre)
    #if nombre == 'Pablo':
        #break              En este caso se imprimiría Miguel Ángel, Pablo. 
else:
    print('La lista ha terminado')


#Cambiar cualquier elemento de la lista. La lista es mutable
lista_nombres[1] = 'Miriam'
print(lista_nombres) #Miriam ha sustituido a Pablo

