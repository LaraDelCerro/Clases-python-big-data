#Vamos a crear un menú que me permita decidir que operación va a hacer mi calculadora:

def pedir_numeros():
    num1 = float(input('Dime un número: '))
    num2= float(input('Dime un número: '))
    return num1, num2



def main():
    menu = """
##BIENVENIDO A NUESTRA MARAVILLOSA CALCULADORA##
-----------------------------------------------
¿Qué operación quieres realizar?

[1] Sumar
[2] Restar
[3] Multiplicar
[x] Salir
"""

    print(menu)
    option = input ('¿Qué operación quieres realizar? ')
    if option == '1':
        numeros = pedir_numeros()
        resultado= numeros[0] + numeros[1]
    elif option == '2':
        numeros = pedir_numeros()
        resultado= numeros[0] - numeros[1]
    elif option == '3':
        numeros = pedir_numeros()
        resultado= numeros[0] * numeros[1]
    elif option == 'x' or option == 'X':
        print('Hasta pronto. Vuelve cuando quieras')
        return False
    else:
        print('Valor introducido no válido. Introduce de nuevo el valor. ')
        main()
    print(resultado)
    main()    

main()
