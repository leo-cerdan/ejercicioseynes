from random import randint

def genera_diccionario():
    id = ["A","B","C","D","E","F","G","H","I","J"]
    edad = []

    for i in range(11):
        a = randint(1,100)
        edad.append(a)

    diccionario = dict(zip(id,edad))

    return diccionario

