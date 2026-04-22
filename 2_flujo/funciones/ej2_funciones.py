#Media de tres nºs 

def sumar(n1,n2,n3):
    return n1 + n2 + n3

def dividir(dividendo, divisor):
    return dividendo/divisor

#def pedir():
    return float(input('Dime un nº: '))


def media (num_1, num_2, num_3):
    num_1= float(input('Dame un primer nº: '))
    num_2=float(input('Dame un segundo nº: '))
    num_3 = float(input('Dame un tercer nº: '))
    suma= sumar(num_1,num_2,num_3)
    media = dividir(suma,3)
print(media)

media()