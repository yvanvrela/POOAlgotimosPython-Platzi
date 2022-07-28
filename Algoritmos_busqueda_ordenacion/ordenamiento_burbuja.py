import random


# O(n**)
def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        # Se recorre el tamaño de la lista menos lo que ya se recorrio
        for j in range(0, n - i - 1):  # O(n) + O(n) = O(n*n) = O(n**2)

            if lista[j] > lista[j + 1]:
                # 2, 1 -> 1, 2
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == '__main__':
    tamaño_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamaño_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)
