from juego.excepciones import *
from juego.pieza import *
from juego.casilla import *
from juego.peon import *
from juego.torre import *
from juego.caballo import *
from juego.alfil import *
from juego.dama import *
from juego.rey import *


class Tablero():

    def __init__(self):
        self.__cuadricula__ = [[Casilla(x = fila, y = columna)
                                for columna in range(8)]
                                for fila in range(8)]
        # Al crear el tablero, se crean las casillas solas (vacias)

        self.inicializar_piezas()

    def inicializar_piezas(self):

        piezas_especiales_inicio = [Torre, Caballo, Alfil, Dama, Rey, Alfil, Caballo, Torre]

        # Piezas blancas
        for columna, pieza_especial in enumerate(piezas_especiales_inicio):

            pieza_especial = pieza_especial("blanco", 7, columna)
            peon = Peon("blanco", 6, columna)

            self.__cuadricula__[pieza_especial.x][pieza_especial.y] = pieza_especial
            self.__cuadricula__[peon.x][peon.y] = peon

        # Piezas negras
        for columna, pieza_especial in enumerate(piezas_especiales_inicio):

            pieza_especial = pieza_especial("negro", 0, columna)
            peon = Peon("negro", 1, columna)

            self.__cuadricula__[pieza_especial.x][pieza_especial.y] = pieza_especial
            self.__cuadricula__[peon.x][peon.y] = peon

    def get_pieza(self, x, y):
        return self.__cuadricula__[x][y]  

    def set_pieza(self, x, y, objeto):
        self.__cuadricula__[x][y] = objeto


    def __str__(self):

        string_tablero = ""

        columnas = ("A", "B", "C", "D", "E", "F", "G", "H")

        for i in range(8):
            # Añade número de fila a la izquierda
            string_tablero += f" {8 - i}  "

            # Añade contenido de cada fila
            string_tablero += "  ".join(str(self.__cuadricula__[i][j]) for j in range(8)) + "\n"
        
        # Agrega la fila final de letras
        string_tablero += "    " + "  ".join(columnas) + "\n"

        return string_tablero