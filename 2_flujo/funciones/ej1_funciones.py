#Quiero una función que me permita calcular sumas, restas y multiplicaciones de dos nºs.

def sumar(num_A, num_B):
    return num_A + num_B

def restar(num_A, num_B):
    return num_A - num_B

def multiplicar(num_A, num_B):
    return num_A*num_B


def calcular(n1, n2, operacion):
    resultado= 0
    if operacion == 'sumar':
        resultado = sumar(n1,n2)
    elif operacion == 'restar':
        resultado =restar (n1,n2)
    elif operacion == 'multiplicar':
        resultado = multiplicar(n1,n2)
    else:
        print('operación no válida')
    print (resultado)    
