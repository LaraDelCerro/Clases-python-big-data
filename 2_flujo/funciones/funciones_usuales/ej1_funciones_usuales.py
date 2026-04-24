# =============================================================================
# EJERCICIO : PROCESADOR DE FRASES
# Pide al usuario una frase.
# Muestra:
#   - La frase con todas las palabras invertidas individualmente
#     (ej: "hola mundo" → "aloh odnum")
#   - devolver la cantidad de letras de la frase
#   - El número de veces que aparece cada vocal (a, e, i, o, u)
#   - La frase con los espacios reemplazados por guiones bajos
#   - La frase con palabras invertidas Tony Stark => Stark Tony
# =============================================================================

frase = input ('Dime la frase: ')

#reemplazar espacios por guiones
def frase_con_separador(texto, separador):
    return texto.replace(' ', separador)

print(frase_con_separador(frase_con_separador, '_'))


#contar las letras
def cantidad_letras(texto):
    contador = 0
    for caracter in texto:
        if caracter.isalpha():
            contador += 1
    return contador

print (cantidad_letras(frase))


#contar vocales
def contar_vocal(texto, vocal):
    return texto.count(vocal)

for vocal in "aeiouáéíóúAEIOUÁÉÍÓÚ":
    if contar_vocal(frase,vocal)!=0:
        print(vocal, contar_vocal(frase, vocal))


#frase con palabras invertidas

#paso 1: convertir la frase en una lista
lista_palabras= texto.split(" ")
cantidad = len (lista_palabras)
frase_invertida=""
while cantidad > 0:
    frase_invertida += f"{lista_palabras[cantidad-1]}"
    cantidad -=1

print(frase_invertida)

#palabras invertidas individualmente
lista_caracteres= list(frase)
cantidad2 = len(list(texto))


def invertir_ lista (lista)



# opcion 1: sin funcion
lista_palabras = texto.split(" ")
cantidad = len(lista_palabras)
frase_invertida = ""
while(cantidad > 0):
    frase_invertida += f"{lista_palabras[cantidad-1]} "
    cantidad -= 1
    
print(frase_invertida)

lista_caracteres = list(texto)
cantidad2 = len(list(texto))
frase_invertida2 = ""
while(cantidad2 > 0):
    frase_invertida2 += f"{lista_caracteres[cantidad2 - 1]}"
    cantidad2 -= 1
    
print( frase_invertida2 )

######
#opcion 2: con funcion 
def invertir_lista(lista, separador):
    cantidad = len(lista)
    frase_invertida = ""
    while(cantidad > 0):
        frase_invertida += f"{lista[cantidad-1]}" + separador
        cantidad -= 1
    print(frase_invertida)

lista_palabras = texto.split(" ")
invertir_lista(lista_palabras , " ")


lista_caracteres = list(texto)
invertir_lista(lista_caracteres, "")