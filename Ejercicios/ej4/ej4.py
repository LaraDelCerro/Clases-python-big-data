#Traer los datos de trabajadores.py
from data.trabajadores import trabajadores

#Calcular para cada trabajador el coste de sus horas extra. Dividimos el sueldo entre las horas y sacamos el coste/hora. Multiplicamos por las horas extra

def calcular_coste_hora_extra(trabajador):
    sueldo_por_hora = trabajador['sueldo_base'] / trabajador['horas_contrato']
    sueldo_horas_extra = trabajador['horas_extra'] * sueldo_por_hora
    trabajador['sueldo_horas_extra'] = sueldo_horas_extra
    #print(trabajador)



#calcular la nómina de un trabajador. Nómina = sueldo base menos impuestos sobre sueldo base + horas extra
#calcular la nómina de todos los trabajadores


def calcular_nomina(trabajador):
    irpf = trabajador['sueldo_base']*(trabajador['porcentaje_impuestos']/100)
    sueldo_neta_sin_extras  = trabajador['sueldo_base'] - irpf
    sueldo_final= sueldo_neta_sin_extras + trabajador['sueldo_horas_extra']
    trabajador['nomina'] = sueldo_final
    
    
   
for trabajador in trabajadores:
    calcular_coste_hora_extra(trabajador)
    calcular_nomina(trabajador)
    print(trabajador)

#pintar todos los trabajores de la lista

def pintar(lista):
    for trabajador in lista:
        print(f'Nombre: {trabajador['nombre']}, Departamento: {trabajador['departamento']}')

pintar(trabajadores)
print('*'*20)

#filtrar los trabajadores y pintarlos por categoría

def filtrar_depto(lista, departamento):
    trabajadores_departamento = []
    for elemento in lista: #recorro la lista
        if elemento['departamento'] == departamento: #si la clave 'departamento' del trabajador coincide con el departamento buscado, añado ese trabajador a la lista
            trabajadores_departamento.append(elemento) #añado el trabajador a la lista
    return trabajadores_departamento



trabajadores_diseño = filtrar_depto(trabajadores, 'Diseño')
pintar(trabajadores_diseño)

trabajadores_TI = filtrar_depto(trabajadores, 'TI')
pintar(trabajadores_TI)





