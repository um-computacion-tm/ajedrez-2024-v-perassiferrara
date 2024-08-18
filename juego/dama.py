from juego.pieza import Pieza

class Dama(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Dama"

    def __str__(self):
        return "♛" if self.__color__ == "blanco" else "♕"

    def checkMovimiento(self, x_destino, y_destino, tablero):

        try:            
            if (x_destino != self.__x__ and y_destino != self.__y__) and abs(x_destino - self.__x__) != abs(y_destino - self.y):
                raise ValueError("Movimiento inválido para la Dama. Debe moverse en una línea recta horizontal, vertical o diagonal.")
            
            paso_x = 1 if x_destino > self.__x__ else -1 if x_destino < self.__x__ else 0
            paso_y = 1 if y_destino > self.__y__ else -1 if y_destino < self.__y__ else 0
            x_comparacion, y_comparacion = self.__x__ + paso_x, self.__y__ + paso_y

            while x_comparacion != x_destino or y_comparacion != y_destino:
                if tablero.get_pieza(x_comparacion,y_comparacion) == Pieza:
                    raise ValueError("No se puede mover porque hay una pieza en el camino")
                x_comparacion += paso_x
                y_comparacion += paso_y

            return True
        
        except ValueError as e:
            raise(e)