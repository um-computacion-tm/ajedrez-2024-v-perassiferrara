from juego.pieza import Pieza

class Alfil(Pieza):

    __nombre__ = "Alfil"
    __tipos_movimiento__ = ("diagonal")

    def __str__(self):
        return "♝" if self.__color__ == "blanco" else "♗"

    def checkMovimiento(self, x_destino, y_destino):

        if abs(x_destino - self.__x__) != abs(y_destino - self.__y__):
            raise ValueError("El Alfil debe moverse en una línea recta diagonal")
            
        return True