contador_e = 0
contador_i = 0
while contador_e < 5:
    while contador_i < 6:
        print(contador_e, contador_i)
        contador_i += 1 #contador = contador + 1
        if contador_i >= 3:
            break
    contador_e += 1
    contador_i = 0