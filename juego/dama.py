from juego.excepciones import DamaMovementError
from juego.pieza import Pieza

class Dama(Pieza): # Definición de la clase Dama que hereda de la clase Pieza

    __nombre__ = "Dama" # Nombre del tipo de pieza
    __tipos_movimiento__ = ("perpendicular", "diagonal") # La dama permite movimientos de tipo perpendicular y diagonal

    __str_blanco__ = "♛" # Carácter gráfico de la dama para mostrar en blanco
    __str_negro__ = "♕" # Carácter gráfico de la dama para mostrar en negro

    def checkMovimiento(self, x_destino, y_destino): # Método que define cómo se puede mover la dama

        if (x_destino != self.__x__ and y_destino != self.__y__) and abs(x_destino - self.__x__) != abs(y_destino - self.y):
            raise DamaMovementError()

        return True # Retorna True si el movimiento es permitido por la dama