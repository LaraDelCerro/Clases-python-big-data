


try:
    numero = int(input('Dime un número: '))
    numero2= int(input('Dime otro número: '))
    resultado = numero/numero2
    print(resultado)
except ValueError:
    print('Los valores introducidos no son números')
except ZeroDivisionError:
    print('no se puede dividir entre cero')
except:#error genérico por si surge algo que no se nos ocurre, para que no se detenga la aplicación
    print('futuro error no previsto') 


print('otros cálculos') #esta línea se ejecutará aunque tengamos un error en las líneas superiores