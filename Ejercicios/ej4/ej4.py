#Traer los datos de trabajadores.py
from data.trabajadores import trabajadores

#Calcular para cada trabajador el coste de sus horas extra. Dividimos el sueldo entre las horas y sacamos el coste/hora. Multiplicamos por las horas extra

def calcular_coste_hora_extra(trabajador):
    sueldo_por_hora = trabajador['sueldo_base'] / trabajador['horas_contrato']
    sueldo_horas_extra = trabajador['horas_extra'] * sueldo_por_hora
    trabajador['sueldo horas extra'] = calcular_coste_hora_extra


for trabajador in trabajadores:
    calcular_coste_hora_extra(trabajador)


print(calcular_coste_hora_extra(trabajadores))

#calcular la nómina de un trabajador. Nómina = sueldo base menos impuestos sobre sueldo base + horas extra
#calcular la nómina de todos los trabajadores

#probando git
