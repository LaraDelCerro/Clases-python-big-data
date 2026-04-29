#Modificar el ejercicio anterior para que admita nºs negativos

def pedir_numeros():
    numeros = []
    while True:
        num = (input ('Dame un nº: '))
        num_sin_signo = num.replace("-", "")
        if not num_sin_signo.isdigit():
            break
        numeros.append(int(num))
    
    print(numeros)
    
pedir_numeros()


