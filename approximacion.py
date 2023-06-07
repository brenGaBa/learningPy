# variables
objetivo = int(input('Escoge un número: '))
epsilon = 0.01
respuesta = 0.0
paso = epsilon**2

while respuesta**2 <= objetivo and abs(respuesta**2 - objetivo) >= epsilon:
    respuesta += paso
    #print(respuesta)
if abs(respuesta**2 - objetivo) >= epsilon:
    print('No se encontró la raíz cuadrada')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')