# Uso de map combinado con diccionarios
items = [
    {'product': 'camisa', 'price': 100},
    {'product': 'pantalon 1', 'price': 300},
    {'product': 'pantalon 2', 'price': 200}
]

# lambda permite condensar el bucle en una sola línea
prices = list(map(lambda item: item['price'], items))
print(prices)

# Suponiendo que necesitamos calcular los imptos del producto
def taxes_add(item):
    item['taxes'] = item['price']*0.19
    return item

new_items = list(map(taxes_add, items))
print(new_items)
