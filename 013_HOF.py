### Funciones de orden superior
def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1

def hof(x, func):
    return x + func(x)

hof_v2 = lambda x, func: x + func(x)

result = hof(2, increment)
print(result)

