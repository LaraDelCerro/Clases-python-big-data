def mostrar_auditoria(fichero, resumen_auditoria):
    variables = resumen_auditoria.keys() #las claves son el nombre de las vbles. 
    print(f'#' * 30)
    print(f'AUDITORÍA DEL FICHERO {fichero}')
    for var in variables:
        print(f'Cambios en la variable {var}: {resumen_auditoria[var]} registros')
        print(' ')
    #print(f'#' * 30)