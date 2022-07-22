class Inmueble:

    def __init__(self, precio: int) -> None:
        self._precio = precio  # atributo privado

    @property
    def precio(self):  # cuando se ejecute departamento.precio
        return self._precio  # retornar el atributo privado _precio

    @precio.setter  # setter, se ejecutará cuando se intente cambiar los valores
    def precio(self, nuevo_valor: int) -> None:
        if nuevo_valor < 1000 or nuevo_valor > 200000:  # si valor es menor a 1000 o mayor a 200000
            # arrojamos error
            raise ValueError('No es posible cambiar a estos valores')
        else:
            self._precio = nuevo_valor  # asignamos el nuevo valor
            # imprimimos el nuevo valor
            print(f'El nuevo valor del departamento es: {self._precio}')

    @precio.deleter  # supersor
    def precio(self) -> None:
        del self._precio  # borramos el atributo


if __name__ == '__main__':

    # Instancia
    casa_condominio = Inmueble(precio=1000)
    casa_playa = Inmueble(precio=2000)

    # Implementando getter
    print(casa_condominio.precio)

    # Implementando setter
    casa_condominio.precio = 2500

    del casa_condominio.precio
