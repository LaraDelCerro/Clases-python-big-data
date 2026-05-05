#EJERCICIO 1: FUNCIÓN QUE CLASIFICA UNA LISTA DE NÚMEROS

numeros = [4, -2, 0, 7, -5, 0, 3, -1, 8, 0, -9, 6]

 #- Crea una función clasificar_numeros(lista) que reciba una lista de números y devuelva tres listas: positivos, negativos y ceros.
# - Crea también una función estadisticas(lista) que devuelva la suma, el mayor numero, menor numero y la media

def color_numero(numero):
    if numero > 0:
        print(f'\033[32m {numero} \033[0m')
    elif numero < 0:
        print(f'\033[31m {numero} \033[0m')





def clasificar_numeros(lista):
    positivos = []
    negativos = []
    ceros = []
    for numero in lista:
        if numero >0:
            positivos.append(numero)
        elif numero <0:
            negativos.append(numero)
        elif numero == 0:
            ceros.append(numero)
        else:
            print(f'El valor {numero} no es número')
    return positivos, negativos,ceros

print(' '*15)
print('## CLASIFICAR NÚMEROS ##')
print(' '*15)

print(f'Lista de números positivos: \033[32m {clasificar_numeros(numeros)[0]} \033[0m') #los pinta de verde
print(f'Lista de números negativos: \033[31m {clasificar_numeros(numeros)[1]} \033[0m')#los pinta de rojo
print(f'Lista de ceros: {clasificar_numeros(numeros)[2]}')

        


def estadisticas(lista):
    print(f'La suma de los números de la lista es {sum(lista)}')
    print(f'El número mayor de la lista es {max(lista)}')
    print(f'El número menor de la lista es {min(lista)}')
    print(f'La media de los números de la lista es {round(sum(lista)/len(lista),2)}')


print(' '*15)
print('## ESTADÍSTICAS ##')
print(' '*15)
estadisticas(numeros)
    
    

 

