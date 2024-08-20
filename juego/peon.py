from juego.pieza import Pieza
from juego.casilla import Casilla

class Peon(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Peón"

    def __str__(self):
        return "♟" if self.__color__ == "blanco" else "♙"

    def checkMovimiento(self, x_destino, y_destino, tablero):
        direccion = -1 if self.__color__ == "blanco" else 1

        pieza = tablero.get_pieza(x_destino, y_destino)

        # Movimiento de una casilla hacia adelante
        if (x_destino == self.__x__ + direccion and y_destino == self.__y__):
            if isinstance(pieza, Casilla):
                return True
        
        # Movimiento de dos casillas hacia adelante desde la posición inicial
        elif (x_destino == self.__x__ + (2 * direccion) and y_destino == self.__y__):
            if self.__x__ == (6 if self.__color__ == "blanco" else 1):
                if isinstance(tablero.get_pieza(self.__x__ + direccion, self.__y__), Casilla) and \
                    isinstance(pieza, Casilla):
                    return True

        # Captura en diagonal
        elif (x_destino == self.__x__ + direccion and abs(y_destino - self.__y__) == 1):
            if isinstance(pieza, Pieza) and pieza.color != self.__color__:
                return True

        # Movimiento inválido
        raise ValueError("Movimiento inválido para el peón.")