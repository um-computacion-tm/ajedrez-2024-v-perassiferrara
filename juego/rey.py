from juego.pieza import Pieza

class Rey(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Rey"

    def __str__(self):
        return "♚" if self.__color__ == "blanco" else "♔"

    def checkMovimiento(self, x_destino, y_destino):

        if abs(x_destino - self.__x__) > 1 or abs(y_destino - self.__y__) > 1:
            raise ValueError("Movimiento inválido para el Rey. Debe moverse solo una casilla en cualquier dirección.")

        return True