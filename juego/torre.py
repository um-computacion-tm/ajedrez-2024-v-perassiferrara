from juego.pieza import Pieza

class Torre(Pieza):
    
    __nombre__ = "Torre"
    __tipos_movimiento__ = ("perpendicular")

    def __str__(self):
        return "♜" if self.__color__ == "blanco" else "♖"

    def checkMovimiento(self, x_destino, y_destino):

        if x_destino != self.__x__ and y_destino != self.__y__:
            raise ValueError("No se puede mover en diagonal. Se debe mover en una línea recta horizontal o vertical")

        return True