class Casilla(): # Definición de la clase Casilla, usada solo para casillas vacías
    
    def __init__(self, x, y):
        self.__color__ = "blanco" if (x + y) % 2 == 0 else "negro"
        # Las casillas tienen un color fijo según su posición en el tablero
        self.__x__ = x
        self.__y__ = y

    @property
    def x(self):
        return self.__x__

    @property
    def y(self):
        return self.__y__

    def __str__(self):
        return "■" if self.__color__ == "blanco" else "□" # Retorna el carácter gráfico de la casilla para mostrar