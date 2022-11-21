from random import randint

def crear_matriz():
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(randint(1,25))
    return matriz

def comprobar_horizontal(matriz):
    horizontal = 0
    horizontal1 = 0
    horizontal2 = 0
    horizontal3 = 0
    horizontal4 = 0
    for i in range(5):
        for j in range(4):
            if matriz[i][j] + 1 == matriz[i][j+1]:
                if i == 0:
                    horizontal += 1
                    if horizontal == 3:
                        resultado_horizontal(matriz, i, j)
                elif i == 1:
                    horizontal1 += 1
                    if horizontal1 == 3:
                        resultado_horizontal(matriz, i, j)
                elif i == 2:
                    horizontal2 += 1
                    if horizontal2 == 3:
                        resultado_horizontal(matriz, i, j)
                elif i == 3:
                    horizontal3 += 1
                    if horizontal3 == 3:
                        resultado_horizontal(matriz, i, j)
                elif i == 4:
                    horizontal4 += 1
                    if horizontal4 == 3:
                        resultado_horizontal(matriz, i, j)

def comprobar_vertical(matriz):
    vertical = 0
    vertical1 = 0
    vertical2 = 0
    vertical3 = 0
    vertical4 = 0
    for i in range(5):
        for j in range(4):
            if matriz[j][i]+1 == matriz[j+1][i]:
                if i == 0:
                    vertical += 1
                    if vertical == 3:
                        resultado_verical(matriz, i, j)
                elif i == 1:
                    vertical1 += 1
                    if vertical1 == 3:
                        resultado_verical(matriz, i, j)
                elif i == 2:
                    vertical2 += 1
                    if vertical2 == 3:
                        resultado_verical(matriz, i, j)
                elif i == 3:
                    vertical3 += 1
                    if vertical3 == 3:
                        resultado_verical(matriz, i, j)
                elif i == 4:
                    vertical4 += 1
                    if vertical4 == 3:
                        resultado_verical(matriz, i, j)

def resultado_horizontal(matriz, i, j):
    print(f"Horizontal: inicia con el número {matriz[i][j-2]} posición: matriz[{i}][{j-2}], finaliza con el número: {matriz[i][j+1]} posición: matriz[{i}][{j+1}]")

def resultado_verical(matriz, i, j):
    print(f"Vertical: inicia con el número {matriz[j-2][i]} posición: matriz[{j-2}][{i}], finaliza con el número: {matriz[j+1][i]} posición: matriz[{j+1}][{i}]")

