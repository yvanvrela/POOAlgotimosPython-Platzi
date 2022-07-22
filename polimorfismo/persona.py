
class Persona:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self._acccion = 'Ando caminando'

    def avanza(self):
        print(self._acccion)


class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self._acccion = 'Ando moviendome en bicicleta'

    def avanza(self):
        return super().avanza()


def main() -> None:

    persona = Persona(nombre='Yvan')
    persona.avanza()

    ciclista = Ciclista(nombre='Aldo')
    ciclista.avanza()


if __name__ == '__main__':
    main()
