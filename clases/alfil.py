from clases.pieza import Pieza

class Alfil(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Alfil"

    def __str__(self):
        return "♝" if self.__color__ == "blanco" else "♗"

    def checkMovimiento(self, x_destino, y_destino, tablero):

        try:
            if abs(x_destino - self.__x__) != abs(y_destino - self.__y__):
                raise ValueError("El Alfil debe moverse en una línea recta diagonal")
            
            paso_x = 1 if x_destino > self.__x__ else -1
            paso_y = 1 if y_destino > self.__y__ else -1
            x_comparacion, y_comparacion = self.__x__ + paso_x, self.__y__ + paso_y

            while x_comparacion != x_destino and y_comparacion != y_destino:
                if isinstance(tablero.cuadricula(x_comparacion,y_comparacion), Pieza):
                    raise ValueError("No se puede mover porque hay una pieza en el camino")
                x_comparacion += paso_x
                y_comparacion += paso_y
                
            return True
        
        except ValueError as e:
            print(e, "\n")