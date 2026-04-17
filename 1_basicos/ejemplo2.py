#Comprobar si un nº es par o divisible por 5

numA = float(input("Introduce un nº: "))
resultado = numA%2 == 0 or numA%5 == 0
print(f'El resulatdo es {resultado}')