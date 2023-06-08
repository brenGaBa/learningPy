# Inmutabilidad: conservando el diccionario original
## Partiendo del script anterior:

items = [
    {'product': 'camisa', 'price': 100},
    {'product': 'pantalon 1', 'price': 300},
    {'product': 'pantalon 2', 'price': 200}
]

# lambda permite condensar el bucle en una sola línea
prices = list(map(lambda item: item['price'], items))
print(prices)

# Se modifica la función para que la iteración no altere el original
def taxes_add(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price']*0.19
    return new_item

new_items = list(map(taxes_add, items))
print(new_items)