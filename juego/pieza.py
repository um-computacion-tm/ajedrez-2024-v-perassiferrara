class Pieza():
    
    def __init__(self, color, x, y): # Definición de la clase Pieza con sus atributos
        self.__color__ = color
        self.__x__ = x
        self.__y__ = y



    # Los métodos @property (propiedades) permiten acceder a los atributos de la clase pieza desde el exterior 

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


    # Método que devuelve True si el tipo de movimiento es permitido por la pieza
    def puede_mover(self, tipo_movimiento):
        return tipo_movimiento in self.__tipos_movimiento__

    # Método que cambia las coordenadas de la pieza a las especificadas
    def mover(self, x_destino, y_destino):
            self.__x__ = x_destino 
            self.__y__ = y_destino