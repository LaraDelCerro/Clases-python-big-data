"""
Tu objetivo es escribir un programa que haga lo siguiente:

Crea una lista con 5 recompensas (textos).

Pide al usuario que introduzca el número de la recompensa que quiere extraer (del 0 al 4).

Utiliza un bloque try-except-finally para controlar los posibles errores:

Maneja el ValueError: Si el usuario escribe letras en lugar de un número.

Maneja el IndexError: Si el usuario escribe un número que no está en la lista (por ejemplo, el 9 o el 25).

El programa debe imprimir siempre al final (haya fallado o no) un mensaje que diga: "Cerrando el catálogo de recompensas. ¡Gracias por jugar!".    
    
"""

def jugar():
recompensas = ["Espada de madera", "Poción de salud", "Escudo", "Botas de velocidad", "Oro"] 
try:
    print(f'Bienvenido al catálogo de recompensas: {recompensas}')
    print(' '*15)
    entrada= input('Dime qué recompensa de la lista quieres (del 0 al 4): ')
    print(' '*15)
    numero = int(entrada)
    print(f'La recompensa solicitada es {recompensas[numero]}')
except ValueError:
    print(f'{entrada} no es un número. Debes introducir un número del 0 al 4')
except IndexError:
    print('El número introducido no se corresponde con ninguna recompensa, debe ser un número de 0 a 4')
finally:
    print('Cerrando el catálogo de recompensas. ¡Gracias por jugar!')


jugar()