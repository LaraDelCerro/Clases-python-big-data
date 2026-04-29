#Pedir nºs por pantalla, insertarlos en una lista de nºs. El programa para cuando introduzcamos una letra y dicha letra no estará en la lista. 

def pedir_numeros():
    numeros = []
    while True:
        num = input ('Dame un nº: ')
        if not num.isdigit():
            break
        numeros.append(int(num))
    
    print(numeros)
    

pedir_numeros()


