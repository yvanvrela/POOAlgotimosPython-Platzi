"""
    Otro concepto importante a tener en cuenta es que en Python 
    las funciones son objetos de primera-clase, es decir, 
    que pueden ser pasados y utilizados como argumentos al igual 
    que cualquier otro objeto (strings, enteros, flotantes, listas, etc.).
"""


def presentarse(nombre: str) -> str:
    return f'Me llamo {nombre}'


def estudiar_juntos(nombre: str) -> str:
    return f'¡Estudiemos juntos {nombre}!'


def consume_funciones(funcion_entrante):
    return funcion_entrante('Yvan')


def main():

    print(consume_funciones(presentarse))
    print(consume_funciones(estudiar_juntos))


if __name__ == '__main__':
    main()
