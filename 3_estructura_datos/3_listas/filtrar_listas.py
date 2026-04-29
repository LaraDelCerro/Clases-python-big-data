## Filtrado de listas. 

#Me dan una lista y quiero separar los nºs pares de los impares

numeros = [1,2,3,4,5,6,45,46, 72, 33, 36]
otra_lista =[1,3,5,4,6,7,45,46,74]



def obtener_lista_pares(lista):
    lista_resultante=[]
    for numero in lista:
        if numero % 2 == 0:
            lista_resultante.append(numero)
    return lista_resultante

numero_pares = obtener_lista_pares (otra_lista)
print(numero_pares)


#Modificar esta fcón para que devuelva o una lista de impares o una lista de pares

def obtener_lista(lista, tipo):
    lista_pares= []
    lista_impares=[]
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)
    return lista_pares if tipo == 'pares' else lista_impares


numeros_pares = obtener_lista(numeros, 'pares')
numeros_impares = obtener_lista(numeros, 'impares')

print(numeros_pares)
print(numeros_impares)