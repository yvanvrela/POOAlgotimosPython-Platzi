class Helado:
    def __init__(self, sabor_helado) -> None:
        self.__sabor_helado = sabor_helado

    @property
    def sabor_helado(self):
        return self.__sabor_helado

    @sabor_helado.setter
    def sabor_helado(self, sabor):
        self.__sabor_helado = sabor


if __name__ == '__main__':
    helado_chocolate = Helado(sabor_helado='chocolate')
    print(helado_chocolate.sabor_helado)
