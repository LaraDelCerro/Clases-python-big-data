nota = float(input('Dime tu nota: '))

if nota  >= 5 and nota <= 10:
    print ("Aprobado")
elif nota >= 0 and nota < 5:
    print ("Suspenso")
else:
    print("Nota no válida")


if  0 <= nota < 5:
    print("Suspenso")
elif 5 <= nota < 6:
    print("Suficiente")
elif 6<= nota < 7:
    print ("Bien")
elif 7<= nota < 9:
    print ("Notable")
elif 9<= nota <= 10 :
    print ("Sobresaliente")
else:
    print("Nota no válida")