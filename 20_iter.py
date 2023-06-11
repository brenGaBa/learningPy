# Funcionamiento de una iteración:

## normalmente se usaría un bucle:
for i in range(1,10):
    print(i)

# para tener mayor control se usaría un método más "manual":
my_iter = iter(range(1,4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#eel error que sale indica que se acabó el rango y no se puede iterar más