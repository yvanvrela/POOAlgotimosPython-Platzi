from abstraccion.contabilidad import Contabilidad
from instancia.coordenada import Coordenada
from decomposicion.automovil import Automovil
from abstraccion.lavadora import Lavadora
from herencia.rectangulo import Rectangulo
from herencia.cuadrado import Cuadrado


def main() -> None:
    """ Instancia """
    # coord_1 = Coordenada(3, 30)
    # coord_2 = Coordenada(4, 8)

    # print(coord_1.distancia(coord_2))
    # print(isinstance(coord_2, Coordenada))

    """ Decomposicion """
    # auto = Automovil(modelo='Hb20', marca='Hyndai',
    #                  color='Gris', cantidad_pasajeros=4, puerta=5)
    # auto.recargar_tanque(100)

    # auto.acelerar('rapida')
    # print(auto._motor.cantidad_combustible)

    # auto.acelerar()
    # print(auto._motor.cantidad_combustible)

    """ Abstraccion"""
    # lavadora = Lavadora()
    # lavadora.lavar()

    """ Herencia """
    # rectangulo = Rectangulo(base=3, altura=4)
    # print(rectangulo.area())

    # cuadrado = Cuadrado(lado=5)
    # print(cuadrado.area())

    # contabilidad = Contabilidad()
    # contabilidad.liquidacion_de_documentos(mes_presentacion='Junio')


if __name__ == '__main__':
    main()
