from tablero import Tablero
from excepciones import *
from pieza import *
from casilla import *
from peon import *
from torre import *
from caballo import *
from alfil import *
from dama import *
from rey import *



class JuegoAjedrez:
    def __init__(self):
        self.__tablero__ = Tablero()

    def iniciar_juego(self):
        return "Tablero Inicial:\n" + str(self.__tablero__)

    def seleccionar_opcion(self, opcion):
        if opcion not in ("1", "2"):
            return "Opción no válida"
        elif opcion == "2":
            return "Cerrando juego"
        elif opcion == "1":
            return "Juego iniciado"

    def turno_actual(self):
        return f"Turno {self.__tablero__.num_turno}: {self.__tablero__.turno}"

    def seleccionar_pieza(self, x, y):
        try:
            if self.__tablero__.seleccionarPieza(x, y):
                pieza = self.__tablero__.seleccionarPieza(x, y)
                return pieza
        except Exception as e:
            raise e

    def mover_pieza(self, pieza, x_destino, y_destino):
        try:
            if pieza.mover(x_destino, y_destino, self.__tablero__):
                if self.__tablero__.checkVictoria():
                    self.__tablero__ = Tablero()
                    return "Victoria"
            
                return pieza.mover(x_destino, y_destino, self.__tablero__)
        except Exception as e:
            return str(e)

    def mostrar_tablero(self):
        return str(self.__tablero__)

    def finalizar_juego(self):
        return "\nJuego terminado: Empate\n"

    def cambiar_turno(self):
        self.__tablero__.cambiar_turno()
