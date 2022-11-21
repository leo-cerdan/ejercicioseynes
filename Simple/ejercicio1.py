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

    ordenado = dict(sorted(diccionario.items(), key=itemgetter(1)))

    bajo = list(ordenado.keys())[0]
    alto = list(ordenado.keys())[9]

    print(f"La persona más joven tiene el id: {bajo} y su edad es: {ordenado[bajo]} ")
    print(f"La persona más anciana tiene el id: {alto} y su edad es: {ordenado[alto]}")


