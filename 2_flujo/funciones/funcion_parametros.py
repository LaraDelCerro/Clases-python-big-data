#Una función puede tener dos tipos de parámetros
    #obligatorios
    #optativos

numero_1 = 3
numer_2 = 23

def sumar(num_1, num_2):
    resultado = num_1 + num_2 
    print(resultado)

def potencia(base, exp):
    resultado = base ** exp
    print(f'El resultado de {base} elevado a {exp} es {resultado}')

potencia(3,4)
potencia(10,6)

#Parámetros optativos
def potencia(base, exp=3): #exp es optativo. Si no le paso exp, tomará el valor 3. Si le paso un valor, lo toma. 
    resultado = base ** exp
    print(f'El resultado de {base} elevado a {exp} es {resultado}')

potencia(2) # es equivalente a potencia(2,3)
potencia(2,4)

#Media de tres números cualquiera

def media(num_1, num_2, num_3):
    suma=num_1 + num_2 + num_3
    media=suma/3
    print (media)

