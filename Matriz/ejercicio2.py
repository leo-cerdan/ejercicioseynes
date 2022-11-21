from random import randint

def crear_matriz():
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(randint(1,25))
    return matriz

def comprobar_horizontal(matriz):
    """
    Test función comprobar_horizontal
    >>> comprobar_horizontal([[20, 21, 22, 23, 16], [21, 24, 17, 10, 23], [22, 17, 18, 19, 20], [23, 21, 19, 10, 4], [17, 7, 20, 3, 22]])
    Horizontal: inicia con el número 20 posición: matriz[0][0], finaliza con el número: 23 posición: matriz[0][3]
    Horizontal: inicia con el número 17 posición: matriz[2][1], finaliza con el número: 20 posición: matriz[2][4]
    >>> comprobar_horizontal([[2, 5, 9, 10, 1], [20, 4, 24, 10, 23], [14, 5, 20, 8, 20], [23, 6, 19, 10, 4], [17, 7, 8, 9, 10]])
    Horizontal: inicia con el número 7 posición: matriz[4][1], finaliza con el número: 10 posición: matriz[4][4]
    """
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
    """
    Test función comprobar_vertical:
    >>> comprobar_vertical([[20, 21, 22, 23, 16], [21, 24, 17, 10, 23], [22, 17, 18, 19, 20], [23, 21, 19, 10, 4], [17, 7, 20, 3, 22]])
    Vertical: inicia con el número 20 posición: matriz[0][0], finaliza con el número: 23 posición: matriz[3][0]
    Vertical: inicia con el número 17 posición: matriz[1][2], finaliza con el número: 20 posición: matriz[4][2]
    >>> comprobar_vertical([[2, 5, 9, 10, 1], [20, 4, 24, 10, 23], [14, 5, 20, 8, 20], [23, 6, 19, 10, 4], [17, 7, 8, 9, 10]])
    Vertical: inicia con el número 4 posición: matriz[1][1], finaliza con el número: 7 posición: matriz[4][1]
    """
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    matriz = crear_matriz()
    print(matriz)
    comprobar_horizontal(matriz)
    comprobar_vertical(matriz)