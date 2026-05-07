
print('------Simulación de conexión a Base de Datos')
conexion_bbdd = False
lista_inexistente = ['uno','dos', 'tres']
try:
    print('1 - conectando a la BBDD')
    conexion_bbdd = True
    print('2 - pedimos los dato de un cliente')
    cliente = lista_inexistente[2]
    print('cliente encontrado')
except NameError: #error específicico si no existe la lista cliente
    print('la tabla de clientes no existe')
except IndexError: #error si la lista cliente tiene 3 valores y he pedido los datos del cuarto, por ejemplos
    print('El cliente solicitado no existe')
finally: #el finally ocurre siempre, haya o no error. 
    print('cierro la conexion')
    

print('lo siguiente')