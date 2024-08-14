class Casilla(): # usada solo para casillas vacías
    
    def __init__(self, x, y):
        self.__color__ = "blanco" if (x + y) % 2 == 0 else "negro"
        self.__x__ = x
        self.__y__ = y

    def __str__(self):
        return "■" if self.__color__ == "blanco" else "□"