# python tiene una libreria especial para funciones matemáticas complejas math. Para usarla tenemos que importarla al principio del script
# tiene libreria operaciones matematicas math
# https://docs.python.org/3/library/math.html

import math

# funciones de conversion
numero = 5
print( float(numero) ) # 5.0 racional
print( int(3.3) ) # 3 integer

# a modo reto, conseguir que no redondee a 5 
nota = 4.999999999999999999
print(nota)
#Solución:
otra_nota= input('Dime tu nota: ') #no redondea a 5 porque input recoge un string
print(float(otra_nota[0:5])) # transforma a float y coge solo las posiciones 0-4 del string

# redondeo de un numero
numero = 4.567892
print( round(numero, 4) ) # matematico

# redondeo a la alta
print(math.ceil(numero)) #5
# redondeo a la baja
print(math.floor(numero)) #4

#raíz cuadrada de un numero
print(math.sqrt(256))#16

#suma de un conjunto de nºs
suma_total= math.fsum([1,2,3,4])
