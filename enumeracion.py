objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1
    print(respuesta)

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raíz cuadrada exacta')