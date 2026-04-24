#Métodos de unión

nombre = "Juan Antonio"
apellido = "Pérez"
edad = 44
separador = "-"

texto = f"{nombre}{separador}{apellido}{separador}{edad}"

otro_texto = separador.join([nombre, apellido, str(edad)])

print(texto)
print(otro_texto)

#Métodos de separación

frase = "El presidente dijo: Hola cómo están los máquinas" #Queremos quedarnos con la frase que dijo el presidente

resultado = frase.partition(": ")
print(resultado)
print(resultado[2])

#Es mejor el método split()
texto = "Porque la vida puede ser maravillosa"
resultado = texto.split(' ') #crea un cjto de elementos sin el espacio en blanco
print (resultado[5]) #saca la palabra maravillosa

#splitlines() me permite separar líneas en un texto multilínea

cadena = """Hola
bienvenido
al
maravilloso
mundo
python
"""

print(cadena)

conjunto_lineas = cadena.splitlines()
print(conjunto_lineas)

# Deletrear una  cadena de texto cualquiera
palabra =  "supercalifragilístico"

print(list(palabra))


