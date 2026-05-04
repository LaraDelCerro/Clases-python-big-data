producto = {
    "title" : "Televisión 4k 55 pulgadas",
    "price" : 899,
    "quantity": 2,
    "tax" : 21
    }


producto1 = {
    'title': 'Sillón de masaje',
    "price": 455,
    "quantity": 4, 
    "tax": 10
}

#Suponer que esto es un carrito de un compra de página web. 
# Calcular el PVP (precio de venta al público) del carrito
#PVP = (precio*cantidad) + (precio*cantidad)*0.21 = (precio*cantidad)*1,21

def pvp(producto):
    impuesto=producto['tax']/100
    return round((producto["price"]*producto["quantity"])*(1+impuesto),2)
    

print(f'El precio final del producto es {pvp(producto)}') #2175.58
print(f'El precio final del producto1 {pvp(producto1)}') #2002
      

