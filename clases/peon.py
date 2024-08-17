from pieza import Pieza
from casilla import Casilla

class Peon(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Peón"

    def __str__(self):
        return "♟" if self.__color__ == "blanco" else "♙"

    def checkMovimiento(self, x_destino, y_destino, tablero):
        direccion = -1 if self.__color__ == "blanco" else 1

        # Movimiento de una casilla hacia adelante
        if (tablero.get_pieza(x_destino, y_destino).x == self.x + direccion and tablero.get_pieza(x_destino, y_destino).y == self.y):
            if isinstance(tablero.get_pieza(x_destino, y_destino), Casilla):
                return True
        
        # Movimiento de dos casillas hacia adelante desde la posición inicial
        elif (tablero.get_pieza(x_destino, y_destino).x == self.x + (2 * direccion) and tablero.get_pieza(x_destino, y_destino).y == self.y):
            if self.__x__ == (6 if self.__color__ == "blanco" else 1):
                if isinstance(tablero.get_pieza(self.__x__ + direccion, self.__y__), Casilla) and \
                    isinstance(tablero.get_pieza(x_destino, y_destino), Casilla):
                    return True

        # Captura en diagonal
        elif (tablero.get_pieza(x_destino, y_destino).x == self.x + direccion and abs(tablero.get_pieza(x_destino, y_destino).y - self.y) == 1):
            if isinstance(tablero.get_pieza(x_destino, y_destino), Pieza) and \
               tablero.get_pieza(x_destino, y_destino).color != self.__color__:
                return True

        # Movimiento inválido
        raise ValueError("Movimiento inválido. Solo puede avanzar una casilla vacía ocapturar una pieza en diagonal hacia adelante, o avanzar dos casillas desde la posición inicial si están vacías.")