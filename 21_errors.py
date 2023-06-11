# error de sintaxix
#print(0/0)


# la variable no existe:
#print(result)
print('hola')
# cuando se detecta un error, el programa se detiene 

# se puede probar el funcionamiento correcto de una función:
suma = lambda x,y: x + y
assert suma(2,2) == 4
print('todo ok, sin errores')

# se pueden programar condiciones para que den error:
age = 20
if age < 18:
    raise Exception('Debes ser mayor de edad para acceder')

print('Soy mayor de edad')