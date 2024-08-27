from juego.pieza import Pieza

class Alfil(Pieza): # Definición de la clase Alfil que hereda de la clase Pieza

    __nombre__ = "Alfil" # Nombre del tipo de pieza
    __tipos_movimiento__ = ("diagonal") # El alfil permite movimientos de tipo diagonal

    __str_blanco__ = "♝" # Carácter gráfico del alfil para mostrar en blanco
    __str_negro__ = "♗" # Carácter gráfico del alfil para mostrar en negro

    def checkMovimiento(self, x_destino, y_destino): # Método que define cómo se puede mover el alfil

        if abs(x_destino - self.__x__) != abs(y_destino - self.__y__):
            raise ValueError("El Alfil debe moverse en una línea recta diagonal")
            
        return True # Retorna True si el movimiento es permitido por el alfil