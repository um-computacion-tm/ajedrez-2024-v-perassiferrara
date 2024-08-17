from pieza import Pieza

class Torre(Pieza):
    
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__nombre__ = "Torre"

    def __str__(self):
        return "♜" if self.__color__ == "blanco" else "♖"

    def checkMovimiento(self, x_destino, y_destino, tablero):

        try:
            if x_destino != self.__x__ and y_destino != self.__y__:
                raise ValueError("No se puede mover en diagonal. Se debe mover en una línea recta horizontal o vertical")
            

            if x_destino != self.__x__:
                paso = 1 if x_destino > self.__x__ else -1
                for x_comparacion in range(self.__x__ + paso, x_destino, paso):
                    if isinstance(tablero.get_pieza(x_comparacion,self.y), Pieza):
                        raise ValueError("No se puede mover porque hay una pieza en el camino")
                    
            elif y_destino != self.__y__:
                paso = 1 if y_destino > self.__y__ else -1
                for y_comparacion in range(self.__y__ + paso, y_destino, paso):
                    if isinstance(tablero.get_pieza(self.x,y_comparacion), Pieza):
                        raise ValueError("No se puede mover porque hay una pieza en el camino")

            return True
        
        except ValueError as e:
            raise(e)