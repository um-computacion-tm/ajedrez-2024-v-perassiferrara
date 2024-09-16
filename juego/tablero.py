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
        self.__cuadricula__ = [[Casilla(x = fila, y = columna) # Crea una matriz de posiciones del tablero
                                for columna in range(8)]
                                for fila in range(8)]
        # Al crear la matriz, las posiciones son ocupadas por casillas vacías

        self.inicializar_piezas() # Se llama al método que inicializa las piezas

    def inicializar_piezas(self): # Coloca las piezas iniciales del tablero (blancas y negras)

        piezas_especiales_inicio = (Torre, Caballo, Alfil, Dama, Rey, Alfil, Caballo, Torre)

        # Piezas blancas: 
        for columna, pieza_especial in enumerate(piezas_especiales_inicio): # Itera sobre las piezas iniciales y columnas

            pieza_especial = pieza_especial("blanco", 7, columna)
            peon = Peon("blanco", 6, columna)

            self.__cuadricula__[pieza_especial.x][pieza_especial.y] = pieza_especial
            self.__cuadricula__[peon.x][peon.y] = peon

        # Con cada iteración, se crea una pieza especial negra y un peon negro y se asignan en sus respectivas posiciones  



        # Piezas negras
        for columna, pieza_especial in enumerate(piezas_especiales_inicio): # Itera sobre las piezas iniciales y columnas

            pieza_especial = pieza_especial("negro", 0, columna)
            peon = Peon("negro", 1, columna)

            self.__cuadricula__[pieza_especial.x][pieza_especial.y] = pieza_especial
            self.__cuadricula__[peon.x][peon.y] = peon

        # Con cada iteración, se crea una pieza especial blanca y un peon blanco y se asignan en sus respectivas posiciones  




    def get_pieza(self, x, y): # Método que devuelve la pieza en la posición (x,y)
        return self.__cuadricula__[x][y]  

    def set_pieza(self, x, y, objeto): # Método que establece el objeto/pieza indicado en la posición (x,y)
        self.__cuadricula__[x][y] = objeto


    def __str__(self): # Método que devuelve una representación "gráfica" del tablero

        string_tablero = "" # Crea un string vacío

        columnas = ("A", "B", "C", "D", "E", "F", "G", "H")

        for i in range(8):
            # Añade número de fila a la izquierda
            string_tablero += f" {8 - i}  "

            # Añade contenido de la fila
            string_tablero += "  ".join(str(self.__cuadricula__[i][j]) for j in range(8)) + "\n"
        
        # Agrega la fila final de letras
        string_tablero += "    " + "  ".join(columnas) + "\n"

        return string_tablero