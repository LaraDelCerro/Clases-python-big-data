""""
  Cálculo del precio a pagar en un aparcamiento
    - Pedir el número de horas que ha estado aparcado (número decimales permitidos)
        - El número de horas debe ser mayor de 0
    - Pedir si tiene tarjeta residente o no ("s" o "n")
        - La opción solo puede ser s o n
    - Pedir el tipo de vehículo ("moto", "coche", "furgoneta")
        - El tipo de vehículo debe ser moto, coche o furgonet
    - Validamos los datos

    - Cálculo el precio dependiendo de las horas:
        - Primera hora: 2€
        - De 1 a 3 horas: 1.5€ por hora adicional
        - Más de 3 horas: 1€ por hora adicional a partir de la 3ª 
"""
"""
    - Multiplicador de precio dependiendo del vehículo:
        moto x 0.7, coche x 1, furgoneta x 1.5

    - Aplica 20% descuento sobre el precio si erees residente

    FORMATO:
    --- TICKET DE APARCAMIENTO ---
    Horas: 2.5 | Vehículo: coche | Residente: sí
    Precio base: 3.75 €
    Descuento residente: -0.75 €
    TOTAL: 3.00 €

"""



horas = float(input('Dime el nº de horas: '))
tarjeta = input('¿Tienes tarjeta de residente? [s/n]: '). lower()
vehiculo = input('¿Qué tipo de vehículo: moto, coche o furgoneta?: '). lower()

if horas<=0 :
    print("Nº de horas no válido")
elif tarjeta not in ("s", "n"):
    print('Respuesta no válida.')
elif vehiculo not in ("moto", "coche", "furgoneta"):
    print ("Opción de vehículo no válida")
else:
    if horas <= 1:
        precio = 2
    elif horas <=3:
        precio = 2 + (horas-1)*1.5
    else:
        precio= 2 + 2*1.5 + (horas-3)
#multiplicador
    multiplicador = 1 
    if vehiculo == "moto":
         multiplicador= 0.7
    elif vehiculo == "furgoneta":
        multiplicador =  1.5
    total= precio * multiplicador       
 #descuento residente  
    if tarjeta == "s":
        precio = precio * 0.8
        tarjeta = 'Sí'
        descuento = precio * 0.2
    else:
        tarjeta == "No"
    #print(f'Has estado {horas}. El precio es {precio}€')

    print (f"""
    --- TICKET DE APARCAMIENTO ---
        Horas: {horas} | Vehículo: {vehiculo} | Residente: {tarjeta}
        Precio base: {precio} €
        Descuento residente: -{round(descuento)} €
        TOTAL: {total} €

    """)