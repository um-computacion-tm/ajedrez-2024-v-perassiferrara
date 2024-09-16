from juego.excepciones import PeonMovementError
from juego.pieza import Pieza

class Peon(Pieza): # Definición de la clase Peon que hereda de la clase Pieza

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__primera_posicion__ = True # Indica si la instancia de peón está en su posición inicial

    __nombre__ = "Peón" # Nombre del tipo de pieza
    __tipos_movimiento__ = ("peon") # El peón permite movimientos de tipo peón

    __str_blanco__ = "♟" # Carácter gráfico del peón para mostrar en blanco
    __str_negro__ = "♙" # Carácter gráfico del peón para mostrar en negro

    @property
    def primera_posicion(self):
        return self.__primera_posicion__
    
    def set_primera_posicion(self, primera_posicion): # Método que establece la propiedad primera_posicion
        self.__primera_posicion__ = primera_posicion


    def checkMovimiento(self, x_destino, y_destino): # Método que define cómo se puede mover el peón
        direccion = -1 if self.__color__ == "blanco" else 1

        if self.checkMovimiento1Casilla(x_destino, y_destino, direccion):
            # Verifica si el peón puede avanzar una casilla hacia adelante
            return True
        
        if self.checkMovimiento2Casillas(x_destino, y_destino, direccion):
            # Verifica si el peón puede avanzar dos casillas hacia adelante
            return True
        
        if self.checkMovimientoDiagonal(x_destino, y_destino, direccion):
            # Verifica si el peón puede avanzar en diagonal
            return True # 
        
        # Movimiento inválido
        raise PeonMovementError()



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