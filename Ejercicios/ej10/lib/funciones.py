def limpiar_string(cadena, lower = False):
    if not cadena:
        return 'Sin datos'
    nuevo_str = cadena.strip()
    if lower:
        nuevo_str = nuevo_str.lower()
    return nuevo_str

def limpiar_id(id):
    if not id:
        return None
    nuevo_id = str(id).strip()
    return int(nuevo_id)

def limpiar_precio(precio):
    nuevo_precio = precio.replace('€', '')
    nuevo_precio = nuevo_precio.lower()
    if  nuevo_precio == 'gratis':
        nuevo_precio = 0
    nuevo_precio = round(float(nuevo_precio),2)
    return nuevo_precio


def limpiar_stock(stock):
    if not stock.isdigit() or int(stock) < 0:
        nuevo_stock = 0
    else:
        nuevo_stock = int(stock)
    return nuevo_stock
