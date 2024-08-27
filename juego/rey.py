from juego.pieza import Pieza

class Rey(Pieza): # Definición de la clase Rey que hereda de la clase Pieza

    __nombre__ = "Rey" # Nombre del tipo de pieza
    __tipos_movimiento__ = ("especial") # El rey permite movimientos de tipo especial

    __str_blanco__ = "♚" # Carácter gráfico del rey para mostrar en blanco
    __str_negro__ = "♔" # Carácter gráfico del rey para mostrar en negro


    def checkMovimiento(self, x_destino, y_destino): # Método que define cómo se puede mover el rey

        if abs(x_destino - self.__x__) > 1 or abs(y_destino - self.__y__) > 1:
            raise ValueError("Movimiento inválido para el Rey. Debe moverse solo una casilla en cualquier dirección.")

        return True # Retorna True si el movimiento es permitido por el rey