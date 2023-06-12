# Como leer un archivo txt
file = open('./texto.txt')
print(file.read())

# Pero el método ocupa mucha memoria...
# método más ligero, pero a veces no sabemos cuantas lineas hay
print(file.readline())

# lee linea a linea sin bloquear la memoria usando bucles:
for line in file:
    print(line)

# es importante cerrar el archivo:
file.close()

# forma mas comun de leer archivos (cierra automaticamente):
with open('./texto.txt') as file:
    for line in file:
        print(line)
