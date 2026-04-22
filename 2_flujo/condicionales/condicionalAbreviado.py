#Definir el valor de una variable en función de una condición

estado_luz = True


mensaje = "La luz está encendida" if estado_luz else "La luz está apagada"
print (mensaje)

#Esta línea es equivalente a: 
if estado_luz :
    mensaje = "La luz está encencida"
else:
    mensaje = "La luz está apagada"
print(mensaje)