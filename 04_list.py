## Como crear listas iterables

## Forma clásica:
numbers = []
for i in range(1, 11):
    numbers.append(i*2)
print(numbers)

## Forma condensada:
numbers_v2 = [i*2 for i in range(1, 11)]
print(numbers_v2)

# Ahora agregamos condiciones:
  # En la forma clásica
numbers = []
for i in range(1, 11):
    if i%2 == 0:
     numbers.append(i*2)
print(numbers)
  # En la forma condensada:
numbers_v2 = [i*2 for i in range(1, 11) if i%2 == 0]
print(numbers_v2)
