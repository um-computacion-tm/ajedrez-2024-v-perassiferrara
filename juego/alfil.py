from juego.pieza import Pieza

class Alfil(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Alfil"
        self.__tipos_movimiento__ = ("diagonal")

    def __str__(self):
        return "♝" if self.__color__ == "blanco" else "♗"

    def checkMovimiento(self, x_destino, y_destino):

        if abs(x_destino - self.__x__) != abs(y_destino - self.__y__):
            raise ValueError("El Alfil debe moverse en una línea recta diagonal")
            
        return True