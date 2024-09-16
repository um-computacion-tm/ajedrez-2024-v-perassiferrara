from juego.excepciones import TorreMovementError
from juego.pieza import Pieza

class Torre(Pieza): # Definición de la clase Torre que hereda de la clase Pieza
    
    __nombre__ = "Torre" # Nombre del tipo de pieza
    __tipos_movimiento__ = ("perpendicular") # El torre permite movimientos de tipo perpendicular

    __str_blanco__ = "♜" # Carácter gráfico de la torre para mostrar en blanco
    __str_negro__ = "♖" # Carácter gráfico de la torre para mostrar en negro

    def checkMovimiento(self, x_destino, y_destino): # Método que define cómo se puede mover la torre

        if x_destino != self.__x__ and y_destino != self.__y__:
            raise TorreMovementError()

        return True # Retorna True si el movimiento es permitido por la torre