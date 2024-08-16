from excepciones import *
from pieza import *
from casilla import *
from peon import *
from torre import *
from caballo import *
from alfil import *
from dama import *
from rey import *


class Tablero():

    def __init__(self):
        self.__cuadricula__ = [[Casilla(x = fila, y = columna)
                                for columna in range(8)]
                                for fila in range(8)]
        # Al crear el tablero, se crean las casillas solas

        self.__turno__ = "blanco"
        self.__num_turno__ = 1

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



    @property
    def turno(self):
        return self.__turno__
    
    @property
    def num_turno(self):
        return self.__num_turno__
    
    def cambiar_turno(self):
        self.__turno__ = "negro" if self.__turno__ == "blanco" else "blanco"
        self.__num_turno__ += 1

    def cuadricula(self, x = None, y = None):
        return self.__cuadricula__[x][y]

    def set_cuadricula(self, x, y, objeto):
        self.__cuadricula__[x][y] = objeto


    def seleccionarPieza(self, x, y):
        pieza = self.__cuadricula__[x][y]

        if isinstance(pieza, Casilla):
            raise EmptyError(f"No hay ninguna pieza en la casilla")

        if pieza.color != self.__turno__:
            raise ColorError("No puedes seleccionar piezas de tu oponente")

        return pieza



    def checkVictoria(self):
        for fila in self.__cuadricula__:
            for casilla in fila:

                if isinstance(casilla, Pieza) and casilla.color != self.turno:
                    return False

        return True

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