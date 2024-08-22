from juego.pieza import Pieza

class Dama(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Dama"

    def __str__(self):
        return "♛" if self.__color__ == "blanco" else "♕"

    def checkMovimiento(self, x_destino, y_destino):
          
        if (x_destino != self.__x__ and y_destino != self.__y__) and abs(x_destino - self.__x__) != abs(y_destino - self.y):
            raise ValueError("Movimiento inválido para la Dama. Debe moverse en una línea recta horizontal, vertical o diagonal.")

        return True