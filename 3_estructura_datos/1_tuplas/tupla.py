#Una tupla es un cjto de datos inmutable (no se puede cambiar, ni de valor ni de longitud). El objetivo es proteger los datos que hay dentro

mi_primera_tupla = ('Lara', 34, True)

frutas = ('naranja', 'pera', 'plátano', 'manzana')

config_db = ('123.0.0.1', 'root', '123456')

print(mi_primera_tupla)
print(frutas)

#cómo saber la longitud de una tupla
print(len(frutas))

#cómo sacar un elemento concreto - un cjto se numera de 0 a n-1, siendo n la longitud
print(frutas[2]) #plátano
print(mi_primera_tupla[0])#Lara
print(frutas[-2])#plátano --> las tuplas se pueden recorrer de izda a dcha (0, 1, 2,...) y de dcha a izqda(-1, -2, -3,...)


#copiar una tupla
otras_frutas = frutas[1:3] #pera, plátano
print (otras_frutas)
print(frutas[0:3:2]) #naranja, plátano

#el uso típico de las tuplas es para el return de las fcones
def devolver_datos_usuario():
    nombre = input ('Dime un nombre: ')
    edad = input ('Dime tu edad: ')
    email = input ('Dime tu email: ')
    return nombre, edad, email

print (devolver_datos_usuario())
print (devolver_datos_usuario()[1])


#las tuplas se pueden recorrer porque tiene posición
for i in range(len(frutas)): #es lo mismo que range(0,len(frutas)), va de 0 a n-1
    print(frutas[i])

#este bucle es equivalente a este otro, más cómodo:
for fruta in frutas:
    print(fruta)


#ERROR con las tuplas
#frutas[0] = 'Mandarina' #no se puede reasignar ningún elemento de la tupla. frutas[0] = 'naranja'
#Tampoco se puede añadir más elementos

#Para eliminar una tupla:
del (frutas)
print(frutas)

#si creo una tupla de un único elemento
tupla_unico_elemento = ('Juan',) #es necesario añadir una coma detrás para que lo trate como tupla
print tupla_unico_elemento