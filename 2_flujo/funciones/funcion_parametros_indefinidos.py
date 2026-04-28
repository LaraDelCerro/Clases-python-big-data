
# *numeros representa un cjto de datos, que tiene posición, empezando en 0 y terminando en n-1, siendo n la longitud o cantidad de datos introducidos
def sumar(*numeros): #el * indica un cjto de nºs 
    resultado = 0
    for i in range(len(numeros)): #va de 0 a n-1
        resultado += (numeros[i])
    print(resultado)
    print('.------------')




sumar(1,2)
sumar(1,4,3)
sumar(1,6,3,4,5,12)

def sumar2(*numeros):  #lo mismo con la fcón sum
    print (sum(numeros))

sumar2(1,4,3)




def sumar_(numeros):  
    resultado = 0
    for i in range(len(numeros)): #va de 0 a n-1
        resultado += (numeros[i])
    return (resultado)



def media(*numeros):
    print (sumar_(numeros)/len(numeros))

media(1,2,3,4,5)
media(2,3,4)

def media(*numeros):  #este bucle es más cómodo de usar y hace lo mismo
    suma = 0 
    for numero in numeros:
        suma += numero
    print(suma/len(numeros))