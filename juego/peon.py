from juego.pieza import Pieza

class Peon(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Peón"
        self.__primera_posicion__ = True
        self.__tipos_movimiento__ = ("peon")

    @property
    def primera_posicion(self):
        return self.__primera_posicion__
    
    def set_primera_posicion(self, primera_posicion):
        self.__primera_posicion__ = primera_posicion

    def __str__(self):
        return "♟" if self.__color__ == "blanco" else "♙"

    def checkMovimiento(self, x_destino, y_destino):
        direccion = -1 if self.__color__ == "blanco" else 1

        if self.checkMovimiento1Casilla(x_destino, y_destino, direccion):
            return True
        
        if self.checkMovimiento2Casillas(x_destino, y_destino, direccion):
            return True
        
        if self.checkMovimientoDiagonal(x_destino, y_destino, direccion):
            return True
        
        # Movimiento inválido
        raise ValueError("Movimiento inválido para el peón.")



    def checkMovimiento1Casilla(self, x_destino, y_destino, direccion):
        # Movimiento de una casilla hacia adelante
        if (x_destino == self.__x__ + direccion and y_destino == self.__y__):
            return True
        
    def checkMovimiento2Casillas(self, x_destino, y_destino, direccion):
        # Movimiento de dos casillas hacia adelante desde la posición inicial
        if (x_destino == self.__x__ + (2 * direccion) and y_destino == self.__y__):
            return True

    def checkMovimientoDiagonal(self, x_destino, y_destino, direccion):
        # Captura en diagonal
        if (x_destino == self.__x__ + direccion and abs(y_destino - self.__y__) == 1):
            return True