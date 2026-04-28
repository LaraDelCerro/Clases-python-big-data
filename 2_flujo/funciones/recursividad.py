#fcón recursiva es una fcón que se llama a sí misma

'''
def saludar():
    print('hola')
    saludar()

saludar() #haría un bucle infinito de hola
'''

#Crear una fcón que pida un dni solo los nºs y validar que es una cadena numérica. 

#Proceso de validación

def validar_dni():
    dni = input('Dime el número de tu DNI: ')
    if dni.isdigit():
        print('Es un DNI válido')
        return dni
    else:
        print('Esto no es número')
        validar_dni()

mi_dni = validar_dni()
