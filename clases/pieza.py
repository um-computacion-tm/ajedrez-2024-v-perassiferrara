from excepciones import SelectionCancel
from casilla import Casilla

class Pieza():
    
    def __init__(self, color, x, y):
        self.__color__ = color
        self.__x__ = x
        self.__y__ = y

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
    
    @property
    def color(self):
        return self.__color__



    def set_x(self, x):
        try:
            if 0 <= x < 8:
                self.__x__ = x
            else:
                raise ValueError("Coordenada X inválida")
        
        except ValueError as e:
            raise(e)
        
    def set_y(self, y):
        try:
            if 0 <= y < 8:
                self.__y__ = y

            else:
                raise ValueError("Coordenada Y inválida")
        
        except ValueError as e:
            raise(e)
        
    def checkMismaCasilla(self, x_destino, y_destino):
        # Verificar si se intenta mover a la misma casilla
        if x_destino == self.__x__ and y_destino == self.__y__:
            raise ValueError("No se puede mover a la misma casilla")

    def checkDestino(self, x_destino, y_destino, tablero):
        # Verificar si la casilla de destino está ocupada por una pieza aliada
        pieza_destino = tablero.cuadricula(x_destino, y_destino)
        if isinstance(pieza_destino, Pieza) and pieza_destino.__color__ == self.__color__: 
            raise ValueError("No se puede mover porque la casilla destino está ocupada por una pieza aliada")
        elif isinstance(pieza_destino, Pieza) and pieza_destino.__color__ != self.__color__:
            return True
        else:
            return False
            

    def mover(self, posicion_destino, tablero):
        while True:

            if posicion_destino == "0":  # Si el input para destino es 0, se deselecciona la pieza
                raise SelectionCancel("Selección cancelada")

            posicion_destino = posicion_destino.upper()

            try:
                x_destino, y_destino = tablero.traducir_a_coordenadas(posicion_destino)

            except TypeError:
                raise TypeError("Formato de entrada inválido. Use notación de ajedrez (a1, b7, etc.)")         

            if self.checkMovimiento(x_destino, y_destino, tablero):

                self.checkMismaCasilla(x_destino, y_destino)
                ocupada_por_rival = self.checkDestino(x_destino, y_destino, tablero)

                # Cambiar casilla origen por vacía
                tablero.set_cuadricula(self.x, self.y, Casilla(self.x, self.y))

                posicion_origen = tablero.traducir_a_posicion(self.x, self.y)

                # Cambiar coordenadas de la pieza
                self.set_x(x_destino)
                self.set_y(y_destino)

                pieza_destino = tablero.cuadricula(x_destino, y_destino)

                # Asignar la pieza a la casilla destino 
                tablero.set_cuadricula(x_destino, y_destino, self) 

                # Devuelve la acción realizada

                if ocupada_por_rival:
                    return(f"{self.__nombre__} {self.__color__} {posicion_origen} captura a {pieza_destino.__nombre__} {pieza_destino.__color__} en {posicion_destino}\n")
                else:    
                    return(f"{self.__nombre__} {self.__color__} {posicion_origen} se mueve a {posicion_destino}\n")
            
            return False