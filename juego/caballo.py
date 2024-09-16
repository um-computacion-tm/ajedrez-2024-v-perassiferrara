from juego.excepciones import CaballoMovementError
from juego.pieza import Pieza

class Caballo(Pieza): # Definición de la clase Caballo que hereda de la clase Pieza

    __nombre__ = "Caballo" # Nombre del tipo de pieza
    __tipos_movimiento__ = ("especial") # El caballo permite movimientos de tipo especial

    __str_blanco__ = "♞" # Carácter gráfico del caballo para mostrar en blanco
    __str_negro__ = "♘" # Carácter gráfico del caballo para mostrar en negro

    def checkMovimiento(self, x_destino, y_destino): # Método que define cómo se puede mover el caballo

        if (abs(x_destino - self.__x__), abs(y_destino - self.__y__)) not in [(2, 1), (1, 2)]:
            raise CaballoMovementError()
        
        return True # Retorna True si el movimiento es permitido por el caballo