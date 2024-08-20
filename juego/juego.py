from juego.tablero import Tablero
from juego.excepciones import *
from juego.pieza import *
from juego.casilla import *
from juego.peon import *
from juego.torre import *
from juego.caballo import *
from juego.alfil import *
from juego.dama import *
from juego.rey import *



class JuegoAjedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "blanco"
        self.__num_turno__ = 1

    @property
    def tablero(self):
        return self.__tablero__

    @property
    def turno(self):
        return self.__turno__
    
    @property
    def num_turno(self):
        return self.__num_turno__
    
    def turno_actual(self):
        return f"Turno {self.num_turno}: {self.turno}"

    def cambiar_turno(self):
        self.__turno__ = "negro" if self.__turno__ == "blanco" else "blanco"
        self.__num_turno__ += 1

    def iniciar_juego(self):
        return "Tablero Inicial:\n" + str(self.__tablero__)

    def seleccionar_opcion(self, opcion):
        if opcion not in ("1", "2"):
            return "Opción no válida"
        elif opcion == "2":
            return "Cerrando juego"
        elif opcion == "1":
            return "Juego iniciado"

    def get_pieza(self, x, y):
        return self.__tablero__.get_pieza(x, y)

    def checkMismaCasilla(self, x_origen, y_origen, x_destino, y_destino):
        if x_origen == x_destino and y_origen == y_destino:
            raise ValueError("No se puede mover a la misma casilla")
        
    def checkColorPieza(self, pieza):
        # Verificar si la pieza seleccionada es del color propio
        if pieza.color != self.__turno__:
            raise ColorError("No puedes seleccionar piezas de tu oponente")



    def validar_origen(self, x_origen, y_origen):

        pieza = self.__tablero__.get_pieza(x_origen, y_origen)

        self.__tablero__.checkCasillaVacia(pieza)
        self.checkColorPieza(pieza)

        return pieza


    def validar_destino(self, x_origen, y_origen, x_destino, y_destino):

        try:
            pieza = self.get_pieza(x_origen, y_origen)
            pieza_destino = self.get_pieza(x_destino, y_destino)

            self.checkMismaCasilla(x_origen, y_origen, x_destino, y_destino)
            self.__tablero__.checkDestino(pieza, pieza_destino)
            pieza.checkMovimiento(x_destino, y_destino, self.__tablero__)

        except Exception as e:
            raise e




    def mover_pieza(self, x_origen, y_origen, x_destino, y_destino):

        pieza = self.get_pieza(x_origen, y_origen)
    
        try:

            # Actualizar coordenadas internas de la pieza
            pieza.mover(x_destino, y_destino)

            # Asignar pieza a su nueva posición en el tablero 
            self.__tablero__.set_pieza(x_destino, y_destino, pieza)

            # Asignar casilla vacía a la posición de origen en el tablero
            self.__tablero__.set_pieza(x_origen, y_origen, Casilla(x_origen, y_origen))

            # Verifica condición de victoria
            if self.checkVictoria():
                return "Victoria"

            # Si no es victoria, indica que el movimiento fue correcto
            return True           

        except Exception as e:  # Si ocurre algún error, devuelve el mensaje de error
            raise e
    
    def checkVictoria(self):
        for fila in range(8):
            for columna in range(8):
                pieza = self.get_pieza(fila, columna)

                if isinstance(pieza, Rey) and pieza.color != self.turno:
                    return False

        return True    
    
    
    def mostrar_tablero(self):
        return str(self.__tablero__)

    def finalizar_juego(self):
        return "\nJuego terminado: Empate\n"
