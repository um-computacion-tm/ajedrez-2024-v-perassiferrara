from juego.pieza import Pieza

class Dama(Pieza): # Definición de la clase Dama que hereda de la clase Pieza

    __nombre__ = "Dama" # Nombre del tipo de pieza
    __tipos_movimiento__ = ("perpendicular", "diagonal") # La dama permite movimientos de tipo perpendicular y diagonal

    def __str__(self):
        return "♛" if self.__color__ == "blanco" else "♕" # Retorna el carácter gráfico de la dama para mostrar

    def checkMovimiento(self, x_destino, y_destino): # Método que define cómo se puede mover la dama

        if (x_destino != self.__x__ and y_destino != self.__y__) and abs(x_destino - self.__x__) != abs(y_destino - self.y):
            raise ValueError("Movimiento inválido para la Dama. Debe moverse en una línea recta horizontal, vertical o diagonal.")

        return True # Retorna True si el movimiento es permitido por la dama