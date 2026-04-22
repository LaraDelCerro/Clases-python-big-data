# Una función tiene dos partes, definición y llamada, la una sin la otra no pueden convivir. 

#PARTE 1 DECLARACIÓN - DEFINICIÓN

def saludar():
    print('Hola desde una función')

def despedir():
    print('Vete a tu casa, por favor')

#Parte 2: EJECUCIÓN
for i in range(3):
    saludar()
despedir()
