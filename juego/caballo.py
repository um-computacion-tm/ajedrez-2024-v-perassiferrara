from juego.pieza import Pieza

class Caballo(Pieza): # Definición de la clase Caballo que hereda de la clase Pieza

    __nombre__ = "Caballo" # Nombre del tipo de pieza
    __tipos_movimiento__ = ("especial") # El caballo permite movimientos de tipo especial

    def __str__(self):
        return "♞" if self.color == "blanco" else "♘" # Retorna el carácter gráfico del caballo para mostrar

    def checkMovimiento(self, x_destino, y_destino): # Método que define cómo se puede mover el caballo

        if (abs(x_destino - self.__x__), abs(y_destino - self.__y__)) not in [(2, 1), (1, 2)]:
            raise ValueError("Movimiento inválido para el Caballo. Debe moverse en forma de 'L'.")
        
        return True # Retorna True si el movimiento es permitido por el caballo