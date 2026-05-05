# EJERCICIO 2: CATÁLOGO DE PELÍCULAS
# Tienes una lista de diccionarios con películas (titulo, director, año, nota).
# Recorre la lista y muestra cada película con sus datos formateados si la nota es aprobada en verde y si no en rojo solo la nota
# Muestra solo las películas con nota >= 8.
# Ordena la lista por año (ascendente) y muéstrala de nuevo.
# =============================================================================

peliculas = [
    {'titulo': 'El Padrino', 'director': 'F. Coppola',   'anio': 1972, 'nota': 9.2},
    {'titulo': 'Interstellar','director': 'C. Nolan',     'anio': 2014, 'nota': 8.6},
    {'titulo': 'El Gran Lebowski','director': 'Coen Bros.',   'anio': 1998, 'nota': 7.9},
    {'titulo': 'Pulp Fiction','director': 'Q. Tarantino', 'anio': 1994, 'nota': 4.9},
    {'titulo': 'La La Land','director': 'D. Chazelle',  'anio': 2016, 'nota': 3.0},
    {'titulo': 'Joker','director': 'T. Phillips',  'anio': 2019, 'nota': 7.5},
]

peliculas2 = [
    {'titulo': 'Notting Hill', 'director': 'Roger Michell', 'anio': 1999, 'nota': 9.2},
    {'titulo': 'El diario de Noa', 'director': 'Nick Cassavetes', 'anio': 2004, 'nota': 8.6},
    {'titulo': 'Tienes un email', 'director': 'Nora Ephron', 'anio': 1998, 'nota': 7.9},
    {'titulo': 'Cómo perder a un chico en 10 días', 'director': 'Donald Petrie', 'anio': 2003, 'nota': 4.9},
    {'titulo': 'Mejor... imposible', 'director': 'James L. Brooks', 'anio': 1997, 'nota': 3.0},
    {'titulo': 'Love Actually', 'director': 'Richard Curtis', 'anio': 2003, 'nota': 7.5},
]


def colorear(numero):
    rojo = "\033[91m"
    verde = "\033[92m"
    reset = "\033[0m"
    if numero >= 5 and numero <=10:
        return f"{verde}{numero}{reset}"
    elif numero >= 0 and numero < 5:
        return f"{rojo}{numero}{reset}"




def mostrar_peliculas(lista, titulo):
    print(f'\n##### {titulo} #######\n')
    for pelicula in lista:
        print (' '*15)
        print(f'Título: {pelicula['titulo']} | Director: {pelicula['director']} | Año: {pelicula['anio']} | Nota: {colorear(pelicula['nota'])}')
        print('-'*15)


mostrar_peliculas(peliculas, 'Acción')
mostrar_peliculas(peliculas, 'Románticas')

def filtrar_por_nota(lista, nota_min, nota_max):
    pelis_filtradas = []
    for pelicula in lista:
        if pelicula['nota'] >= nota_min and pelicula['nota']<= nota_max:
            pelis_filtradas.append(pelicula)
    return pelis_filtradas

peliculas_nota_mayor_que_ocho  = filtrar_por_nota(peliculas, 8, 10)
mostrar_peliculas(peliculas_nota_mayor_que_ocho,'Películas cuya nota es mayor que 8' )



def ordenar_por_anio(lista, ordenacion):
    booleano = True if ordenacion == 'dsc' else False
    resultado = sorted(lista, key= lambda pelicula: pelicula['anio'], reverse=False)
    return resultado

peliculas_ordenadas = ordenar_por_anio(peliculas, 'dsc')

mostrar_peliculas(peliculas_ordenadas, 'películas ordenadas por año')


