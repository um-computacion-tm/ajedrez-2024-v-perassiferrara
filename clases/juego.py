from clases.tablero import Tablero
from clases.excepciones import *
from clases.pieza import *
from clases.casilla import *
from clases.peon import *
from clases.torre import *
from clases.caballo import *
from clases.alfil import *
from clases.dama import *
from clases.rey import *



class JuegoAjedrez:
    def __init__(self):
        self.__tablero__ = Tablero()

    def iniciar_juego(self):
        return "Tablero Inicial:\n" + str(self.__tablero__)

    def seleccionar_opcion(self, opcion):
        if opcion not in ("1", "2"):
            return "Opción no válida"
        elif opcion == "2":
            return "Juego terminado: Empate"
        elif opcion == "1":
            return "Juego iniciado"

    def turno_actual(self):
        return f"Turno {self.__tablero__.num_turno}: {self.__tablero__.turno}"

    def seleccionar_pieza(self, entrada):
        try:
            if self.__tablero__.seleccionarPieza(entrada):
                pieza = self.__tablero__.seleccionarPieza(entrada)
                posicion = self.__tablero__.traducir_a_posicion(pieza.x, pieza.y)
                return pieza, posicion
        except Exception as e:
            return str(e)

    def mover_pieza(self, pieza, entrada_destino):
        try:
            if pieza.mover(entrada_destino, self.__tablero__):
                if self.__tablero__.checkVictoria():
                    self.__tablero__ = Tablero()
                    return "Victoria"
            
                return "Movimiento exitoso"
        except Exception as e:
            return str(e)

    def mostrar_tablero(self):
        return str(self.__tablero__)

    def finalizar_juego(self):
        return "Juego terminado: Empate"

    def cambiar_turno(self):
        self.__tablero__.cambiarTurno()
