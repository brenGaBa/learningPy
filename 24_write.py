with open('./texto.txt', '+w') as file:
    for line in file:
        print(line)
    file.write('126898956\n')
    file.write('esos fueron numeros\n')
    file.write('y ahora hay texto xD\n')
# 'r+' permite escribir mas lineas respetando el contenido original
# 'w+' sobreescribe todo el archivo

