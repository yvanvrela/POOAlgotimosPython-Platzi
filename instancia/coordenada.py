class Coordenada():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        x_diff = (self.x - otra_cordenada.x)**2
        y_diff = (self.y - otra_cordenada.y)**2

        return (x_diff + y_diff)**0.5
