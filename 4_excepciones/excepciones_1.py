## try - except, estructurura de excepciones
# try maneja la parte correcta o parte esperada
# except maneja el posible error, no se para la aplicación, sino que todo lo que haya debajo del error se ejecutará 


try:
    entrada = input('Dime un número: ')
    numero = int(entrada)
    print(numero)#si todo va correcto lo imprime por pantalla
except ValueError: #excepción específica,  ocurrirá cuando sea un error del tipo ValueError
    print(f'Has introducido "{entrada}", que no es un valor numérico')
except: #excepción genérica
    print('error genérico')

