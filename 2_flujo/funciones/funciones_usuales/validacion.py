valor = input('Dime algo bonito: ')
print(valor.isdigit()) #solo dígitos
print(valor.isalpha()) #solo letras
print(valor.isalnum()) #nºs y letras
print(valor.isnumeric()) #si es numero


## saber si una cadena de caracteres empieza, termina o incluye un determinado caracter. True o False
texto = "En un lugar de la Mancha"
print(texto.startswith('e')) #False
print(texto.lower().startswith('e')) #True

#saber si algo está incluido
busqueda="Lugar"
resultado = busqueda.lower() in texto.lower()
print('incluido', resultado)

