import random

# O(log n)
def busqueda_binaria(lista, comienzo, final, objetivo, contador=0):
    print(f'buscando el {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    contador += 1
    if comienzo > final:
        return (False, contador)

    # Division de enteros
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, contador)
    elif lista[medio] < objetivo:  # medio -> objetivo, final
        return busqueda_binaria(lista, comienzo=medio + 1, final=final, objetivo=objetivo, contador=contador)
    else:  # comienzo, objetivo <- medio, final
        return busqueda_binaria(lista, comienzo=comienzo, final=medio - 1, objetivo=objetivo, contador=contador)


if __name__ == '__main__':
    tamano_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    # Ordenar la lista
    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    (encontrado, contador) = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(f'Contador: {contador}')
    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
