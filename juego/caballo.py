from juego.pieza import Pieza

class Caballo(Pieza):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Caballo"

    def __str__(self):
        return "♞" if self.__color__ == "blanco" else "♘"

    def checkMovimiento(self, x_destino, y_destino, tablero):

        try:
            if (abs(x_destino - self.__x__), abs(y_destino - self.__y__)) not in [(2, 1), (1, 2)]:
                raise ValueError("Movimiento inválido para el Caballo. Debe moverse en forma de 'L'.")
            
            return True

        except ValueError as e:
            raise(e)