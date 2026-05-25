
def comprobar_duplicados(email,tel, lista):
    for contacto in lista:
        if contacto['email'] == email or contacto['teléfono'] == tel:
            return False
    return True

            

  
def validar_contacto(nombre, email, tel):
    if nombre == "" or not tel.isdigit() or '@' not in email:
        return False
    return True



def insertar_contacto(nombre, email, tel, lista): #ya sabemos que los datos son correctos, creamos el contacto
    nuevo_contacto = {
        'nombre': nombre,
        'email': email,
        'teléfono': tel
    }
    no_duplicado = comprobar_duplicados(email, tel, lista)
    if no_duplicado:
        lista.append(nuevo_contacto)
    else:
        print('Usuario duplicado')



def pintar_contactos(lista):
    for contacto in lista:
        print("-"*15)
        print(f'{contacto['nombre']} - {contacto['email']} - {contacto['teléfono']}')
        print('-'*15)


