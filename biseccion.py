# Método de bisección en métodos numéricos
objetivo = int(input('Escribe un número: '))
epsilon = 0.01
inf = 0.0
sup = max(1.0, objetivo)
respuesta = (sup + inf) / 2

while abs (respuesta**2 -objetivo) >= epsilon:
    print(f'i={inf}, s={sup}, r={respuesta}')
    if respuesta**2 < objetivo:
        inf = respuesta
    else:
        sup = respuesta
    respuesta = (sup + inf) / 2
print(f'La raíz cuadrada de {objetivo} es {respuesta}')