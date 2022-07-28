import random


def busqueda_lineal(lista, objetivo):
    match = False

    contador = 0
    # O(n)
    for elemento in lista:
        contador += 1
        if elemento == objetivo:
            match = True
            break

    print(f'contador: {contador}')
    return match


if __name__ == '__main__':
    tamaño_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamaño_lista)]

    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
