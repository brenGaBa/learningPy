# SCRIPT con diferentes formas de resolver una raíz cuadrada

#Método de fuerza bruta
def enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
    
    if respuesta**2 == objetivo:
        return respuesta
    else:
        print(f'{objetivo} no tiene raíz cuadrada exacta')

#Método con aproximación
def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada de {objetivo}')
    else: 
        return respuesta

#Método bisección
def biseccion(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        
        if respuesta**2 < objetivo:
            bajo = respuesta
        else: 
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return respuesta

#Opción de elegir el método para resolver la raíz cuadrada

method = input('Escoge el método para calcular la raíz cuadrada:\n [E]\n [A]\n [B]')

objetivo = int(input('Escribe un número entero: '))

if method == 'e' or method == 'E':
    result = enumeracion(objetivo)
    print(f'La raíz cuadrada de {objetivo} es {result}')

elif method == 'a' or method == 'A':
    result = aproximacion(objetivo)
    print(f'La raíz cuadrada de {objetivo} es {result}')

elif method == 'b' or 'B':
    result = biseccion(objetivo)
    print(f'La raíz cuadrada de {objetivo} es {result}')

else:
    print('No escogiste un método válido')

if result != None:
    print(f'La raíz cuadrada de {objetivo} es {result}')