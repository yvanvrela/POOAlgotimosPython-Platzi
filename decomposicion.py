
class Automovil:
    def __init__(self, modelo, marca, color, cantidad_pasajeros, puerta, ruedas=4) -> None:
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.cantidad_pasajeros = cantidad_pasajeros
        self.puerta = puerta
        self.ruedas = ruedas
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)

    def recargar_tanque(self, cantidad: int) -> None:
        self._motor.cantidad_combustible = cantidad

    def acelerar(self, tipo='despacio') -> None:
        if tipo == 'rapida':
            self._motor.inyectar_combustible(10)
            print('Acelerando a 100 km/h')
        else:
            self._motor.inyectar_combustible(3)

        self._estado = 'en movimiento'


class Motor:
    def __init__(self, cilindros, cantidad_combustible=0, tipo='gasolina') -> None:
        self.cilindros = cilindros
        self.tipo = tipo
        self.cantidad_combustible = cantidad_combustible
        self._temperatura = 0

    def inyectar_combustible(self, cantidad) -> None:
        combustible_restante = self.cantidad_combustible - cantidad
        if combustible_restante >= 0:
            self.cantidad_combustible = combustible_restante
        else:
            print('Ya no hay combustible!')


if __name__ == '__main__':
    auto = Automovil('Hb20', 'Hyndai', 'Gris', 4, 4)
    auto.recargar_tanque(100)

    auto.acelerar('rapida')
    print(auto._motor.cantidad_combustible)

    auto.acelerar()
    print(auto._motor.cantidad_combustible)
