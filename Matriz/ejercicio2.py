from random import randint

def crear_matriz():
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(randint(1,25))
    return matriz
