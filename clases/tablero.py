from clases.excepciones import *
from clases.pieza import *
from clases.casilla import *
from clases.peon import *
from clases.torre import *
from clases.caballo import *
from clases.alfil import *
from clases.dama import *
from clases.rey import *


class Tablero():

    def __init__(self):
        self.__cuadricula__ = [[Casilla(x = fila, y = columna)
                                for columna in range(8)]
                                for fila in range(8)]
        # Al crear el tablero, se crean las casillas solas

        self.__filas__ = ("8", "7", "6", "5", "4", "3", "2", "1")
        self.__columnas__ = ("A", "B", "C", "D", "E", "F", "G", "H")
        self.__posiciones__ = [columna+fila for columna in self.__columnas__ for fila in self.__filas__]
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
    
    def cambiarTurno(self):
        self.__turno__ = "negro" if self.__turno__ == "blanco" else "blanco"
        self.__num_turno__ += 1

    def cuadricula(self, x = None, y = None):
        return self.__cuadricula__[x][y]

    def set_cuadricula(self, x, y, objeto):
        self.__cuadricula__[x][y] = objeto

    def traducir_a_coordenadas(self, notacion_ajedrez):
        notacion_ajedrez = notacion_ajedrez.upper()

        if notacion_ajedrez in self.__posiciones__:
            # Si la posicion dada existe en el tablero, devuelve las coordenadas
            y = self.__columnas__.index(notacion_ajedrez[0].upper())
            x = self.__filas__.index(notacion_ajedrez[1])
            return x, y
        else:
            raise ValueError("Posición no válida. Use casillas del tablero (a-h y 1-8)")

    def traducir_a_posicion(self, fila, columna):
        return self.__columnas__[columna] + self.__filas__[fila]

    def seleccionarPieza(self, entrada):
        while True:
            x, y = self.traducir_a_coordenadas(entrada)
            pieza = self.__cuadricula__[x][y]

            if isinstance(pieza, Casilla):
                raise EmptyError(f"No hay ninguna pieza en la casilla {self.traducir_a_posicion(x, y)}")

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

        for i in range(8):
            # Añade número de fila a la izquierda
            string_tablero += f" {8 - i}  "

            # Añade contenido de cada fila
            string_tablero += "  ".join(str(self.__cuadricula__[i][j]) for j in range(8)) + "\n"
        
        # Agrega la fila final de letras
        string_tablero += "    " + "  ".join(self.__columnas__) + "\n"

        return string_tablero