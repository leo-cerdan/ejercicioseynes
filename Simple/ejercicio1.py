from random import randint
from operator import itemgetter

def genera_diccionario():
    id = ["A","B","C","D","E","F","G","H","I","J"]
    edad = []

    for i in range(11):
        a = randint(1,100)
        edad.append(a)

    diccionario = dict(zip(id,edad))

    return diccionario

def ordenar_diccionario(diccionario):

    """
    Test de la función ordenar_diccionario
    >>> ordenar_diccionario({'A': 72, 'B': 71, 'C': 81, 'D': 55, 'E': 37, 'F': 89, 'G': 31, 'H': 21, 'I': 18, 'J': 58})
    La persona más joven tiene el id: I y su edad es: 18 
    La persona más anciana tiene el id: F y su edad es: 89
    {'I': 18, 'H': 21, 'G': 31, 'E': 37, 'D': 55, 'J': 58, 'B': 71, 'A': 72, 'C': 81, 'F': 89}
    >>> ordenar_diccionario({'A': 72, 'B': 71, 'C': 81, 'D': 55, 'E': 37, 'F': 89, 'G': 31, 'H': 21, 'I': 18, 'J': 58})
    La persona más joven tiene el id: I y su edad es: 18 
    La persona más anciana tiene el id: F y su edad es: 89
    {'A': 72, 'B': 71, 'C': 81, 'D': 55, 'E': 37, 'F': 89, 'G': 31, 'H': 21, 'I': 18, 'J': 58}
    """

    ordenado = dict(sorted(diccionario.items(), key=itemgetter(1)))

    bajo = list(ordenado.keys())[0]
    alto = list(ordenado.keys())[9]

    print(f"La persona más joven tiene el id: {bajo} y su edad es: {ordenado[bajo]} ")
    print(f"La persona más anciana tiene el id: {alto} y su edad es: {ordenado[alto]}")

    return ordenado

if __name__ == "__main__":
    import doctest
    doctest.testmod()