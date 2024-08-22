class Pieza():
    
    def __init__(self, color, x, y):
        self.__color__ = color
        self.__x__ = x
        self.__y__ = y
        self.__nombre__ = ""
        self.__tipos_movimiento__ = ("")

    @property
    def color(self):
        return self.__color__
    
    @property
    def nombre(self):
        return self.__nombre__

    @property
    def x(self):
        return self.__x__

    @property
    def y(self):
        return self.__y__

    def puede_mover(self, tipo_movimiento):
        return tipo_movimiento in self.__tipos_movimiento__

    def mover(self, x_destino, y_destino):

            # Cambiar coordenadas de la pieza
            self.__x__ = x_destino 
            self.__y__ = y_destino

    def checkMovimiento(self, x_destino, y_destino):
        pass