##_______________________
#EJERCICIO 4: NOTAS DE CLASE- INSERTAR, ORDENAR y ESTADÍSTICAS
#Tienes una lista de notas de un examen
#Añade tres notas más notas con append() y una en la posición 2 con insert()
#Muestra la lista ordenada de mayor a menor
#Calcula y muestra la media, la nota más alta y la más baja
#Cuenta cuántos alumnos han aprobado (nota>=5)
#________________________________________________________________________________


notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]

def mostrar_notas(notas):
    for nota in notas:
        color = "1" if nota <5 else "2"
        print(f'\033[3{color}m {nota} \033[0m')


def añadir_nota(notas):
    nota_nueva= input('¿Qué nota quieres añadir?: ')
    notas = notas.append(nota_nueva)
    mostrar_notas(notas)

def añadir_por_posicion(notas):
    nota = input('¿Qué nota quieres añadir?: ')
    posicion = input('¿En qué posición quieres añadirla?: ')
    notas = notas.insert(int(posicion), float(nota))


def mostrar_lista_ordenada(notas):
    notas_ordenadas = notas.sort()
    mostrar_notas(notas_ordenadas)

def media_notas(notas):
    media=sum(notas)/len(notas)
    print(media)

    

def alumnos_aprobados(notas):
    for nota in notas:
        aprobados = 0
        if nota>=5:
            aprobados+=1
    mostrar_notas(notas)


def insertar_nota(nota, posicion=len(notas)):
    notas = notas.insert(int(posicion), float(nota))
    mostrar_notas(notas)




def main():
    
    menu = """
##MENÚ##
-----------------------------------------------
¿Qué operación quieres realizar?

[1] Ver la lista de notas
[2] Añadir una nota al final
[3] Añadir una nota por posición
[4] Ver la lista ordenada
[5] Calcular la media
[6] Calcular el máximo
[7] Calcular el mínimo
[8] Ver cuántos alumnos han aprobado
[x] Salir
"""

    print(menu)

    option = input ('¿Qué operación quieres realizar? ')
    if option == '1':
        mostrar_notas(notas)
    elif option == '2':
        insertar_nota(notas)
    elif option == '3':
        posicion= input('Dame la posición: ')
        insertar_nota(notas, posicion)
    elif option == '4':
        mostrar_lista_ordenada(notas)
    elif option == '5':
        media_notas(notas)
    elif option == '6':
        print(max(nota))
    elif option == '7':
        print(min(notas))
    elif option == '8':
        alumnos_aprobados(notas)
    elif option == 'x' or option == 'X':
        print('Hasta pronto. Vuelve cuando quieras')
    else:
        print('Valor introducido no válido. Introduce de nuevo el valor. ')
        main()
    



main()