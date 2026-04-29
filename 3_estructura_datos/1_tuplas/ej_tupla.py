#Tenemos un producto 

producto = ('Laptop Pro', 899.94, 15, 'electronica')
producto2 = ('Raton gaming', 34.90, 100, 'electronica')

#el primer elemento representa el nombre del producto
#el segundo, el precio
#el tercero, el stock
#el cuarto la categoría

#quiero hacer una fcón que me permita calcular el precio total del stock de este producto

def precio_total(producto):
    return producto[1]*producto[2]

#print(precio_total(producto))

precio_p1 = precio_total(producto)
precio_p2 = precio_total(producto2)


print (precio_p1, precio_p2)