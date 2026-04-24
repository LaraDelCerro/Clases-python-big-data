# replace -> sanitizar o limpiar textos

frase = 'Ho)laÇm^u)nd^oÇde)sdeÇp)yth^on'

frase = frase.replace(')', '').replace('^', '')
frase = frase.replace('Ç', ' ')
print(frase)

otra_frase = "Él envió más café frío allá después según él también pidió algún té allí recién así él podría reír todavía."
otra_frase =  otra_frase.lower()
otra_frase = otra_frase.replace('ó', 'o').replace('é', 'e').replace('á', 'a').replace('ú', 'u').replace('í', 'i')
print(otra_frase)


def quitar_acentos(texto):
    return texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')

resultado = quitar_acentos(otra_frase)
print(resultado)

#eliminar los espacios en blanco dentro de una palabra, espacios por delante y por detrás
#strip() elimina por los dos lados
#lstrip() elimina por la izqda
#rstrip() elimina por la dcha

nombre = '   Juan Antonio    '
print(f'Hola, {nombre.strip()}, ¿cómo estás?')
