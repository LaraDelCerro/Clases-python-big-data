#Pedir varios números por pantalla y sumarlos. El programa termina cuando metemos el nº 0. 
#Hacerlo con while

#Ejemplo: 1, 3, 7, 0 -> 11

#Paso 1: pedir un nº constantemente
#Paso 2: crear una vble suma=0
#Paso 3: añadir a suma el valor introducido previamente convertido
#Paso 4: pulsando 0 acabamos el ejercicio

print('#' * 40)
print('Ejercicio 4 - SUMA ACUMULADA')
print('#' * 40)
print(" ")
suma = 0
while True:
    num = float(input('Dame un nº: '))
    if num == 0:
        break
    suma += num
print (f'La suma es {suma}')