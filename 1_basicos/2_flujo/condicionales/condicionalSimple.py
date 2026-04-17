

nota = float (input("Dime tu nota: "))

while nota <0 or nota >10:
    print ('Nota no válida')
    nota = float (input("Dime tu nota: "))

if nota <5:
    print ('Suspenso')
else:
    print('Aprobado')




#"""
#     Pide por input el importe de una compra
#     Si el importe es mayor que 100 muestra el mensaje:
#         "Aplicamos un 10% de descuento"
#     Y además, mostramos el precio con el descuento aplicado
# """   

Importe = float(input("Dame el importe de la compra: "))
if Importe > 100:
    print('Aplicamos el 10% de descuento')
    nuevo_importe= 0.9* Importe
    print(f'Precio original: {Importe}€. Nuevo precio: {nuevo_importe}€')
