from juego.pieza import Pieza

class Caballo(Pieza):

    __nombre__ = "Caballo"
    __tipos_movimiento__ = ("especial")

    def __str__(self):
        return "♞" if self.color == "blanco" else "♘"

    def checkMovimiento(self, x_destino, y_destino):

        if (abs(x_destino - self.__x__), abs(y_destino - self.__y__)) not in [(2, 1), (1, 2)]:
            raise ValueError("Movimiento inválido para el Caballo. Debe moverse en forma de 'L'.")
        
        return True