### uso de la función map: transformación a cada elemento AKA interaciones

numbers = [1, 2, 3, 4]

# Forma que usaba hasta ahora:
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i*2)

print(numbers)
print(numbers_v2)

# Con map se hace en 1 sola línea:
numbers_v3 = list(map(lambda i: i*2, numbers))

print(numbers_v3)

# Qué pasa con listas de longitudes diferentes:
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)